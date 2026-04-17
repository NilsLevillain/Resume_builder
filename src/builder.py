"""
🏗  Constructeurs HTML — 2 colonnes, cards, KPI, tags, dark mode.
"""
import base64
import os
from typing import Any

from data.cv_config import SECTION_LABELS, SECTIONS
from src.styles    import get_styles, THEME_JS

# ════════════════════════════════════════════════════════════
# SVG ICONS — Bootstrap Icons, currentColor, 13×13
# ════════════════════════════════════════════════════════════

_ICON_EMAIL = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" class="cv-icon">'
    '<path d="M.05 3.555A2 2 0 0 1 2 2h12a2 2 0 0 1 1.95 1.555L8 8.414.05 3.555Z"/>'
    '<path d="M0 4.697v7.104l5.803-3.558L0 4.697ZM6.761 8.83l-6.57 4.026A2 2 0 0 0 2 '
    '14h12a2 2 0 0 0 1.808-1.144l-6.57-4.027L8 9.586l-1.239-.757Zm3.436-.586L16 '
    '11.801V4.697l-5.803 3.546Z"/></svg>'
)

_ICON_PHONE = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" class="cv-icon">'
    '<path d="M3.654 1.328a.678.678 0 0 0-1.015-.063L1.605 2.3c-.483.484-.661 1.169-.45 '
    '1.77a17.568 17.568 0 0 0 4.168 6.608 17.569 17.569 0 0 0 6.608 4.168c.601.211 '
    '1.286.033 1.77-.45l1.034-1.034a.678.678 0 0 0-.063-1.015l-2.307-1.794a.678.678 0 '
    '0 0-.58-.122l-2.19.547a1.745 1.745 0 0 1-1.657-.459L5.482 8.062a1.745 1.745 0 0 '
    '1-.46-1.657l.548-2.19a.678.678 0 0 0-.122-.58L3.654 1.328ZM1.884.511a1.745 1.745 '
    '0 0 1 2.612.163L6.29 2.98c.329.423.445.974.315 1.494l-.547 2.19a.678.678 0 0 0 '
    '.178.643l2.457 2.457a.678.678 0 0 0 .644.178l2.189-.547a1.745 1.745 0 0 1 '
    '1.494.315l2.306 1.794c.829.645.905 1.87.163 2.611l-1.034 1.034c-.74.74-1.846 '
    '1.065-2.877.702a18.634 18.634 0 0 1-7.01-4.42 18.634 18.634 0 0 1-4.42-7.009c'
    '-.362-1.03-.037-2.137.703-2.877L1.885.511Z"/></svg>'
)

_ICON_LOCATION = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" class="cv-icon">'
    '<path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10Zm0-7a3 3 0 1 1 '
    '0-6 3 3 0 0 1 0 6Z"/></svg>'
)

_ICON_LINKEDIN = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" class="cv-icon">'
    '<path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708'
    'c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854Zm4.943 12.248V'
    '6.169H2.542v7.225Zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248'
    '-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248Zm4.908 '
    '8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216'
    '.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845'
    '.7-2.165 1.193v.025h-.016l.016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225Z"/>'
    '</svg>'
)

_ICON_GITHUB = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" class="cv-icon">'
    '<path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 '
    '0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28'
    '-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28'
    '-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02'
    '.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04'
    ' 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 '
    '3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38'
    'A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>'
)

# ════════════════════════════════════════════════════════════
# HELPERS
# ════════════════════════════════════════════════════════════

def t(field: Any, lang: str) -> str:
    if field is None:
        return ""
    if isinstance(field, dict):
        return field.get(lang, field.get("fr", ""))
    return str(field)

def _label(key: str, lang: str) -> str:
    labels = SECTION_LABELS.get(key, {})
    return labels.get(lang, labels.get("fr", key.upper()))

def _is_on(key: str) -> bool:
    return SECTIONS.get(key, True)

def _bullets(items: list, lang: str) -> str:
    if not items:
        return ""
    lis = "\n".join(f'      <li>{t(item, lang)}</li>' for item in items)
    return f"    <ul>\n{lis}\n    </ul>\n"

def _tags(items: list) -> str:
    spans = "".join(f'<span class="tag">{item}</span>' for item in items)
    return f'<div class="tags">{spans}</div>'


