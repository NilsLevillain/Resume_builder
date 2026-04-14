"""
🎨  Design system — Modern CV
     Light / Dark mode · 2 colonnes · Cards · Tags · KPI badges
"""
from data.cv_config import (
    ACCENT_COLOR, SIDEBAR_COLOR, FONT_FAMILY, FONT_SIZE_BASE, KPI_BG, KPI_TEXT, KPI_BORDER,
)
# ── JavaScript : toggle thème + particules ────────────────────
THEME_JS = """
(function () {
    const saved       = localStorage.getItem('cv-theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const theme       = saved || (prefersDark ? 'dark' : 'light');
    document.documentElement.setAttribute('data-theme', theme);
})();

function toggleTheme() {
    const html = document.documentElement;
    const next = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
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

function initParticles() {
    if (document.getElementById('cv-particles')) return;

    const canvas  = document.createElement('canvas');
    canvas.id     = 'cv-particles';
    canvas.style.cssText = [
        'position:fixed', 'top:0', 'left:0',
        'width:100%', 'height:100%',
        'z-index:-1', 'pointer-events:none',
    ].join(';');
    document.body.prepend(canvas);

    const ctx       = canvas.getContext('2d');
    const COUNT     = 333;
    const particles = [];

    function resize() {
        canvas.width  = window.innerWidth;
        canvas.height = window.innerHeight;
    }

    function make() {
        return {
            x  : Math.random() * canvas.width,
            y  : Math.random() * canvas.height,
            r  : Math.random() * 2 + 0.6,
            dx : (Math.random() - 0.5) * 0.77,
            dy : (Math.random() - 0.5) * 0.77,
            a  : Math.random() * 0.25 + 0.09,
        };
    }

    resize();
    window.addEventListener('resize', resize);
    for (let i = 0; i < COUNT; i++) particles.push(make());

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        const dark = document.documentElement.getAttribute('data-theme') === 'dark';
        const rgb  = dark ? '147,197,253' : '37,99,235';

        particles.forEach(p => {
            p.x += p.dx;
            p.y += p.dy;
            if (p.x < -4) p.x = canvas.width  + 4;
            if (p.x > canvas.width  + 4) p.x = -4;
            if (p.y < -4) p.y = canvas.height + 4;
            if (p.y > canvas.height + 4) p.y = -4;

            ctx.beginPath();
            ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(${rgb},${p.a})`;
            ctx.fill();
        });

        requestAnimationFrame(draw);
    }
    draw();
}

document.addEventListener('DOMContentLoaded', initParticles);

// ── Scroll reveal (main content + mobile) ────────────────────
function initScrollReveal() {
    if (!window.IntersectionObserver) return;
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    const targets = Array.from(document.querySelectorAll(
        '.cv-main .entry-card, .cv-main .cv-summary, .cv-main .section-title'
    ));

    // Masquer immédiatement avant observation
    targets.forEach((el, i) => {
        el.style.opacity    = '0';
        el.style.transform  = 'translateY(16px)';
        el.style.transition =
            `opacity 0.45s ease ${i * 0.05}s, transform 0.45s ease ${i * 0.05}s`;
    });

    const obs = new IntersectionObserver(
        (entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity   = '1';
                    entry.target.style.transform = 'translateY(0)';
                    obs.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.06, rootMargin: '0px 0px -10px 0px' }
    );

    targets.forEach(el => obs.observe(el));
}

document.addEventListener('DOMContentLoaded', initScrollReveal);

"""

