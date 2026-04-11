"""
🖊  Contenu du CV — Bilingue FR / EN
"""

# ── Helpers ───────────────────────────────────────────────────

def bi(fr: str, en: str) -> dict:
    """Champ bilingue."""
    return {"fr": fr, "en": en}

def kpi(text: str) -> str:
    """Badge visuel pour un KPI / chiffre clé dans une bullet.
    Ex : kpi('+200 utilisateurs')  →  badge ambre mis en valeur.
    """
    return f'<span class="kpi-badge">{text}</span>'

def bold(text: str) -> str:
    """Met un mot-clé en gras dans une bullet."""
    return f'<strong>{text}</strong>'

# ── Usage dans les bullets ────────────────────────────────────
# bi(
#     f"Pilotage de produits analytiques — {kpi('+200 utilisateurs actifs')}.",
#     f"Global analytics products — {kpi('200+ active users')}.",
# ),
# bi(
#     f"Réduction {kpi('−20%')} des écarts de stock via {bold('tableaux de bord')}.",
#     f"{kpi('−20%')} stock discrepancy reduction through {bold('monitoring dashboards')}.",
# ),

"""
🖊  Contenu du CV — Bilingue FR / EN
======================================
SEUL FICHIER À MODIFIER pour mettre à jour votre CV.

Convention :
  ┌─ Champ bilingue  → bi("Texte français", "English text")
  └─ Champ identique → "L'Oréal"  (chaîne simple, ex : entreprise, dates, outils)
"""

# ── Helper bilingue ───────────────────────────────────────────
def bi(fr: str, en: str) -> dict:
    """Crée un champ bilingue FR / EN."""
    return {"fr": fr, "en": en}

# ══════════════════════════════════════════════════════════════
#  INFORMATIONS PERSONNELLES
# ══════════════════════════════════════════════════════════════

PERSONAL = {
    "name"    : "Nils Levillain",
    "title"   : bi(
        "Data & Supply Chain | Product Owner Analytics @ L'Oréal",
        "Data & Supply Chain | Product Owner Analytics @ L'Oréal",
    ),
    "email"   : "levillain.nils@gmail.com",
    "phone"   : "+33 06 69 56 69 37",
    "location": "Paris, 75015, France",
    "linkedin": "linkedin.com/in/nils-levillain",
}

# ══════════════════════════════════════════════════════════════
#  RÉSUMÉ / PROFIL
# ══════════════════════════════════════════════════════════════

SUMMARY = bi(
    fr=(
        "Ingénieur Supply Chain avec 3+ ans chez L'Oréal, spécialisé en Data Products "
        "et optimisation logistique. Expertise end-to-end : discovery utilisateur, "
        "data engineering (BigQuery, SQL), déploiement Power BI & Web Apps, avec un "
        "impact direct sur la durabilité (CO2) et la performance financière."
    ),
    en=(
        "Supply Chain Engineer with 3+ years at L'Oréal, specialising in Data Products "
        "and logistics optimisation. End-to-end expertise: user discovery, data engineering "
        "(BigQuery, SQL), Power BI & Web App deployment, with direct impact on "
        "sustainability (CO2) and financial performance."
    ),
)

