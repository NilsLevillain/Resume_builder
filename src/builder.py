"""
🏗  Constructeurs HTML — 2 colonnes, cards, KPI, tags, dark mode.
"""
from typing import Any
from data.cv_config import SECTION_LABELS, SECTIONS
from src.styles import get_styles, THEME_JS

# ════════════════════════════════════════════════════════════
# HELPERS
# ════════════════════════════════════════════════════════════

def t(field: Any, lang: str) -> str:
    """Résout un champ bilingue ou retourne la chaîne directement."""
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
    """Génère une ligne de tags depuis une liste de strings."""
    spans = "".join(f'<span class="tag">{item}</span>' for item in items)
    return f'<div class="tags">{spans}</div>'

def _lang_dots(filled: int, total: int = 5) -> str:
    """Génère les points de niveau de langue (●●●○○)."""
    dots = ""
    for i in range(total):
        cls = "lang-dot filled" if i < filled else "lang-dot"
        dots += f'<span class="{cls}"></span>'
    return f'<div class="lang-dots">{dots}</div>'

# ════════════════════════════════════════════════════════════
# HEADER (pleine largeur)
# ════════════════════════════════════════════════════════════

def build_header(personal: dict, lang: str) -> str:
    p = personal

    # Icônes contact
    icons = {"email": "✉", "phone": "☎", "location": "📍", "linkedin": "in"}
    contact_fields = [
        ("email",    icons["email"],    p.get("email",    "")),
        ("phone",    icons["phone"],    p.get("phone",    "")),
        ("location", icons["location"], p.get("location", "")),
        ("linkedin", icons["linkedin"], p.get("linkedin", "")),
    ]
    contact_html = "".join(
        f'<span class="cv-contact-item">'
        f'<span class="cv-contact-icon">{icon}</span>{value}'
        f'</span>'
        for _, icon, value in contact_fields if value
    )

    return (
        f'<header class="cv-header">\n'
        f'  <button class="theme-toggle no-print" '
        f'    onclick="toggleTheme()" title="Dark mode">🌙</button>\n'
        f'  <div class="cv-name">{p["name"]}</div>\n'
        f'  <div class="cv-tagline">{t(p.get("title", ""), lang)}</div>\n'
        f'  <div class="cv-contact">{contact_html}</div>\n'
        f'</header>\n'
    )

# ════════════════════════════════════════════════════════════
# CONTENU PRINCIPAL (colonne droite, premier dans le HTML pour ATS)
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
    for job in experience:
        date_str    = f"{t(job['start'], lang)} – {t(job['end'], lang)}"
        company_str = job["company"]
        if job.get("type"):
            company_str += f" · {t(job['type'], lang)}"
        if job.get("location"):
            company_str += f" · {t(job['location'], lang)}"

        cards.append(
            f'  <div class="entry-card entry">\n'
            f'    <div class="entry-header">\n'
            f'      <div class="entry-left">\n'
            f'        <div class="entry-title">{t(job["title"], lang)}</div>\n'
            f'        <div class="entry-sub">{company_str}</div>\n'
            f'      </div>\n'
            f'      <div class="entry-date">{date_str}</div>\n'
            f'    </div>\n'
            f'{_bullets(job.get("bullets", []), lang)}'
            f'  </div>\n'
        )

    return (
        f'<section>\n'
        f'  <div class="section-title">{_label("experience", lang)}</div>\n'
        + "".join(cards)
        + f'</section>\n'
    )

def build_education(education: list, lang: str) -> str:
    if not _is_on("education"):
        return ""

    cards = []
    for edu in education:
        date_str   = f"{edu['start']} – {edu['end']}"
        school_str = edu["school"]
        if edu.get("location"):
            school_str += f" · {edu['location']}"

        # Bullets OU tags selon le contenu
        content = _bullets(edu.get("bullets", []), lang)

        cards.append(
            f'  <div class="entry-card entry">\n'
            f'    <div class="entry-header">\n'
            f'      <div class="entry-left">\n'
            f'        <div class="entry-title">{t(edu["degree"], lang)}</div>\n'
            f'        <div class="entry-sub">{school_str}</div>\n'
            f'      </div>\n'
            f'      <div class="entry-date">{date_str}</div>\n'
            f'    </div>\n'
            f'{content}'
            f'  </div>\n'
        )

    return (
        f'<section>\n'
        f'  <div class="section-title">{_label("education", lang)}</div>\n'
        + "".join(cards)
        + f'</section>\n'
    )

# ════════════════════════════════════════════════════════════
# SIDEBAR (colonne gauche, second dans le HTML)
# ════════════════════════════════════════════════════════════

def build_skills(skills: list, lang: str) -> str:
    if not _is_on("skills"):
        return ""

    rows = []
    for row in skills:
        cat   = t(row["category"], lang)
        items = row["items"]
        rows.append(
            f'  <div class="skill-category">{cat}</div>\n'
            f'  {_tags(items)}\n'
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

    # Mapping niveau → nombre de points
    level_dots = {"native": 5, "c2": 5, "c1": 4, "b2": 3, "b1": 3, "a2": 2, "a1": 1}

    rows = []
    for item in languages:
        level_text = t(item["level"], lang)
        # Détecte le niveau pour les points (cherche c2, b1, etc. dans le texte)
        dots_count = next(
            (v for k, v in level_dots.items() if k in level_text.lower()),
            None,
        )
        dots_html  = _lang_dots(dots_count) if dots_count is not None else ""

        rows.append(
            f'  <div class="lang-item">\n'
            f'    <div class="lang-name">{item["lang"]}</div>\n'
            f'    {dots_html}\n'
            f'    <div class="lang-level">{level_text}</div>\n'
            f'  </div>\n'
        )

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
            f'    <div class="assoc-org">'
            f'{t(a.get("org", ""), lang)} · {a.get("period", "")}'
            f'</div>\n'
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
    """Contenu principal — lu EN PREMIER par les ATS."""
    return (
        build_summary    (cv["summary"],    lang) +
        build_experience (cv["experience"], lang) +
        build_education  (cv["education"],  lang)
    )

def _build_sidebar(cv: dict, lang: str) -> str:
    """Sidebar — lu en second par les ATS (compétences, langues…)."""
    return (
        build_skills      (cv["skills"],                lang) +
        build_languages   (cv["languages"],             lang) +
        build_associations(cv.get("associations", []),  lang) +
        build_interests   (cv.get("interests", []),     lang)
    )

def assemble_html(cv: dict, lang: str) -> str:
    """Assemble le document HTML complet."""
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

    <!-- ══ MAIN — premier dans le HTML pour les ATS ══ -->
    <main class="cv-main">
{_build_main(cv, lang)}
    </main>

    <!-- ══ SIDEBAR — second dans le HTML, visuellement à gauche via CSS ══ -->
    <aside class="cv-sidebar">
{_build_sidebar(cv, lang)}
    </aside>

  </div><!-- .cv-body -->

</div><!-- .cv-page -->

</body>
</html>"""