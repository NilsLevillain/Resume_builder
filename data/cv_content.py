"""
🖊  CV — Bilingue FR / EN
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
    "title"   : bi("Product Owner Analytics @ L'Oréal",
                   "Product Owner Analytics @ L'Oréal"),
    "email"   : "levillain.nils@gmail.com",
    "phone"   : "+33 06 69 56 69 37",
    "location": "Paris, France",
    "linkedin": "linkedin.com/in/nils-levillain",
    "github"  : "github.com/nils-levillain",
    "photo" : "data/assets/photo.jpg",
}

# ══════════════════════════════════════════════════════════════
#  RÉSUMÉ
# ══════════════════════════════════════════════════════════════

SUMMARY = bi(
    fr=(
        "Product Owner & Tech Project Manager avec 3+ ans chez L'Oréal. "
        "Pilotage d'une suite de 10+ produits analytiques mondiaux (Supply Chain) — "
        "200+ utilisateurs actifs, NPS 50+ — au service de l'efficacité opérationnelle, "
        "de la réduction des coûts et de la durabilité. "
        "Expertise : cloud (GCP), IA/ML, UX/UI data-driven et coordination "
        "multi-parties prenantes à l'échelle globale."
    ),
    en=(
        "Product Owner & Tech Project Manager with 3+ years at L'Oréal. "
        "Driving a suite of 10+ global analytics products (Supply Chain) — "
        "200+ active users, NPS 50+ — spanning operational efficiency, "
        "cost reduction and sustainability. "
        "Expertise: cloud (GCP), AI/ML, data-driven UX/UI, "
        "and global multi-stakeholder coordination."
    ),
)

# ══════════════════════════════════════════════════════════════
#  EXPÉRIENCES
# ══════════════════════════════════════════════════════════════

EXPERIENCE = [
    {
        "title"  : bi("Product Owner Analytics – Global Supply Chain",
                      "Product Owner Analytics – Global Supply Chain"),
        "company": "L'Oréal",
        "start"  : bi("Janv. 2024",  "Jan. 2024"),
        "end"    : bi("Aujourd'hui", "Present"),
        "bullets": [
            bi(
                f"Suite de {kpi('10+ produits')} analytiques mondiaux (Fulfillment) — "
                f"{kpi('200+ utilisateurs')}, {kpi('NPS 50+')} ; "
                f"définition roadmap, priorisation produit en environnement agile.",
                f"Suite of {kpi('10+ analytics products')} for global Supply Chain "
                f"(Fulfillment) — {kpi('200+ users')}, {kpi('NPS 50+')}; "
                f"roadmap definition & product prioritisation in agile environment.",
            ),
            bi(
                f"Coordination multi-niveaux : {bold('5+ business owners')}, "
                f"{bold('2 product leads')}, {bold('10+ développeurs')} + "
                f"top management & C-level pour comités de pilotage, arbitrages budget & stratégie.",
                f"Multi-level coordination: {bold('5+ business owners')}, "
                f"{bold('2 product leads')}, {bold('10+ developers')} + "
                f"top management & C-level executives for steering committees, budget & strategic decisions.",
            ),
            bi(
                f"Discovery & {bold('UX/UI')} : entretiens utilisateurs cross-zones/fonctions ; "
                f"dashboards action-oriented & user-centric ; design system partagé "
                f"→ réduction des coûts & délais de développement.",
                f"Discovery & {bold('UX/UI')}: cross-zone/function user interviews; "
                f"action-oriented & user-centric dashboards; shared design system "
                f"→ reduced development costs & time.",
            ),
            bi(
                f"IA : {bold('POCs IA/ML')} (demand forecasting, allocation de stock optimale, …), "
                f"initiative {bold('GenBI / Talk with your Data')}, mélangeant SSBI & compagnons; "
                f"Cloud : GCP (BigQuery, Architecture Médaillon), SQL complexe, data modelling.",
                f"AI: {bold('AI/ML POCs')} (demand forecasting, optimal stock allocation, …), "
                f"{bold('GenBI / Talk with your Data')} initiative, mixing SSBI & companions; "
                f"Cloud: GCP (BigQuery, Medallion Architecture), complex SQL, data modelling.",
            ),
            bi(
                f"Change management & adoption : dashboard de suivi NPS & adoption, "
                f"training kits, webinaires ; coordination partenaires tech internes & externes.",
                f"Change management & adoption: NPS & adoption monitoring dashboard, "
                f"training kits, webinars; internal & external tech partner coordination.",
            ),
            bi(
                f"Promotion du rôle : communication groupe au niveau mondial "
                f"pour renforcer l'attractivité des métiers analytics Supply Chain.",
                f"Role promotion: group-level global communication "
                f"to increase attractivity of Supply Chain analytics roles.",
            ),
        ],
    },
    {
        "title"  : bi("Ingénieur Projets Supply Chain – WMS Key User",
                      "Supply Chain Project Engineer – WMS Key User"),
        "company": "L'Oréal",
        "start"  : bi("Sept. 2022", "Sept. 2022"),
        "end"    : bi("Déc. 2023",  "Dec. 2023"),
        "bullets": [
            bi(
                f"{bold('Business')} : configuration du WMS & tests fonctionnels "
                f"répondant à des angles morts opérationnels & stratégiques — "
                f"{kpi('+100 cas de test')} définis & exécutés.",
                f"{bold('Business')}: WMS configuration & functional tests "
                f"addressing operational & strategic blind spots — "
                f"{kpi('100+')} test cases defined & executed.",
            ),
            bi(
                f"{bold('Data & IT')} : {kpi('+20 rapports BI')} répondant à des "
                f"questions opérationnelles clés ; animation communauté dev Europe ; "
                f"migration de données SAP → Manhattan.",
                f"{bold('Data & IT')}: {kpi('20+')} BI reports answering key "
                f"operational questions; European developer community leadership; "
                f"SAP → Manhattan data migration.",
            ),
            bi(
                f"{bold('Change Management')} : documentation complète, "
                f"{kpi('~50h')} de formation opérateurs & chefs d'équipe, "
                f"accompagnement au déploiement & optimisation continue.",
                f"{bold('Change Management')}: full documentation, "
                f"{kpi('~50h')} training for operators & team leaders, "
                f"deployment support & continuous optimisation.",
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
                f"Responsabilités senior (fin de stage) : planification, appro & "
                f"logistique catalogue promo Garnier — {kpi('99% service rate')}.",
                f"Senior responsibilities (end of internship): planning, procurement "
                f"& logistics for Garnier's promo catalogue — {kpi('99% service rate')}.",
            ),
            bi(
                f"BI & {bold('stakeholder management')} : amélioration de rapports "
                f"de suivi ; réduction {kpi('−20%')} des écarts de stock copacker.",
                f"BI & {bold('stakeholder management')}: improved monitoring reports; "
                f"{kpi('−20%')} stock gap reduction with co-packer.",
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
            "Engineering Degree · Supply Chain, Data & Information Systems",
        ),
        "school" : "Grenoble INP – Génie Industriel",
        "start"  : "2019",
        "end"    : "2022",
        "bullets": [
            bi(
                "Grande école · Organisation industrielle, Data Science, "
                "Recherche Opérationnelle, Gestion de Projet.",
                "Grande École · Industrial organisation, Data Science, "
                "Operations Research, Project Management.",
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
                "ERP (SAP), Data Mining, Machine Learning, Optimisation.",
                "ERP (SAP), Data Mining, Machine Learning, Optimisation.",
            ),
        ],
    },
]

# ══════════════════════════════════════════════════════════════
#  COMPÉTENCES
# ══════════════════════════════════════════════════════════════

SKILLS = [
    {
        "category": bi("Gestion de Projet", "Project Delivery"),
        "items"   : [
            "Agile / Scrum",
            "Stakeholder Management",
            "UX/UI Design",
            "Change Management",
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
            "MS Office (Excel, PowerPoint)",
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
#  VIE ASSOCIATIVE & LEADERSHIP
# ══════════════════════════════════════════════════════════════

ASSOCIATIONS = [
    {
        "role"       : bi("Délégué — One Young World Summit",
                          "Delegate — One Young World Summit"),
        "org"        : "One Young World",
        "period"     : "2024 – 2025",
        "description": bi(
            "Sommet mondial RSE & leadership responsable à l'international ; "
            "programme de 9 mois pour devenir acteur du changement.",
            "Global sustainability & ethics summit abroad; "
            "9-month programme to become a responsible leader.",
        ),
    },
    {
        "role"       : bi(
            "Président du Bureau des Sports — 27 personnes managées, budget 25K€",
            "President of Sports Committee — 27 people managed, €25K budget",
        ),
        "org"        : "Grenoble INP",
        "period"     : "2020 – 2021",
        "description": bi("", ""),
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