# ══════════════════════════════════════════════════════════════
#  EXPÉRIENCES PROFESSIONNELLES
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
        "start"   : bi("Janvier 2024",   "January 2024"),
        "end"     : bi("Aujourd'hui",     "Present"),
        "bullets" : [
            bi(
                "Pilotage du développement de produits analytiques mondiaux pour le métier "
                "Fulfillment (Transport, Douane, Entrepôt), toutes Zones et Divisions — "
                "+200 utilisateurs actifs.",
                "Driving the development of global analytics products for the Fulfillment "
                "function (Transport, Customs, Warehouse) across all L'Oréal Zones and "
                "Divisions — 200+ active users.",
            ),
            bi(
                "Durabilité & RSE : calculateur CO2 Transport ; outil No Waste "
                "(optimisation fin de vie des stocks via ML forecasting, "
                "Programmation Linéaire, Web App Full-Stack).",
                "Sustainability & CSR: CO2 Transport calculator; No Waste tool "
                "(end-of-life stock optimisation via ML forecasting, Linear "
                "Programming, Full-Stack Web App).",
            ),
            bi(
                "Performance Financière : suivi efficacité transport, Cockpit Entrepôt 360°, "
                "monitoring Douanes & Compliance, détection Anti-Diversion & Traçabilité.",
                "Financial Performance: transport efficiency tracking, Warehouse 360° "
                "Cockpit, Customs & Compliance monitoring, Anti-Diversion detection.",
            ),
            bi(
                "Discovery & Design : +30 entretiens utilisateurs, UX/UI Design sur mesure.",
                "Discovery & Design: 30+ user interviews, tailored UX/UI Design.",
            ),
            bi(
                "Data Engineering : BigQuery (Architecture Médaillon, Schéma en étoile), "
                "transformations SQL complexes, suivi qualité des données sur GCP.",
                "Data Engineering: BigQuery modelling (Medallion Architecture, Star Schema), "
                "complex SQL transformations, data quality monitoring on GCP.",
            ),
            bi(
                "Stack : SQL (BigQuery), Python (ML/Optimisation), Power BI (DAX), "
                "GitHub (CI/CD).",
                "Stack: SQL (BigQuery), Python (ML/Optimisation), Power BI (DAX), "
                "GitHub (CI/CD).",
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
                "Projet de remplacement du WMS en centrale de distribution "
                "(SAP → Manhattan).",
                "WMS replacement project in the distribution centre (SAP → Manhattan).",
            ),
            bi(
                "Développement BI : +20 rapports impactants, animation de la communauté "
                "de développeurs au niveau Europe, migration de données entre systèmes.",
                "BI Development: 20+ impactful reports, European developer community lead, "
                "data migration between systems.",
            ),
            bi(
                "Configuration & tests du nouveau WMS : définition et exécution de +100 "
                "cas de test, suivi de KPIs d'avancement.",
                "WMS configuration & testing: definition and execution of 100+ test cases, "
                "progress KPI tracking.",
            ),
            bi(
                "Conduite du changement : documentation, formation opérateurs et chefs "
                "d'équipe (~50h), accompagnement au déploiement.",
                "Change management: documentation, training of operators and team "
                "leaders (~50h), deployment support.",
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
                "Planification, approvisionnement et logistique du catalogue promotionnel "
                "Ultradoux de Garnier — taux de service de 99%.",
                "Planning, procurement and logistics for Garnier's Ultradoux promotional "
                "catalogue — 99% service rate.",
            ),
            bi(
                "Analyse et réduction de 20% des écarts de stock avec le principal "
                "copacker (CA & production) via tableaux de bord de suivi.",
                "20% reduction of stock discrepancies with the main co-packer "
                "(turnover & production) through monitoring dashboards.",
            ),
            "SAP/APO · Power BI (PowerPivot, M, DAX) · Excel (M, DAX, VBA)",
        ],
    },
    {
        "title"   : bi("Supply Chain Analyst", "Supply Chain Analyst"),
        "company" : "Plastic Omnium",
        "type"    : bi("Stage", "Internship"),
        "location": bi("Sainte-Julie, Auvergne-Rhône-Alpes", "Sainte-Julie, France"),
        "start"   : bi("Juin 2021",  "June 2021"),
        "end"     : bi("Août 2021", "August 2021"),
        "bullets" : [
            bi(
                "Développement d'un outil de calcul de taille de lot optimale : "
                "recueil du besoin, base de données & GUI, data visualization.",
                "Development of an optimal batch size calculation tool: "
                "requirements gathering, database & GUI, data visualisation.",
            ),
            bi(
                "Déployé en usine — gains potentiels de 175K€.",
                "Deployed in production plants — potential savings of €175K.",
            ),
        ],
    },
    {
        "title"   : bi(
            "Consultant Optimisation de Processus",
            "Process Optimisation Consultant",
        ),
        "company" : "STMicroelectronics",
        "type"    : bi("Partenariat universitaire", "University partnership"),
        "location": "Grenoble, France",
        "start"   : bi("Février 2021", "February 2021"),
        "end"     : bi("Mai 2021",     "May 2021"),
        "bullets" : [
            bi(
                "Optimisation du processus d'accueil et de départ des collaborateurs.",
                "Optimisation of the employee onboarding and offboarding process.",
            ),
            bi(
                "Formalisation des processus, PDCA, kits de communication.",
                "Process formalisation, PDCA methodology, communication kits.",
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
                "Data science, recherche opérationnelle, informatique.",
                "Data science, operations research, computer science.",
            ),
            bi(
                "Gestion de projet, sociologie, économie.",
                "Project management, sociology, economics.",
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
                "Systèmes de gestion d'entreprise (SAP), performance et prix de revient.",
                "Enterprise resource planning (SAP), performance and cost analysis.",
            ),
            bi("Data mining, machine learning.", "Data mining, machine learning."),
        ],
    },
    {
        "degree"  : "Classe Préparatoire PCSI / PC*",
        "school"  : "Lycée Champollion",
        "location": "Grenoble, France",
        "start"   : "2017",
        "end"     : "2019",
        "bullets" : [],
    },
]

