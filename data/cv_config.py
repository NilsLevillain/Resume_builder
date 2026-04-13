"""
⚙  Configuration design & export.
"""

# ── Export & GitHub Pages ─────────────────────────────────────
OUTPUT_DIR    = "docs"
FILE_BASENAME = "cv_nils_levillain"
PRIMARY_LANG  = "en"

# ── Couleurs principales ──────────────────────────────────────
ACCENT_COLOR  = "#2563eb"
SIDEBAR_COLOR = "#1e3a5f"

# ── Typographie ──────────────────────────────────────────────
FONT_FAMILY    = "Arial, Helvetica, sans-serif"
FONT_SIZE_BASE = "10.5pt"

# ── KPI Badge — palette facilement modifiable ─────────────────
# Thème actif : bleu
KPI_BG     = "#dbeafe"   # fond
KPI_TEXT   = "#1e40af"   # texte
KPI_BORDER = "#93c5fd"   # bordure

# Autres thèmes disponibles — décommenter pour changer :
#
# Vert émeraude :
# KPI_BG = "#d1fae5" ; KPI_TEXT = "#065f46" ; KPI_BORDER = "#6ee7b7"
#
# Violet :
# KPI_BG = "#ede9fe" ; KPI_TEXT = "#5b21b6" ; KPI_BORDER = "#c4b5fd"
#
# Teal :
# KPI_BG = "#ccfbf1" ; KPI_TEXT = "#0f766e" ; KPI_BORDER = "#5eead4"
#
# Ambre (ancien défaut) :
# KPI_BG = "#fffbeb" ; KPI_TEXT = "#b45309" ; KPI_BORDER = "#fde68a"

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