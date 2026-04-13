"""
🖊  Contenu du CV — Bilingue FR / EN
    Adapté pour : Website Factory Tech Project Manager @ L'Oréal
"""

# ── Helpers ───────────────────────────────────────────────────
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
    "location": "Paris, 75010, France",
    "linkedin": "linkedin.com/in/nils-levillain",
    "github"  : "github.com/nils-levillain",       # ← adapter si username différent
}

# ══════════════════════════════════════════════════════════════
#  RÉSUMÉ
# ══════════════════════════════════════════════════════════════

SUMMARY = bi(
    fr=(
        "Tech Project Manager & Technical Product Owner avec 3+ ans chez L'Oréal. "
        "Expert en pilotage de projets tech end-to-end dans un environnement agile "
        "et international, je fais le pont entre équipes techniques et métier à l'échelle "
        "de plusieurs zones géographiques. Expertise : cloud (GCP), IA/ML, conduite du "
        "changement, gestion de partenaires technologiques et communication multi-niveaux."
    ),
    en=(
        "Tech Project Manager & Technical Product Owner with 3+ years at L'Oréal. "
        "Expert in end-to-end tech project delivery in agile, global environments, "
        "bridging the gap between technical teams and business stakeholders across "
        "multiple zones. Expertise: cloud (GCP), AI/ML, change management, technology "
        "partner coordination, and multi-level communication."
    ),
)

# ══════════════════════════════════════════════════════════════
#  EXPÉRIENCES  (L'Oréal uniquement)
# ══════════════════════════════════════════════════════════════