# ══════════════════════════════════════════════════════════════
#  COMPÉTENCES
# ══════════════════════════════════════════════════════════════

SKILLS = [
    {
        "category": bi("Data & BI", "Data & BI"),
        "items"   : [
            "SQL (BigQuery)",
            "Python (Pandas, PySpark, Scikit-learn, TensorFlow)",
            "R (tidyr, dplyr, ggplot2)",
            "Power BI (DAX, M)",
            "IBM Cognos Analytics",
        ],
    },
    {
        "category": bi("ERP & Supply Chain", "ERP & Supply Chain"),
        "items"   : [
            "SAP (FI, CO, MM, PP, SD, APO)",
            "Manhattan WMS",
            "VSM · Kaizen · Lean Manufacturing",
            "Arena",
        ],
    },
    {
        "category": bi("Dev & Outils", "Dev & Tools"),
        "items"   : [
            "Git / GitHub (CI/CD)",
            "Java · OPL · UML",
            "MS Office avancé (Excel, Access, Project)",
            "VBA",
        ],
    },
    {
        "category": bi("Produit & Méthodes", "Product & Methods"),
        "items"   : [
            "Product Management",
            "Agile / Scrum",
            "UX/UI Design",
        ],
    },
]

# ══════════════════════════════════════════════════════════════
#  LANGUES
# ══════════════════════════════════════════════════════════════

LANGUAGES = [
    {
        "lang" : "Français",
        "level": bi("Langue maternelle", "Native"),
    },
    {
        "lang" : "Anglais / English",
        "level": bi(
            "C2 — TOEFL ITP 624, Cambridge Certificate",
            "C2 — TOEFL ITP 624, Cambridge Certificate",
        ),
    },
    {
        "lang" : "Español / Espagnol",
        "level": bi("B1/B2", "B1/B2"),
    },
]

# ══════════════════════════════════════════════════════════════
#  VIE ASSOCIATIVE & LEADERSHIP
# ══════════════════════════════════════════════════════════════

ASSOCIATIONS = [
    {
        "role"       : bi(
            "Président du Bureau des Sports",
            "President of the Sports Committee",
        ),
        "org"        : "Grenoble INP",
        "period"     : "2020 – 2021",
        "description": bi(
            "Management de 27 personnes pour animer la vie étudiante "
            "sur 1,5 an — budget géré : 25K€.",
            "Management of 27 people to drive student life over 18 months "
            "— budget managed: €25K.",
        ),
    },
    {
        "role"       : bi("Chef de projet – Collecte de fonds", "Project Lead – Fundraising"),
        "org"        : bi("Association scolaire", "School Association"),
        "period"     : "2018 – 2019",
        "description": bi(
            "Organisation de collectes de fonds pour deux voyages scolaires.",
            "Organisation of fundraising campaigns for two school trips.",
        ),
    },
]

# ══════════════════════════════════════════════════════════════
#  CENTRES D'INTÉRÊT
# ══════════════════════════════════════════════════════════════

INTERESTS = [
    bi(
        "Musique & Art (guitariste et bassiste autodidacte)",
        "Music & Art (self-taught guitarist and bassist)",
    ),
    bi(
        "Ski (10 ans de compétition en club)",
        "Skiing (10 years of club competition)",
    ),
    bi(
        "Volleyball (compétitions interuniversitaires)",
        "Volleyball (interuniversity competitions)",
    ),
    bi(
        "Force athlétique (niveau régional)",
        "Powerlifting (regional level)",
    ),
]