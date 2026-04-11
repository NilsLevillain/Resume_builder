"""
Export du CV en HTML et PDF.

Compatible avec :
  • Nouveau format → variables séparées (PERSONAL, SUMMARY, ...)
  • Ancien format  → dictionnaire unique (CV = {...})
"""
import os
import shutil
import subprocess
import data.cv_content as _mod

from data.cv_config import OUTPUT_DIR, FILE_BASENAME, PRIMARY_LANG
from src.builder import assemble_html

# ════════════════════════════════════════════════════════════
# CHARGEMENT DES DONNÉES (compatible ancien et nouveau format)
# ════════════════════════════════════════════════════════════

def _load_cv_data() -> dict:
    """
    Charge les données du CV depuis cv_content.py.
    Détecte automatiquement le format utilisé.
    """

    # ── Nouveau format : variables séparées ──────────────────
    if hasattr(_mod, "PERSONAL"):
        return {
            "personal"    : _mod.PERSONAL,
            "summary"     : getattr(_mod, "SUMMARY",      ""),
            "experience"  : getattr(_mod, "EXPERIENCE",   []),
            "education"   : getattr(_mod, "EDUCATION",    []),
            "skills"      : _normalize_skills(getattr(_mod, "SKILLS", [])),
            "languages"   : getattr(_mod, "LANGUAGES",    []),
            "associations": getattr(_mod, "ASSOCIATIONS", []),
            "interests"   : getattr(_mod, "INTERESTS",    []),
        }

    # ── Ancien format : dictionnaire unique CV = {...} ────────
    if hasattr(_mod, "CV"):
        cv = dict(_mod.CV)
        cv["skills"] = _normalize_skills(cv.get("skills", {}))
        return cv

    # ── Ni l'un ni l'autre → erreur claire ───────────────────
    raise ImportError(
        "\n\n❌  cv_content.py introuvable ou mal formé.\n"
        "    Le fichier doit contenir soit :\n"
        "      • Des variables séparées : PERSONAL = {...}, EXPERIENCE = [...], ...\n"
        "      • Un dictionnaire unique : CV = {'personal': {...}, ...}\n"
    )

def _normalize_skills(skills) -> list:
    """
    Normalise le format des compétences.

    Ancien format (dict)  : {"Data & BI": ["SQL", "Python"], ...}
    Nouveau format (list) : [{"category": "Data & BI", "items": ["SQL", ...]}, ...]
    """
    if isinstance(skills, list):
        return skills                           # déjà au bon format

    if isinstance(skills, dict):
        return [
            {"category": cat, "items": items}
            for cat, items in skills.items()
        ]

    return []

# Charge une seule fois au démarrage
CV = _load_cv_data()

# ════════════════════════════════════════════════════════════
# HELPERS
# ════════════════════════════════════════════════════════════

def _ensure_output_dir() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def _filepath(lang: str, ext: str) -> str:
    """EN → index.html pour GitHub Pages, autres → {basename}_{lang}.{ext}"""
    if ext == "html" and lang == PRIMARY_LANG:
        return os.path.join(OUTPUT_DIR, "index.html")
    return os.path.join(OUTPUT_DIR, f"{FILE_BASENAME}_{lang}.{ext}")

def _pdf_exists(path: str) -> bool:
    return os.path.exists(path) and os.path.getsize(path) > 0

# ════════════════════════════════════════════════════════════
# BACKENDS PDF (tentés dans l'ordre)
# ════════════════════════════════════════════════════════════

def _try_playwright(html: str, pdf_path: str) -> bool:
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page    = browser.new_page()
            page.set_content(html, wait_until="domcontentloaded")
            page.pdf(
                path=pdf_path,
                format="A4",
                print_background=True,
                margin={"top": "10mm", "bottom": "10mm",
                        "left": "12mm", "right": "12mm"},
            )
            browser.close()
        print(f"  ✅  PDF   →  {pdf_path}  (Playwright)")
        return True
    except ImportError:
        print("  ℹ   Playwright non installé → essai suivant…")
        return False
    except Exception as e:
        print(f"  ⚠   Playwright : {e} → essai suivant…")
        return False

def _try_browser_headless(html_path: str, pdf_path: str) -> bool:
    candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        "google-chrome", "chromium-browser", "chromium",
    ]
    browser_exe = next(
        (c for c in candidates
         if (os.path.isabs(c) and os.path.exists(c)) or shutil.which(c)),
        None,
    )
    if not browser_exe:
        print("  ℹ   Chrome / Edge non trouvé → essai suivant…")
        return False

    name = "Edge" if "msedge" in browser_exe.lower() else "Chrome"
    try:
        uri = "file:///" + os.path.abspath(html_path).replace(os.sep, "/")
        subprocess.run(
            [browser_exe, "--headless=new", "--disable-gpu", "--no-sandbox",
             "--print-to-pdf-no-header", f"--print-to-pdf={os.path.abspath(pdf_path)}", uri],
            capture_output=True, timeout=30, check=False,
        )
        if _pdf_exists(pdf_path):
            print(f"  ✅  PDF   →  {pdf_path}  ({name} headless)")
            return True
        print(f"  ⚠   {name} : PDF vide → essai suivant…")
        return False
    except Exception as e:
        print(f"  ⚠   {name} : {e} → essai suivant…")
        return False

def _try_xhtml2pdf(html: str, pdf_path: str) -> bool:
    try:
        from xhtml2pdf import pisa
        with open(pdf_path, "wb") as f:
            result = pisa.CreatePDF(html.encode("utf-8"), dest=f, encoding="utf-8")
        if not result.err and _pdf_exists(pdf_path):
            print(f"  ✅  PDF   →  {pdf_path}  (xhtml2pdf — rendu simplifié)")
            return True
        return False
    except ImportError:
        print("  ℹ   xhtml2pdf non installé → essai suivant…")
        return False
    except Exception as e:
        print(f"  ⚠   xhtml2pdf : {e} → essai suivant…")
        return False

def _fallback_manual(html_path: str) -> None:
    print(f"\n  ❌  PDF non généré automatiquement.")
    print(f"  💡  Conversion manuelle :")
    print(f"      1. Ouvre  {os.path.abspath(html_path)}  dans Chrome/Edge")
    print(f"      2. Ctrl+P  →  Enregistrer en PDF")
    print(f"         ✓ Activer : Imprimer les arrière-plans")

# ════════════════════════════════════════════════════════════
# API PUBLIQUE
# ════════════════════════════════════════════════════════════

def export_html(lang: str) -> None:
    _ensure_output_dir()
    path = _filepath(lang, "html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(assemble_html(CV, lang))
    print(f"  ✅  HTML  →  {path}")

def export_pdf(lang: str) -> None:
    _ensure_output_dir()
    pdf_path  = _filepath(lang, "pdf")
    html_path = _filepath(lang, "html")
    html      = assemble_html(CV, lang)

    backends = [
        lambda: _try_playwright      (html,      pdf_path),
        lambda: _try_browser_headless(html_path, pdf_path),
        lambda: _try_xhtml2pdf       (html,      pdf_path),
    ]

    for backend in backends:
        if backend():
            return

    _fallback_manual(html_path)

def export_all(langs: list) -> None:
    print(f"\n📋  Format détecté : {'nouveau (variables séparées)' if hasattr(_mod, 'PERSONAL') else 'ancien (CV = {...})'}")
    for lang in langs:
        print(f"\n🌐  [{lang.upper()}]")
        export_html(lang)
        export_pdf(lang)
    print(f"\n✨  Terminé — fichiers dans /{OUTPUT_DIR}/\n")