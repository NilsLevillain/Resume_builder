"""
⚙  Configuration design & export.
"""

# ── Export & GitHub Pages ─────────────────────────────────────
OUTPUT_DIR   = "docs"               # GitHub Pages sert /docs
FILE_BASENAME = "cv_nils_levillain"
PRIMARY_LANG  = "en"                # → docs/index.html  (les autres → docs/{lang}.html)

# ── Palette principale (les autres couleurs sont dans styles.py) ──
ACCENT_COLOR  = "#2563eb"           # Bleu — changer ici suffit
SIDEBAR_COLOR = "#1e3a5f"           # Bleu marine sidebar

# ── Typographie ──────────────────────────────────────────────
FONT_FAMILY   = "Arial, Helvetica, sans-serif"
FONT_SIZE_BASE = "10.5pt"

# ── Sections actives ─────────────────────────────────────────
SECTIONS = {
    "summary"      : True,
    "experience"   : True,
    "education"    : True,
    "skills"       : True,
    "languages"    : True,
    "associations" : True,
    "interests"    : True,
}

# ── Labels traduits ──────────────────────────────────────────
SECTION_LABELS = {
    "summary"      : {"fr": "Profil",                       "en": "Profile"},
    "experience"   : {"fr": "Expériences Professionnelles", "en": "Work Experience"},
    "education"    : {"fr": "Formation",                    "en": "Education"},
    "skills"       : {"fr": "Compétences",                  "en": "Skills"},
    "languages"    : {"fr": "Langues",                      "en": "Languages"},
    "associations" : {"fr": "Vie Associative",              "en": "Leadership"},
    "interests"    : {"fr": "Intérêts",                     "en": "Interests"},
}