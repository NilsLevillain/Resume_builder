"""
🖊  Contenu du CV — Bilingue FR / EN
    Adapté pour : Website Factory Tech Project Manager @ L'Oréal
"""

def bi(fr: str, en: str) -> dict:
    return {"fr": fr, "en": en}

def kpi(text: str) -> str:
    return f'<span class="kpi-badge">{text}</span>'

def bold(text: str) -> str:
    return f'<strong>{text}</strong>'

# ══════════════════════════════════════════════════════════════
#  INFORMATIONS PERSONNELLES
# ══════════════════════════════════════════════════════════════

PERSONAL = {
    "name"    : "Nils Levillain",
    "title"   : bi(
        "Tech Project Manager | Product Owner Analytics @ L'Oréal",
        "Tech Project Manager | Product Owner Analytics @ L'Oréal",
    ),
    "email"   : "levillain.nils@gmail.com",
    "phone"   : "+33 06 69 56 69 37",
    "location": "Paris, France",
    "linkedin": "linkedin.com/in/nils-levillain",
    "github"  : "github.com/nils-levillain",
}

# ══════════════════════════════════════════════════════════════
#  RÉSUMÉ
# ══════════════════════════════════════════════════════════════

SUMMARY = bi(
    fr=(
        "Tech Project Manager & Product Owner avec 3+ ans chez L'Oréal. "
        "Expert en pilotage de projets tech dans un environnement agile et international, "
        "je fais le pont entre équipes techniques et métier à l'échelle mondiale. "
        "Expertise : cloud (GCP), IA/ML, conduite du changement et gestion multi-parties prenantes."
    ),
    en=(
        "Tech Project Manager & Product Owner with 3+ years at L'Oréal. "
        "Expert in end-to-end tech project delivery in agile, global environments, "
        "bridging technical teams and business stakeholders across multiple zones. "
        "Expertise: cloud (GCP), AI/ML, change management, and stakeholder coordination."
    ),
)

# ══════════════════════════════════════════════════════════════
#  EXPÉRIENCES  (L'Oréal uniquement)
# ══════════════════════════════════════════════════════════════

EXPERIENCE = [
    {
        "title"  : bi(
            "Product Owner Analytics – Global Supply Chain",
            "Product Owner Analytics – Global Supply Chain",
        ),
        "company": "L'Oréal",
        "start"  : bi("Janv. 2024",    "Jan. 2024"),
        "end"    : bi("Aujourd'hui",   "Present"),
        "bullets": [
            bi(
                f"Agile Tech PM : pilotage end-to-end de produits analytiques mondiaux "
                f"(Fulfillment) — {kpi('+200 utilisateurs')} dans 5 zones géographiques ; "
                f"définition & exécution de la {bold('roadmap technique')}.",
                f"Agile Tech PM: end-to-end delivery of global analytics products "
                f"(Fulfillment) — {kpi('200+ users')} across 5 zones; "
                f"{bold('technical roadmap')} definition & execution.",
            ),
            bi(
                f"Pont tech/métier : traduction des besoins en specs techniques ; "
                f"coordination {bold('multi-parties prenantes')} (IT Zones, Divisions, "
                f"Architectes) en environnement matriciel global.",
                f"Bridge tech/business: business needs into technical specs; "
                f"{bold('multi-stakeholder')} coordination (IT Zones, Divisions, "
                f"Architects) in a global matrixed org.",
            ),
            bi(
                f"AI & Innovation : {bold('POCs IA/ML')} (forecasting, Programmation "
                f"Linéaire, Web App Full-Stack) — du prototype au déploiement global ; "
                f"calculateur CO2 Transport.",
                f"AI & Innovation: {bold('AI/ML POCs')} (forecasting, Linear Programming, "
                f"Full-Stack Web App) — from prototype to global deployment; "
                f"CO2 Transport calculator.",
            ),
            bi(
                f"Cloud & Data Engineering : {bold('GCP')} (BigQuery, Architecture "
                f"Médaillon), SQL complexe, data quality monitoring en production.",
                f"Cloud & Data Engineering: {bold('GCP')} (BigQuery, Medallion "
                f"Architecture), complex SQL, data quality monitoring in production.",
            ),
            bi(
                f"Déploiement & {bold('change management')} : Power BI (DAX), "
                f"Web Apps, NPS tracking ; coordination partenaires technologiques.",
                f"Deployment & {bold('change management')}: Power BI (DAX), "
                f"Web Apps, NPS tracking; technology partner coordination.",
            ),
        ],
    },
    {
        "title"  : bi(
            "Ingénieur Projets Supply Chain – WMS Key User",
            "Supply Chain Project Engineer – WMS Key User",
        ),
        "company": "L'Oréal",
        "start"  : bi("Sept. 2022", "Sept. 2022"),
        "end"    : bi("Déc. 2023",  "Dec. 2023"),
        "bullets": [
            bi(
                f"Remplacement WMS {bold('SAP → Manhattan')} : coordination IT, "
                f"ops & partenaires externes — {kpi('+100 cas de test')} définis & exécutés.",
                f"{bold('SAP → Manhattan')} WMS replacement: coordinated IT, ops "
                f"& external partners — {kpi('100+')} test cases defined & executed.",
            ),
            bi(
                f"{kpi('+20 rapports BI')} impactants ; animation communauté "
                f"dev Europe ; migration données inter-systèmes.",
                f"{kpi('20+')} impactful BI reports; European developer community "
                f"leadership; inter-system data migration.",
            ),
            bi(
                f"{bold('Conduite du changement')} : documentation & "
                f"{kpi('~50h')} de formation opérateurs et chefs d'équipe.",
                f"{bold('Change management')}: documentation & "
                f"{kpi('~50h')} training for operators and team leaders.",
            ),
        ],
    },
    {
        "title"  : "Copacking Planner",
        "company": "L'Oréal",
        "start"  : bi("Janv. 2022", "Jan. 2022"),
        "end"    : bi("Juil. 2022", "Jul. 2022"),
        "bullets": [
            bi(
                f"Planification, appro & logistique catalogue promo Garnier "
                f"— {kpi('99% service rate')}.",
                f"Planning, procurement & logistics for Garnier's promo "
                f"catalogue — {kpi('99% service rate')}.",
            ),
            bi(
                f"Réduction {kpi('−20%')} des écarts de stock copacker "
                f"via dashboards de suivi.",
                f"{kpi('−20%')} stock gap reduction with co-packer "
                f"through monitoring dashboards.",
            ),
        ],
    },
]