# ── CSS ───────────────────────────────────────────────────────
def get_styles() -> str:
    """Retourne le CSS complet. Tout le CSS est ICI, dans cette fonction."""
    return f"""

/* ══════════════════════════════════════════════════════
   DESIGN TOKENS
══════════════════════════════════════════════════════ */

:root {{
    --accent          : {ACCENT_COLOR};
    --accent-light    : #eff6ff;

    --page-bg         : #ffffff;
    --shadow-page     : 0 4px 40px rgba(0,0,0,0.10);

    --header-bg       : #ffffff;
    --name-color      : {SIDEBAR_COLOR};
    --tagline-color   : #475569;
    --contact-color   : #64748b;

    --sidebar-bg      : {SIDEBAR_COLOR};
    --sidebar-text    : #e2e8f0;
    --sidebar-muted   : #94a3b8;
    --sidebar-border  : rgba(255,255,255,0.12);
    --sidebar-h2      : #93c5fd;
    --sidebar-tag-bg  : rgba(255,255,255,0.10);
    --sidebar-tag-bd  : rgba(255,255,255,0.20);

    --main-bg         : #ffffff;
    --card-bg         : #f8fafc;
    --card-border     : #e2e8f0;
    --card-shadow     : 0 1px 3px rgba(0,0,0,0.05), 0 4px 14px rgba(0,0,0,0.07);
    --text            : #1e293b;
    --text-muted      : #64748b;
    --section-border  : {ACCENT_COLOR};

    --tag-bg          : #eff6ff;
    --tag-text        : #1d4ed8;
    --tag-border      : #bfdbfe;

    /* ── KPI badges (palette configurable dans cv_config.py) ── */
    --kpi-bg          : {KPI_BG};
    --kpi-text        : {KPI_TEXT};
    --kpi-border      : {KPI_BORDER};

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

    --kpi-bg          : #1e3a5f;
    --kpi-text        : #93c5fd;
    --kpi-border      : #3b82f6;
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
   CANVAS PARTICULES
══════════════════════════════════════════════════════ */

#cv-particles {{ display: block; }}


/* ══════════════════════════════════════════════════════
       GRADIENT EXPÉRIENCES — actuelle → plus ancienne
       (les classes entry-card--0/1/2 sont posées par builder.py)
    ══════════════════════════════════════════════════════ */

    /* ── Rôle actuel (0) : bleu vif + halo ── */
    .section-experience .entry-card--0 {{
        border-left-color : {ACCENT_COLOR} !important;
        border-left-width : 4px !important;
        box-shadow        : var(--card-shadow),
                            0 0 0  2px rgba(37,99,235,0.08),
                            0 0 18px rgba(37,99,235,0.14) !important;
    }}

    /* ── Rôle intermédiaire (1) : bleu moyen ── */
    .section-experience .entry-card--1 {{
        border-left-color : #60a5fa !important;
        border-left-width : 3px !important;
    }}

    /* ── Rôle le plus ancien (2+) : bleu clair ── */
    .section-experience .entry-card--2,
    .section-experience .entry-card--3 {{
        border-left-color : #bfdbfe !important;
        border-left-width : 3px !important;
    }}

    /* ── Dark mode ── */
    [data-theme="dark"] .section-experience .entry-card--0 {{
        box-shadow: var(--card-shadow),
                    0 0 0  2px rgba(96,165,250,0.12),
                    0 0 22px rgba(96,165,250,0.20) !important;
    }}
    [data-theme="dark"] .section-experience .entry-card--1 {{
        border-left-color: #3b82f6 !important;
    }}
    [data-theme="dark"] .section-experience .entry-card--2,
    [data-theme="dark"] .section-experience .entry-card--3 {{
        border-left-color: #1d4ed8 !important;
    }}

  
 /* ══════════════════════════════════════════════════════
   IMPRESSION / PDF
══════════════════════════════════════════════════════ */

@page {{ margin: 5mm 8mm; }}

@media print {{

    .theme-toggle,
    #cv-particles {{ display: none !important; }}

    [style*="opacity"]   {{ opacity: 1 !important; }}
    [style*="transform"] {{ transform: none !important; }}

    html, body {{ height: auto !important; overflow: visible !important; }}

    body, .cv-page {{
        background   : white !important;
        box-shadow   : none  !important;
        border-radius: 0     !important;
        margin       : 0     !important;
        max-width    : none  !important;
    }}
    body {{ font-size: 8pt !important; line-height: 1.3 !important; }}

    /* Header */
    .cv-header          {{ flex-direction: row !important; }}
    .cv-header-photo-col {{
        width  : 190px  !important;
        padding: 10px   !important;
        -webkit-print-color-adjust: exact;
        print-color-adjust        : exact;
    }}
    .cv-photo,
    .cv-photo-placeholder {{ width: 78px !important; height: 78px !important; }}
    .cv-photo-placeholder  {{ font-size: 18pt !important; }}
    .cv-header-info-col    {{ padding: 10px 36px 10px 16px !important; }}
    .cv-name    {{ font-size: 16pt !important; letter-spacing: 2px !important; margin-bottom: 3px !important; }}
    .cv-tagline {{ font-size: 8pt  !important; margin-bottom: 5px !important; }}
    .cv-contact {{ font-size: 7pt  !important; gap: 2px 10px !important; }}
    .cv-contact-icon svg.cv-icon {{ width: 8px !important; height: 8px !important; }}

    /* Corps */
    .cv-body {{
        display        : flex          !important;
        flex-direction : row           !important;
        min-height     : 0             !important;
        align-items    : flex-start    !important;
    }}
    .cv-sidebar {{
        width     : 190px !important;
        order     : -1    !important;
        padding   : 10px 12px 12px !important;
        height    : auto !important;
        align-self: flex-start !important;
        -webkit-print-color-adjust: exact;
        print-color-adjust        : exact;
    }}
    .cv-main {{ order: 1 !important; padding: 10px 14px 12px !important; }}

    /* Titres */
    .section-title {{
        font-size     : 7.5pt !important;
        letter-spacing: 1.5px !important;
        margin-top    : 9px   !important;
        margin-bottom : 6px   !important;
        padding-bottom: 3px   !important;
    }}
    .cv-main > section:first-child .section-title {{ margin-top: 0 !important; }}

    /* Cartes */
    .entry-card      {{ padding: 5px 8px !important; margin-bottom: 4px !important; page-break-inside: avoid; }}
    .section-title   {{ page-break-after: avoid; }}
    .entry-title     {{ font-size: 7.5pt !important; }}
    .entry-sub       {{ font-size: 6.5pt !important; }}
    .entry-date      {{ font-size: 6.5pt !important; padding: 1px 4px !important; }}
    .entry ul        {{ margin-left: 10px !important; margin-top: 2px !important; }}
    .entry ul li     {{ font-size: 7pt !important; margin-bottom: 1px !important; line-height: 1.3 !important; }}
    .cv-summary      {{ font-size: 7pt !important; padding: 5px 8px !important; }}

    /* Sidebar */
    .skill-category  {{ font-size: 6pt !important; margin-top: 6px !important; margin-bottom: 2px !important; }}
    .tag             {{ font-size: 6pt !important; padding: 1px 5px !important; }}
    .lang-item       {{ margin-bottom: 3px !important; }}
    .lang-name       {{ font-size: 7.5pt !important; }}
    .lang-level      {{ font-size: 6.5pt !important; }}
    .assoc-entry     {{ margin-bottom: 4px !important; }}
    .assoc-role      {{ font-size: 7.5pt !important; }}
    .assoc-org,
    .assoc-desc      {{ font-size: 6.5pt !important; }}
    .interest-item   {{ font-size: 6.5pt !important; margin-bottom: 2px !important; }}
    .kpi-badge       {{ font-size: 6.5pt !important; padding: 0 3px !important; }}
}}

/* ══════════════════════════════════════════════════════
   THEME TOGGLE BUTTON
══════════════════════════════════════════════════════ */

.theme-toggle {{
    position     : absolute;
    top          : 16px;
    right        : 20px;
    background   : var(--card-bg);
    border       : 1px solid var(--card-border);
    border-radius: var(--radius-tag);
    padding      : 4px 12px;
    font-size    : 14px;
    cursor       : pointer;
    box-shadow   : var(--card-shadow);
    transition   : all 0.2s;
    z-index      : 10;
    line-height  : 1.4;
}}
.theme-toggle:hover {{ box-shadow: 0 4px 16px rgba(0,0,0,0.15); }}

/* ══════════════════════════════════════════════════════
   PAGE WRAPPER
══════════════════════════════════════════════════════ */

.cv-page {{
    max-width    : 1000px; /* was 920px */
    margin       : 24px auto;
    border-radius: 12px;
    overflow     : hidden;
    box-shadow   : var(--shadow-page);
    position     : relative;
    z-index      : 1;
}}

/* ══════════════════════════════════════════════════════
   HEADER — photo gauche, info droite
══════════════════════════════════════════════════════ */

.cv-header {{
    display       : flex;
    flex-direction: row;
    align-items   : stretch;
    border-bottom : 3px solid var(--accent);
    position      : relative;
    padding       : 0;
}}

.cv-header-photo-col {{
    width          : 265px;
    flex-shrink    : 0;
    background     : var(--sidebar-bg);
    display        : flex;
    align-items    : center;
    justify-content: center;
    padding        : 20px;
    transition     : background 0.2s;
    -webkit-print-color-adjust: exact;
    print-color-adjust        : exact;
}}

.cv-photo {{
    width        : 110px;
    height       : 110px;
    border-radius: 50%;
    object-fit   : cover;
    border       : 3px solid rgba(255,255,255,0.35);
    display      : block;
}}

.cv-photo-placeholder {{
    width          : 110px;
    height         : 110px;
    border-radius  : 50%;
    background     : rgba(255,255,255,0.07);
    border         : 2px dashed rgba(255,255,255,0.25);
    display        : flex;
    align-items    : center;
    justify-content: center;
    font-size      : 24pt;
    font-weight    : bold;
    color          : rgba(255,255,255,0.45);
    letter-spacing : 3px;
}}

.cv-header-info-col {{
    flex      : 1;
    background: var(--header-bg);
    padding   : 22px 56px 18px 22px;
    position  : relative;
    transition: background 0.2s;
    display   : flex;
    flex-direction: column;
    justify-content: center;
}}

.cv-name {{
    font-size     : 24pt;
    font-weight   : bold;
    letter-spacing: 3px;
    text-transform: uppercase;
    color         : var(--name-color);
    line-height   : 1.1;
    margin-bottom : 5px;
}}

.cv-tagline {{
    font-size    : 10.5pt;
    color        : var(--accent);
    font-weight  : 600;
    margin-bottom: 10px;
}}

/* ── Contacts — alignement icônes + texte ── */

.cv-contact {{
    font-size  : 8.5pt; /* was 9pt */
    color      : var(--contact-color);
    display    : flex;
    flex-wrap  : wrap;
    gap        : 4px 11px; /*was 5px 18px */
    align-items: center;
}}

.cv-contact-item {{
    display    : inline-flex;
    align-items: center;
    gap        : 5px;
    line-height: 1;
    white-space: nowrap;
}}

.cv-contact-icon {{
    display    : inline-flex;
    align-items: center;
    flex-shrink: 0;
    line-height: 0;
}}

.cv-contact-icon svg.cv-icon {{
    width      : 12px;
    height     : 12px;
    fill       : currentColor;
    display    : block;
    flex-shrink: 0;
    opacity    : 0.7;
}}

.cv-contact-text {{
    line-height: 1;
}}

.cv-contact-link {{
    color          : inherit;
    text-decoration: none;
    transition     : color 0.15s;
}}
.cv-contact-link:hover {{ color: var(--accent); text-decoration: underline; }}

/* ══════════════════════════════════════════════════════
   DEUX COLONNES
══════════════════════════════════════════════════════ */

.cv-body {{
    display    : flex;
    min-height : 700px;
    align-items: stretch;
}}

.cv-sidebar {{
    width      : 265px;
    flex-shrink: 0;
    background : var(--sidebar-bg);
    color      : var(--sidebar-text);
    padding    : 24px 20px 32px;
    order      : -1;
    transition : background 0.2s;
}}

.cv-main {{
    flex      : 1;
    background: var(--main-bg);
    padding   : 24px 28px 32px;
    order     : 1;
    transition: background 0.2s;
}}

/* ══════════════════════════════════════════════════════
   TITRES DE SECTION
══════════════════════════════════════════════════════ */

.section-title {{
        font-size      : 10pt;
        font-weight    : bold;
        text-transform : uppercase;
        letter-spacing : 2.5px;
        margin-top     : 24px;
        margin-bottom  : 14px;
        padding-bottom : 8px;
}}

.cv-main .section-title {{
        color        : var(--accent);
        border-bottom: 2.5px solid var(--section-border);
}}

.cv-sidebar .section-title {{
        color        : var(--sidebar-h2);
        border-bottom: 1px solid var(--sidebar-border);
        margin-top   : 24px;
    }}

.cv-sidebar .section-title:first-child {{ margin-top: 0; }}

.cv-main > section:first-child .section-title {{ margin-top: 0; }}



.cv-main .section-title {{

    color       : var(--accent);
    border-bottom: 1.5px solid var(--section-border);
}}

.cv-sidebar .section-title {{
    color       : var(--sidebar-h2);
    border-bottom: 1px solid var(--sidebar-border);
    margin-top  : 24px;
}}

.cv-sidebar .section-title:first-child {{ margin-top: 0; }}

/* Espacement bas de chaque section sidebar (dernier tag / titre suivant) */
    .cv-sidebar section {{ padding-bottom: 6px; }}
    .cv-sidebar section:last-child {{ padding-bottom: 0; }}

/* ══════════════════════════════════════════════════════
   CARTES EXPÉRIENCE / FORMATION
══════════════════════════════════════════════════════ */

.entry-card {{
    background   : var(--card-bg);
    border       : 1px solid var(--card-border);
    border-left  : 3px solid var(--accent);
    border-radius: var(--radius-card);
    padding      : 12px 14px;
    margin-bottom: 10px;
    box-shadow   : var(--card-shadow);
    transition   : background 0.2s, box-shadow 0.2s;
}}

.entry-header {{
    display        : flex;
    justify-content: space-between;
    align-items    : flex-start;
    gap            : 10px;
    margin-bottom  : 4px;
}}

.entry-left {{ flex: 1; min-width: 0; }}

.entry-title {{
    font-weight: bold;
    font-size  : 10.5pt;
    color      : var(--text);
    line-height: 1.3;
}}

.entry-sub {{
    font-size : 9.5pt;
    color     : var(--text-muted);
    font-style: italic;
    margin-top: 2px;
}}

.entry-date {{
    font-size    : 9pt;
    color        : var(--text-muted);
    white-space  : nowrap;
    text-align   : right;
    flex-shrink  : 0;
    background   : var(--accent-light);
    border-radius: var(--radius-tag);
    padding      : 2px 8px;
    height       : fit-content;
    font-weight  : 500;
}}

.entry ul {{
    margin-left: 16px;
    margin-top : 7px;
}}

.entry ul li {{
    font-size    : 10pt;
    margin-bottom: 3px;
    line-height  : 1.45;
    color        : var(--text);
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
   TAGS
══════════════════════════════════════════════════════ */

.cv-sidebar .tags {{ display: flex; flex-wrap: wrap; gap: 4px; margin-top: 4px; }}
.cv-sidebar .tag {{
    display      : inline-block;
    background   : var(--sidebar-tag-bg);
    color        : var(--sidebar-text);
    border       : 1px solid var(--sidebar-tag-bd);
    border-radius: var(--radius-tag);
    padding      : 2px 10px;
    font-size    : 8.5pt;
    line-height  : 1.5;
}}

.cv-main .tags {{ display: flex; flex-wrap: wrap; gap: 4px; margin-top: 6px; }}
.cv-main .tag {{
    display      : inline-block;
    background   : var(--tag-bg);
    color        : var(--tag-text);
    border       : 1px solid var(--tag-border);
    border-radius: var(--radius-tag);
    padding      : 2px 10px;
    font-size    : 8.5pt;
    line-height  : 1.5;
    font-weight  : 500;
}}

/* ══════════════════════════════════════════════════════
   COMPÉTENCES (sidebar)
══════════════════════════════════════════════════════ */

.skill-category {{
    font-size     : 9pt;
    font-weight   : bold;
    color         : var(--sidebar-muted);
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-top    : 12px;
    margin-bottom : 5px;
}}
.skill-category:first-of-type {{ margin-top: 0; }}

/* ══════════════════════════════════════════════════════
   LANGUES (sidebar)
══════════════════════════════════════════════════════ */

.lang-item  {{ margin-bottom: 8px; }}
.lang-name  {{ font-weight: bold; font-size: 10pt; }}
.lang-level {{ font-size: 9pt; color: var(--sidebar-muted); }}

.lang-dots {{ display: flex; gap: 4px; margin-top: 3px; }}
.lang-dot {{
    width        : 10px;
    height       : 10px;
    border-radius: 50%;
    background   : var(--sidebar-tag-bd);
}}
.lang-dot.filled {{ background: var(--sidebar-h2); }}

/* ══════════════════════════════════════════════════════
   ASSOCIATIONS (sidebar)
══════════════════════════════════════════════════════ */

.assoc-entry {{ margin-bottom: 10px; }}
.assoc-role  {{ font-weight: bold; font-size: 10pt; }}
.assoc-org   {{ font-size: 9pt; color: var(--sidebar-muted); font-style: italic; }}
.assoc-desc  {{ font-size: 9pt; margin-top: 2px; line-height: 1.4; }}

/* ══════════════════════════════════════════════════════
   INTÉRÊTS (sidebar)
══════════════════════════════════════════════════════ */

.interest-item {{
    font-size    : 9.5pt;
    margin-bottom: 5px;
    display      : flex;
    align-items  : flex-start;
    gap          : 6px;
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
    background   : var(--accent-light);
    border-left  : 3px solid var(--accent);
    border-radius: 0 var(--radius-card) var(--radius-card) 0;
    padding      : 10px 14px;
    font-size    : 10pt;
    line-height  : 1.6;
    margin-bottom: 4px;
    color        : var(--text);
}}

/* ══════════════════════════════════════════════════════
   RESPONSIVE — TABLET (max 768px)
══════════════════════════════════════════════════════ */

@media (max-width: 768px) {{
    .cv-page {{ margin: 0; border-radius: 0; box-shadow: none; }}

    .cv-header        {{ flex-direction: column; }}
    .cv-header-photo-col {{
        width          : 100%;
        padding        : 14px 20px;
        flex-direction : row;
        justify-content: flex-start;
        gap            : 16px;
    }}
    .cv-photo,
    .cv-photo-placeholder {{ width: 64px; height: 64px; flex-shrink: 0; }}
    .cv-photo-placeholder  {{ font-size: 14pt; }}
    .cv-header-info-col    {{ padding: 14px 16px 14px 16px; }}
    .cv-name    {{ font-size: 18pt; }}
    .cv-tagline {{ font-size: 9.5pt; }}
    .cv-contact {{ flex-direction: column; gap: 5px; }}

    .cv-body    {{ flex-direction: column; }}
    .cv-sidebar {{ width: 100%; order: 2; padding: 20px 16px 28px; }}
    .cv-main    {{ order: 1; padding: 16px 16px 20px; }}

    .theme-toggle {{ top: 10px; right: 12px; padding: 3px 8px; font-size: 12px; }}
    .entry-header {{ flex-direction: column; gap: 5px; }}
    .entry-date   {{ align-self: flex-start; }}
}}

@media (max-width: 480px) {{
    .cv-name    {{ font-size: 15pt; letter-spacing: 1px; }}
    body        {{ font-size: 10pt; }}
    .cv-main,
    .cv-sidebar {{ padding: 14px 14px 20px; }}
    .entry-card {{ padding: 10px 12px; }}
}}

/* ══════════════════════════════════════════════════════
   RESPONSIVE — MOBILE (max 480px)
══════════════════════════════════════════════════════ */

@media (max-width: 480px) {{
    .cv-name    {{ font-size: 15pt; letter-spacing: 1px; }}
    body        {{ font-size: 10pt; }}
    .cv-header  {{ padding: 16px 14px 12px; }}
    .cv-main,
    .cv-sidebar {{ padding: 14px 14px 20px; }}
    .entry-card {{ padding: 10px 12px; }}
    .cv-tagline {{ font-size: 9.5pt; }}
}}

"""