EXPERIENCE = [
    {
        "title"   : bi(
            "Product Owner Analytics – Global Supply Chain",
            "Product Owner Analytics – Global Supply Chain",
        ),
        "company" : "L'Oréal",
        "type"    : bi("CDI", "Permanent"),
        "location": bi("Clichy, Île-de-France", "Clichy, France"),
        "start"   : bi("Janvier 2024",  "January 2024"),
        "end"     : bi("Aujourd'hui",   "Present"),
        "bullets" : [
            bi(
                f"Tech Project Manager agile : pilotage end-to-end de produits analytiques "
                f"mondiaux pour toutes les Zones et Divisions L'Oréal — {kpi('+200 utilisateurs '
                f'actifs')} ; définition et exécution de la {bold('roadmap technique')}.",
                f"Agile Tech Project Manager: end-to-end delivery of global analytics products "
                f"across all L'Oréal Zones and Divisions — {kpi('200+ active users')}; "
                f"defined and executed the {bold('technical roadmap')}.",
            ),
            bi(
                f"Pont technique / métier : traduction des besoins métier en spécifications "
                f"techniques ; coordination de multiples {bold('parties prenantes')} dans un "
                f"environnement international et matriciel (IT Zones, Divisions, Architectes).",
                f"Bridge between tech and business: translated business needs into technical "
                f"specifications; coordinated multiple {bold('stakeholders')} in a global, "
                f"matrixed organisation (IT Zones, Divisions, Architects).",
            ),
            bi(
                f"Innovation & IA : {bold('Proof-of-Concepts')} en IA/ML (forecasting, "
                f"Programmation Linéaire, Web App Full-Stack) — de l'idéation au déploiement "
                f"global ; calculateur CO2 Transport.",
                f"Innovation & AI: {bold('Proof-of-Concepts')} in AI/ML (forecasting, "
                f"Linear Programming, Full-Stack Web App) — from ideation to global "
                f"deployment; CO2 Transport calculator.",
            ),
            bi(
                f"Cloud & Data Engineering : {bold('GCP (BigQuery)')}, Architecture Médaillon, "
                f"SQL complexe, suivi qualité des données en production.",
                f"Cloud & Data Engineering: {bold('GCP (BigQuery)')}, Medallion Architecture, "
                f"complex SQL, data quality monitoring in production.",
            ),
            bi(
                f"Déploiement & {bold('conduite du changement')} : Power BI (DAX), Web Apps, "
                f"tracking adoption & NPS ; coordination de partenaires technologiques.",
                f"Deployment & {bold('change management')}: Power BI (DAX), Web Apps, "
                f"adoption & NPS tracking; technology partner coordination.",
            ),
            bi(
                f"Reporting & impact : définition de KPIs, pilotage budgétaire, "
                f"restitution aux équipes tech et métier.",
                f"Reporting & impact: KPI definition, budget monitoring, "
                f"presentation to both technical and business audiences.",
            ),
        ],
    },
    {
        "title"   : bi(
            "Ingénieur Projets Supply Chain – WMS Key User",
            "Supply Chain Project Engineer – WMS Key User",
        ),
        "company" : "L'Oréal",
        "type"    : bi("CDI", "Permanent"),
        "location": bi("Croissy-Beaubourg, Île-de-France", "Croissy-Beaubourg, France"),
        "start"   : bi("Septembre 2022", "September 2022"),
        "end"     : bi("Décembre 2023",  "December 2023"),
        "bullets" : [
            bi(
                f"Chef de projet tech : remplacement du WMS en centrale de distribution "
                f"({bold('SAP → Manhattan')}), coordinant équipes IT, opérations et "
                f"{bold('partenaires externes')} dans un environnement multi-sites.",
                f"Tech project delivery: WMS replacement in distribution centre "
                f"({bold('SAP → Manhattan')}), coordinating IT teams, operations, "
                f"and {bold('external partners')} across multiple sites.",
            ),
            bi(
                f"Développement BI & reporting : {kpi('+20 rapports')} impactants, animation "
                f"de la communauté de développeurs Europe, migration de données inter-systèmes.",
                f"BI development & reporting: {kpi('20+')} impactful reports, European "
                f"developer community leadership, inter-system data migration.",
            ),
            bi(
                f"Tests & qualité : définition et exécution de {kpi('+100 cas de test')}, "
                f"suivi des KPIs d'avancement.",
                f"Testing & quality: definition and execution of {kpi('100+')} test cases, "
                f"progress KPI tracking.",
            ),
            bi(
                f"{bold('Conduite du changement')} : documentation, {kpi('~50h')} de formation "
                f"opérateurs et chefs d'équipe, accompagnement déploiement et optimisation continue.",
                f"{bold('Change management')}: documentation, {kpi('~50h')} training for "
                f"operators and team leaders, deployment support and continuous optimisation.",
            ),
        ],
    },
    {
        "title"   : "Copacking Planner",
        "company" : "L'Oréal",
        "type"    : bi("Stage", "Internship"),
        "location": bi("Levallois-Perret, Île-de-France", "Levallois-Perret, France"),
        "start"   : bi("Janvier 2022", "January 2022"),
        "end"     : bi("Juillet 2022", "July 2022"),
        "bullets" : [
            bi(
                f"Planification, approvisionnement et logistique du catalogue promotionnel "
                f"Garnier — {kpi('taux de service 99%')}.",
                f"Planning, procurement and logistics for Garnier's promotional "
                f"catalogue — {kpi('99% service rate')}.",
            ),
            bi(
                f"Réduction {kpi('−20%')} des écarts de stock avec le principal copacker "
                f"via tableaux de bord de suivi.",
                f"{kpi('−20%')} stock discrepancy reduction with main co-packer "
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
        "degree"  : bi(
            "Master – Génie Industriel, spécialité Logistique & Supply Chain",
            "MSc – Industrial Engineering, Supply Chain & Logistics",
        ),
        "school"  : "Grenoble INP – Génie Industriel",
        "location": "Grenoble, France",
        "start"   : "2019",
        "end"     : "2022",
        "bullets" : [
            bi(
                "Organisation industrielle, ERP (SAP), industrie 4.0, Lean manufacturing.",
                "Industrial organisation, ERP (SAP), Industry 4.0, Lean manufacturing.",
            ),
            bi(
                "Data science, recherche opérationnelle, gestion de projet.",
                "Data science, operations research, project management.",
            ),
        ],
    },
    {
        "degree"  : bi(
            "Échange universitaire – Génie Industriel & Génie Informatique",
            "University Exchange – Industrial Engineering & Computer Science",
        ),
        "school"  : "École Polytechnique de Montréal",
        "location": "Montréal, Canada",
        "start"   : "2021",
        "end"     : "2022",
        "bullets" : [
            bi(
                "Systèmes de gestion d'entreprise (SAP), data mining, machine learning.",
                "Enterprise resource planning (SAP), data mining, machine learning.",
            ),
        ],
    },
]

# ══════════════════════════════════════════════════════════════
#  COMPÉTENCES  (alignées job offer WSF)
# ══════════════════════════════════════════════════════════════

SKILLS = [
    {
        "category": bi("Gestion de Projet Tech", "Tech Project Management"),
        "items"   : [
            "Agile / Scrum", "Roadmap", "PI Planning",
            "Stakeholder Management", "Change Management",
            "Product Management", "UX/UI Design",
        ],
    },
    {
        "category": bi("Cloud & Data", "Cloud & Data"),
        "items"   : [
            "GCP (BigQuery)", "SQL", "Python (ML/Optimisation)",
            "Power BI (DAX, M)", "GitHub (CI/CD)",
        ],
    },
    {
        "category": bi("Plateformes & Outils", "Platforms & Tools"),
        "items"   : [
            "SAP (FI, CO, MM, SD, APO)", "Manhattan WMS",
            "MS Office avancé (Excel, Project)",
        ],
    },
]

# ══════════════════════════════════════════════════════════════
#  LANGUES
# ══════════════════════════════════════════════════════════════

LANGUAGES = [
    {"lang": "Français",          "level": bi("Langue maternelle", "Native")},
    {"lang": "Anglais / English", "level": bi("C2 — TOEFL ITP 624, Cambridge Certificate",
                                              "C2 — TOEFL ITP 624, Cambridge Certificate")},
    {"lang": "Español / Espagnol","level": bi("B1/B2", "B1/B2")},
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
            "Management de 27 personnes sur 1,5 an — budget géré : 25K€.",
            "Management of 27 people over 18 months — budget managed: €25K.",
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