# ══════════════════════════════════════════════════════════════
#  FORMATION
# ══════════════════════════════════════════════════════════════

EDUCATION = [
    {
        "degree" : bi(
            "Diplôme d'Ingénieur · Supply Chain, Data & Systèmes d'Information",
            "Engineering Degree (MSc) · Supply Chain, Data & Information Systems",
        ),
        "school" : "Grenoble INP – Génie Industriel",
        "start"  : "2019",
        "end"    : "2022",
        "bullets": [
            bi(
                "Top école française de Génie Industriel — programme Grande École.",
                "Top French Engineering School — Grande École programme.",
            ),
            bi(
                "Spécialisation : ERP (SAP), recherche opérationnelle, data science, gestion de projet.",
                "Specialisation: ERP (SAP), operations research, data science, project management.",
            ),
        ],
    },
    {
        "degree" : bi(
            "Échange Académique · Génie Industriel & Informatique",
            "Academic Exchange · Industrial Engineering & Computer Science",
        ),
        "school" : "École Polytechnique de Montréal",
        "start"  : "2021",
        "end"    : "2022",
        "bullets": [
            bi(
                "SAP, data mining, machine learning, gestion de projet tech.",
                "SAP, data mining, machine learning, tech project management.",
            ),
        ],
    },
]

# ══════════════════════════════════════════════════════════════
#  COMPÉTENCES  (skills distincts, sans redondance)
# ══════════════════════════════════════════════════════════════

SKILLS = [
    {
        "category": bi("Gestion de Projet", "Project Delivery"),
        "items"   : [
            "Agile / Scrum",
            "Stakeholder Management",
            "Change Management",
            "UX/UI Design",
        ],
    },
    {
        "category": bi("Cloud & Data", "Cloud & Data"),
        "items"   : [
            "GCP (BigQuery)",
            "SQL",
            "Python (ML)",
            "Power BI (DAX)",
        ],
    },
    {
        "category": bi("Plateformes", "Platforms"),
        "items"   : [
            "SAP",
            "Manhattan WMS",
            "MS Office (Excel, Project)",
        ],
    },
]

# ══════════════════════════════════════════════════════════════
#  LANGUES
# ══════════════════════════════════════════════════════════════

LANGUAGES = [
    {"lang": "Français",           "level": bi("Langue maternelle", "Native")},
    {"lang": "Anglais / English",  "level": bi("C2 — TOEFL ITP 624", "C2 — TOEFL ITP 624")},
    {"lang": "Español / Espagnol", "level": bi("B1/B2", "B1/B2")},
]

# ══════════════════════════════════════════════════════════════
#  VIE ASSOCIATIVE
# ══════════════════════════════════════════════════════════════

ASSOCIATIONS = [
    {
        "role"       : bi("Président du Bureau des Sports",
                          "President of the Sports Committee"),
        "org"        : "Grenoble INP",
        "period"     : "2020 – 2021",
        "description": bi(
            "Management de 27 personnes sur 1,5 an — budget : 25K€.",
            "Management of 27 people over 18 months — budget: €25K.",
        ),
    },
]

# ══════════════════════════════════════════════════════════════
#  INTÉRÊTS
# ══════════════════════════════════════════════════════════════

INTERESTS = [
    bi("Musique & Art (guitariste et bassiste autodidacte)",
       "Music & Art (self-taught guitarist and bassist)"),
    bi("Ski (10 ans de compétition en club)",
       "Skiing (10 years of club competition)"),
    bi("Force athlétique (niveau régional)",
       "Powerlifting (regional level)"),
]