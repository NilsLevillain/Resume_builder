"""
🎨  Design system — Modern CV
     Light / Dark mode · 2 colonnes · Cards · Tags · KPI badges
"""
from data.cv_config import ACCENT_COLOR, SIDEBAR_COLOR, FONT_FAMILY, FONT_SIZE_BASE

# ── JavaScript : toggle thème ─────────────────────────────────
THEME_JS = """
(function () {
    const saved       = localStorage.getItem('cv-theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const theme       = saved || (prefersDark ? 'dark' : 'light');
    document.documentElement.setAttribute('data-theme', theme);
})();

function toggleTheme() {
    const html  = document.documentElement;
    const next  = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', next);
    localStorage.setItem('cv-theme', next);
    const btn = document.querySelector('.theme-toggle');
    if (btn) {
        btn.textContent = next === 'dark' ? '☀' : '🌙';
        btn.title       = next === 'dark' ? 'Light mode' : 'Dark mode';
    }
}

document.addEventListener('DOMContentLoaded', function () {
    const theme = document.documentElement.getAttribute('data-theme') || 'light';
    const btn   = document.querySelector('.theme-toggle');
    if (btn) {
        btn.textContent = theme === 'dark' ? '☀' : '🌙';
        btn.title       = theme === 'dark' ? 'Light mode' : 'Dark mode';
    }
});
"""