def _photo_data_uri(personal: dict) -> str:
    """Retourne le data URI de la photo.
    Priorité 1 : base64 embarqué dans cv_content.py (photo_b64) — 100% fiable.
    Priorité 2 : lecture depuis un fichier (photo) — dépend du système de fichiers.
    """
    # Priorité 1 — base64 directement dans le dict (recommandé)
    b64 = personal.get("photo_b64", "")
    if b64:
        return b64

    # Priorité 2 — chemin fichier relatif à la racine du projet
    path = personal.get("photo", "")
    if not path:
        return ""
    if not os.path.isabs(path):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        abs_path     = os.path.join(project_root, path)
    else:
        abs_path = path

    if not os.path.exists(abs_path):
        print(f"  ⚠ Photo non trouvée : {abs_path}")
        return ""

    with open(abs_path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    ext  = abs_path.rsplit(".", 1)[-1].lower()
    mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp"}.get(ext, "jpeg")
    return f"data:image/{mime};base64,{data}"

def _initials(name: str) -> str:
    parts = name.strip().split()
    return "".join(p[0].upper() for p in parts[:2])

# ════════════════════════════════════════════════════════════
# HEADER
# ════════════════════════════════════════════════════════════

def _short_url(url: str) -> str:
    """Affiche seulement le dernier segment de l'URL (username/handle).
    'linkedin.com/in/nils-levillain' → 'nils-levillain'
    'github.com/nils-levillain'      → 'nils-levillain'
    """
    if not url:
        return ""
    return url.rstrip("/").split("/")[-1]

def build_header(personal: dict, lang: str) -> str:
    p          = personal
    photo_uri = _photo_data_uri(p)   # ← passe maintenant 'p' (le dict entier)
    initials   = _initials(p.get("name", "?"))

    if photo_uri:
        photo_html = f'<img class="cv-photo" src="{photo_uri}" alt="{initials}">'
    else:
        photo_html = f'<div class="cv-photo-placeholder">{initials}</div>'

    def contact_item(icon_svg: str, text: str, href: str = None) -> str:
        if not text:
            return ""
        label = (
            f'<a href="{href}" target="_blank" rel="noopener noreferrer" '
            f'class="cv-contact-link">{text}</a>'
            if href else text
        )
        return (
            f'<span class="cv-contact-item">'
            f'<span class="cv-contact-icon">{icon_svg}</span>'
            f'<span class="cv-contact-text">{label}</span>'
            f'</span>'
        )


    contact_html = "".join(filter(None, [
    contact_item(_ICON_EMAIL,
                 p.get("email", ""),
                 f'mailto:{p.get("email","")}' if p.get("email") else None),
    contact_item(_ICON_PHONE,
                 p.get("phone", ""),
                 None),
    contact_item(_ICON_LOCATION,
                 p.get("location", ""),
                 None),
    contact_item(_ICON_LINKEDIN,
                 _short_url(p.get("linkedin", "")),
                 f'https://{p.get("linkedin","")}' if p.get("linkedin") else None),
    contact_item(_ICON_GITHUB,
                 _short_url(p.get("github", "")),
                 f'https://{p.get("github","")}' if p.get("github") else None),
]))

    return (
        f'<header class="cv-header">\n'
        f'  <div class="cv-header-photo-col">{photo_html}</div>\n'
        f'  <div class="cv-header-info-col">\n'
        f'    <button class="theme-toggle" onclick="toggleTheme()" title="Dark mode">🌙</button>\n'
        f'    <div class="cv-name">{p["name"]}</div>\n'
        f'    <div class="cv-tagline">{t(p.get("title", ""), lang)}</div>\n'
        f'    <div class="cv-contact">{contact_html}</div>\n'
        f'  </div>\n'
        f'</header>\n'
    )

# ════════════════════════════════════════════════════════════
# MAIN CONTENT
# ════════════════════════════════════════════════════════════

def build_summary(summary: Any, lang: str) -> str:
    if not _is_on("summary"):
        return ""
    text = t(summary, lang)
    if not text:
        return ""
    return (
        f'<section>\n'
        f'  <div class="section-title">{_label("summary", lang)}</div>\n'
        f'  <p class="cv-summary">{text}</p>\n'
        f'</section>\n'
    )

def build_experience(experience: list, lang: str) -> str:
    if not _is_on("experience"):
        return ""
    cards = []
    for i, job in enumerate(experience):
        date_str   = f"{t(job['start'], lang)} – {t(job['end'], lang)}"
        company    = job.get("company", "")
        title      = t(job["title"], lang)
        full_title = f"{company}&nbsp;&nbsp;|&nbsp;&nbsp;{title}" if company else title
        cards.append(
            f'  <div class="entry-card entry entry-card--{i}">\n'
            f'    <div class="entry-header">\n'
            f'      <div class="entry-left">\n'
            f'        <div class="entry-title">{full_title}</div>\n'
            f'      </div>\n'
            f'      <div class="entry-date">{date_str}</div>\n'
            f'    </div>\n'
            f'{_bullets(job.get("bullets", []), lang)}'
            f'  </div>\n'
        )
    return (
        f'<section class="section-experience">\n'
        f'  <div class="section-title">{_label("experience", lang)}</div>\n'
        + "".join(cards)
        + f'</section>\n'
    )

def build_education(education: list, lang: str) -> str:
    if not _is_on("education"):
        return ""
    cards = []
    for edu in education:
        date_str = f"{edu['start']} – {edu['end']}"
        cards.append(
            f'  <div class="entry-card entry">\n'
            f'    <div class="entry-header">\n'
            f'      <div class="entry-left">\n'
            f'        <div class="entry-title">{edu["school"]}</div>\n'
            f'        <div class="entry-sub">{t(edu["degree"], lang)}</div>\n'
            f'      </div>\n'
            f'      <div class="entry-date">{date_str}</div>\n'
            f'    </div>\n'
            f'{_bullets(edu.get("bullets", []), lang)}'
            f'  </div>\n'
        )
    return (
        f'<section>\n'
        f'  <div class="section-title">{_label("education", lang)}</div>\n'
        + "".join(cards)
        + f'</section>\n'
    )

# ════════════════════════════════════════════════════════════
# SIDEBAR
# ════════════════════════════════════════════════════════════

def build_skills(skills: list, lang: str) -> str:
    if not _is_on("skills"):
        return ""
    rows = []
    for row in skills:
        rows.append(
            f'  <div class="skill-category">{t(row["category"], lang)}</div>\n'
            f'  {_tags(row["items"])}\n'
        )
    return (
        f'<section>\n'
        f'  <div class="section-title">{_label("skills", lang)}</div>\n'
        + "".join(rows)
        + f'</section>\n'
    )

def build_languages(languages: list, lang: str) -> str:
    if not _is_on("languages"):
        return ""
    rows = [
        f'  <div class="lang-item">\n'
        f'    <div class="lang-name">{item["lang"]}</div>\n'
        f'    <div class="lang-level">{t(item["level"], lang)}</div>\n'
        f'  </div>\n'
        for item in languages
    ]
    return (
        f'<section>\n'
        f'  <div class="section-title">{_label("languages", lang)}</div>\n'
        + "".join(rows)
        + f'</section>\n'
    )

def build_associations(associations: list, lang: str) -> str:
    if not associations or not _is_on("associations"):
        return ""
    rows = []
    for a in associations:
        rows.append(
            f'  <div class="assoc-entry">\n'
            f'    <div class="assoc-role">{t(a["role"], lang)}</div>\n'
            f'    <div class="assoc-org">{t(a.get("org",""), lang)} · {a.get("period","")}</div>\n'
            f'    <div class="assoc-desc">{t(a["description"], lang)}</div>\n'
            f'  </div>\n'
        )
    return (
        f'<section>\n'
        f'  <div class="section-title">{_label("associations", lang)}</div>\n'
        + "".join(rows)
        + f'</section>\n'
    )

def build_interests(interests: list, lang: str) -> str:
    if not interests or not _is_on("interests"):
        return ""
    items = "".join(
        f'  <div class="interest-item">{t(item, lang)}</div>\n'
        for item in interests
    )
    return (
        f'<section>\n'
        f'  <div class="section-title">{_label("interests", lang)}</div>\n'
        + items
        + f'</section>\n'
    )

# ════════════════════════════════════════════════════════════
# ASSEMBLAGE
# ════════════════════════════════════════════════════════════

def _build_main(cv: dict, lang: str) -> str:
    return (
        build_summary   (cv["summary"],    lang) +
        build_experience(cv["experience"], lang) +
        build_education (cv["education"],  lang)
    )

def _build_sidebar(cv: dict, lang: str) -> str:
    return (
        build_skills      (cv["skills"],               lang) +
        build_languages   (cv["languages"],            lang) +
        build_associations(cv.get("associations", []), lang) +
        build_interests   (cv.get("interests", []),    lang)
    )

def assemble_html(cv: dict, lang: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="{lang}" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CV – {cv["personal"]["name"]} ({lang.upper()})</title>
  <script>{THEME_JS}</script>
  <style>
{get_styles()}
  </style>
</head>
<body>
<div class="cv-page">
  {build_header(cv["personal"], lang)}
  <div class="cv-body">
    <main class="cv-main">
{_build_main(cv, lang)}
    </main>
    <aside class="cv-sidebar">
{_build_sidebar(cv, lang)}
    </aside>
  </div>
</div>
</body>
</html>"""