def get_styles() -> str:
    return f"""

/* ══════════════════════════════════════════════════════
   DESIGN TOKENS
══════════════════════════════════════════════════════ */

:root {{
    /* ── Accent ── */
    --accent          : {ACCENT_COLOR};
    --accent-light    : #eff6ff;

    /* ── Page ── */
    --page-bg         : #eef2f7;
    --shadow-page     : 0 4px 40px rgba(0,0,0,0.10);

    /* ── Header ── */
    --header-bg       : #ffffff;
    --name-color      : {SIDEBAR_COLOR};
    --tagline-color   : #475569;
    --contact-color   : #64748b;

    /* ── Sidebar ── */
    --sidebar-bg      : {SIDEBAR_COLOR};
    --sidebar-text    : #e2e8f0;
    --sidebar-muted   : #94a3b8;
    --sidebar-border  : rgba(255,255,255,0.12);
    --sidebar-h2      : #93c5fd;
    --sidebar-tag-bg  : rgba(255,255,255,0.10);
    --sidebar-tag-bd  : rgba(255,255,255,0.20);

    /* ── Main area ── */
    --main-bg         : #ffffff;
    --card-bg         : #f8fafc;
    --card-border     : #e2e8f0;
    --card-shadow     : 0 1px 3px rgba(0,0,0,0.05), 0 4px 14px rgba(0,0,0,0.07);
    --text            : #1e293b;
    --text-muted      : #64748b;
    --section-border  : {ACCENT_COLOR};

    /* ── Tags (main) ── */
    --tag-bg          : #eff6ff;
    --tag-text        : #1d4ed8;
    --tag-border      : #bfdbfe;

    /* ── KPI badges ── */
    --kpi-bg          : #fffbeb;
    --kpi-text        : #b45309;
    --kpi-border      : #fde68a;

    /* ── Misc ── */
    --radius-card     : 8px;
    --radius-tag      : 100px;
    --font            : {FONT_FAMILY};
    --size-base       : {FONT_SIZE_BASE};
}}

[data-theme="dark"] {{
    --accent          : #60a5fa;
    --accent-light    : #1e3a5f;

    --page-bg         : #0f172a;
    --shadow-page     : 0 4px 40px rgba(0,0,0,0.50);

    --header-bg       : #1e293b;
    --name-color      : #93c5fd;
    --tagline-color   : #94a3b8;
    --contact-color   : #64748b;

    --sidebar-bg      : #0d1b30;
    --sidebar-text    : #cbd5e1;
    --sidebar-muted   : #64748b;
    --sidebar-border  : rgba(255,255,255,0.07);
    --sidebar-h2      : #60a5fa;
    --sidebar-tag-bg  : rgba(255,255,255,0.06);
    --sidebar-tag-bd  : rgba(255,255,255,0.12);

    --main-bg         : #1e293b;
    --card-bg         : #263548;
    --card-border     : #334155;
    --card-shadow     : 0 1px 3px rgba(0,0,0,0.25), 0 4px 14px rgba(0,0,0,0.35);
    --text            : #e2e8f0;
    --text-muted      : #94a3b8;
    --section-border  : #60a5fa;

    --tag-bg          : #1e3a5f;
    --tag-text        : #93c5fd;
    --tag-border      : #2563eb;

    --kpi-bg          : #422006;
    --kpi-text        : #fbbf24;
    --kpi-border      : #78350f;
}}

/* ══════════════════════════════════════════════════════
   BASE
══════════════════════════════════════════════════════ */

*, *::before, *::after {{ margin: 0; padding: 0; box-sizing: border-box; }}

body {{
    background  : var(--page-bg);
    font-family : var(--font);
    font-size   : var(--size-base);
    color       : var(--text);
    line-height : 1.5;
    transition  : background 0.2s, color 0.2s;
}}

/* ══════════════════════════════════════════════════════
   THEME TOGGLE BUTTON
══════════════════════════════════════════════════════ */

.theme-toggle {{
    position    : absolute;
    top         : 16px;
    right       : 20px;
    background  : var(--card-bg);
    border      : 1px solid var(--card-border);
    border-radius: var(--radius-tag);
    padding     : 4px 12px;
    font-size   : 14px;
    cursor      : pointer;
    box-shadow  : var(--card-shadow);
    transition  : all 0.2s;
    z-index     : 10;
    line-height : 1.4;
}}
.theme-toggle:hover {{ box-shadow: 0 4px 16px rgba(0,0,0,0.15); }}

/* ══════════════════════════════════════════════════════
   PAGE WRAPPER
══════════════════════════════════════════════════════ */

.cv-page {{
    max-width     : 920px;
    margin        : 24px auto;
    border-radius : 12px;
    overflow      : hidden;
    box-shadow    : var(--shadow-page);
}}

/* ══════════════════════════════════════════════════════
   HEADER
══════════════════════════════════════════════════════ */

.cv-header {{
    background  : var(--header-bg);
    padding     : 28px 36px 24px;
    position    : relative;
    border-bottom: 3px solid var(--accent);
    transition  : background 0.2s;
}}

.cv-name {{
    font-size      : 26pt;
    font-weight    : bold;
    letter-spacing : 3px;
    text-transform : uppercase;
    color          : var(--name-color);
    line-height    : 1.1;
    margin-bottom  : 6px;
}}

.cv-tagline {{
    font-size   : 11pt;
    color       : var(--accent);
    font-weight : 600;
    margin-bottom: 10px;
}}

.cv-contact {{
    font-size   : 9.5pt;
    color       : var(--contact-color);
    display     : flex;
    flex-wrap   : wrap;
    gap         : 4px 20px;
}}

.cv-contact-item {{
    display     : flex;
    align-items : center;
    gap         : 4px;
}}

.cv-contact-icon {{
    font-size   : 10pt;
    opacity     : 0.7;
}}

/* ══════════════════════════════════════════════════════
   DEUX COLONNES
══════════════════════════════════════════════════════ */

.cv-body {{
    display         : flex;
    min-height      : 700px;
    align-items     : stretch;
}}

/* ── Sidebar ── */
.cv-sidebar {{
    width       : 265px;
    flex-shrink : 0;
    background  : var(--sidebar-bg);
    color       : var(--sidebar-text);
    padding     : 24px 20px 32px;
    order       : -1;           /* visuellement à gauche */
    transition  : background 0.2s;
}}

/* ── Main ── */
.cv-main {{
    flex        : 1;
    background  : var(--main-bg);
    padding     : 24px 28px 32px;
    order       : 1;            /* visuellement à droite */
    transition  : background 0.2s;
}}

/* ══════════════════════════════════════════════════════
   TITRES DE SECTION
══════════════════════════════════════════════════════ */

.section-title {{
    font-size      : 8.5pt;
    font-weight    : bold;
    text-transform : uppercase;
    letter-spacing : 2px;
    margin-top     : 22px;
    margin-bottom  : 12px;
    padding-bottom : 6px;
}}

/* Main : accent + bordure */
.cv-main .section-title {{
    color        : var(--accent);
    border-bottom: 1.5px solid var(--section-border);
}}

/* Sidebar : couleur claire sur fond foncé */
.cv-sidebar .section-title {{
    color        : var(--sidebar-h2);
    border-bottom: 1px solid var(--sidebar-border);
    margin-top   : 24px;
}}

.cv-sidebar .section-title:first-child {{ margin-top: 0; }}

/* ══════════════════════════════════════════════════════
   CARTES EXPÉRIENCE / FORMATION
══════════════════════════════════════════════════════ */

.entry-card {{
    background    : var(--card-bg);
    border        : 1px solid var(--card-border);
    border-left   : 3px solid var(--accent);
    border-radius : var(--radius-card);
    padding       : 12px 14px;
    margin-bottom : 10px;
    box-shadow    : var(--card-shadow);
    transition    : background 0.2s, box-shadow 0.2s;
}}

.entry-header {{
    display         : flex;
    justify-content : space-between;
    align-items     : flex-start;
    gap             : 10px;
    margin-bottom   : 4px;
}}

.entry-left  {{ flex: 1; min-width: 0; }}

.entry-title {{
    font-weight : bold;
    font-size   : 10.5pt;
    color       : var(--text);
    line-height : 1.3;
}}

.entry-sub {{
    font-size  : 9.5pt;
    color      : var(--text-muted);
    font-style : italic;
    margin-top : 2px;
}}

.entry-date {{
    font-size   : 9pt;
    color       : var(--text-muted);
    white-space : nowrap;
    text-align  : right;
    flex-shrink : 0;
    padding-top : 1px;
    background  : var(--accent-light);
    border-radius: var(--radius-tag);
    padding     : 2px 8px;
    height      : fit-content;
    font-weight : 500;
}}

.entry ul {{
    margin-left : 16px;
    margin-top  : 7px;
}}

.entry ul li {{
    font-size     : 10pt;
    margin-bottom : 3px;
    line-height   : 1.45;
    color         : var(--text);
}}

/* ══════════════════════════════════════════════════════
   KPI BADGES
══════════════════════════════════════════════════════ */

.kpi-badge {{
    display       : inline-block;
    background    : var(--kpi-bg);
    color         : var(--kpi-text);
    border        : 1px solid var(--kpi-border);
    border-radius : 4px;
    padding       : 0px 6px;
    font-weight   : bold;
    font-size     : 9pt;
    white-space   : nowrap;
    vertical-align: middle;
}}

/* ══════════════════════════════════════════════════════
   TAGS (sidebar + main)
══════════════════════════════════════════════════════ */

/* Tags sidebar */
.cv-sidebar .tags {{ display: flex; flex-wrap: wrap; gap: 4px; margin-top: 4px; }}
.cv-sidebar .tag {{
    display       : inline-block;
    background    : var(--sidebar-tag-bg);
    color         : var(--sidebar-text);
    border        : 1px solid var(--sidebar-tag-bd);
    border-radius : var(--radius-tag);
    padding       : 2px 10px;
    font-size     : 8.5pt;
    line-height   : 1.5;
}}

/* Tags main area (formation, etc.) */
.cv-main .tags {{ display: flex; flex-wrap: wrap; gap: 4px; margin-top: 6px; }}
.cv-main .tag {{
    display       : inline-block;
    background    : var(--tag-bg);
    color         : var(--tag-text);
    border        : 1px solid var(--tag-border);
    border-radius : var(--radius-tag);
    padding       : 2px 10px;
    font-size     : 8.5pt;
    line-height   : 1.5;
    font-weight   : 500;
}}

/* ══════════════════════════════════════════════════════
   COMPÉTENCES (sidebar)
══════════════════════════════════════════════════════ */

.skill-category {{
    font-size   : 9pt;
    font-weight : bold;
    color       : var(--sidebar-muted);
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-top  : 12px;
    margin-bottom: 5px;
}}

.skill-category:first-of-type {{ margin-top: 0; }}

/* ══════════════════════════════════════════════════════
   LANGUES (sidebar)
══════════════════════════════════════════════════════ */

.lang-item      {{ margin-bottom: 8px; }}
.lang-name      {{ font-weight: bold; font-size: 10pt; }}
.lang-level     {{ font-size: 9pt; color: var(--sidebar-muted); }}

.lang-dots      {{ display: flex; gap: 4px; margin-top: 3px; }}
.lang-dot {{
    width         : 10px;
    height        : 10px;
    border-radius : 50%;
    background    : var(--sidebar-tag-bd);
}}
.lang-dot.filled {{ background: var(--sidebar-h2); }}

/* ══════════════════════════════════════════════════════
   ASSOCIATIONS (sidebar)
══════════════════════════════════════════════════════ */

.assoc-entry    {{ margin-bottom: 10px; }}
.assoc-role     {{ font-weight: bold; font-size: 10pt; }}
.assoc-org      {{ font-size: 9pt; color: var(--sidebar-muted); font-style: italic; }}
.assoc-desc     {{ font-size: 9pt; margin-top: 2px; line-height: 1.4; }}

/* ══════════════════════════════════════════════════════
   INTÉRÊTS (sidebar)
══════════════════════════════════════════════════════ */

.interest-item {{
    font-size     : 9.5pt;
    margin-bottom : 5px;
    display       : flex;
    align-items   : flex-start;
    gap           : 6px;
}}

.interest-item::before {{
    content    : "◆";
    color      : var(--sidebar-h2);
    font-size  : 7pt;
    margin-top : 3px;
    flex-shrink: 0;
}}

/* ══════════════════════════════════════════════════════
   RÉSUMÉ (main)
══════════════════════════════════════════════════════ */

.cv-summary {{
    background    : var(--accent-light);
    border-left   : 3px solid var(--accent);
    border-radius : 0 var(--radius-card) var(--radius-card) 0;
    padding       : 10px 14px;
    font-size     : 10pt;
    line-height   : 1.6;
    margin-bottom : 4px;
    color         : var(--text);
}}

/* ══════════════════════════════════════════════════════
   IMPRESSION / PDF
══════════════════════════════════════════════════════ */

@page {{ margin: 10mm 12mm; }}

@media print {{
    /* Masquer éléments web uniquement */
    .theme-toggle {{ display: none !important; }}

    /* Fond du CV plein page */
    body, .cv-page {{ background: white; box-shadow: none; border-radius: 0; margin: 0; }}

    /* Conserver les couleurs de fond sidebar */
    .cv-sidebar {{
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }}

    /* Éviter les coupures dans les cartes */
    .entry-card {{ page-break-inside: avoid; }}
    .section-title {{ page-break-after: avoid; }}

    /* Taille légèrement réduite à l'impression */
    body {{ font-size: 9.5pt; }}
    .cv-name {{ font-size: 20pt; }}
}}
"""