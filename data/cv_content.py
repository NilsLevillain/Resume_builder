"""
✅  CV — Bilingue FR / EN
    Adapté pour : Product Manager @ Riot (cybersecurity awareness)
"""

def bi(fr: str, en: str) -> dict:
    return {"fr": fr, "en": en}

def kpi(text: str) -> str:
    return f'<span class="kpi-badge">{text}</span>'

def bold(text: str) -> str:
    return f'<strong>{text}</strong>'

# ══════════════════════════════════════════════════════════════
# INFORMATIONS PERSONNELLES
# ══════════════════════════════════════════════════════════════

PERSONAL = {
    "name"    : "Nils Levillain",
    "title"   : bi(
        "Product Manager | Discovery & Innovation @ L'Oréal",
        "Product Manager | Discovery & Innovation @ L'Oréal",
    ),
    "email"   : "levillain.nils@gmail.com",
    "phone"   : "+33 06 69 56 69 37",
    "location": "Paris, France",
    "linkedin": "linkedin.com/in/nils-levillain",
    "github"  : "github.com/NilsLevillain",
    "photo": "data/assets/photo.jpg",
}

# ══════════════════════════════════════════════════════════════
# RÉSUMÉ
# ══════════════════════════════════════════════════════════════

SUMMARY = bi(
    fr=(
        "Product Manager orienté discovery et innovation avec 3+ ans chez L'Oréal. "
        "Propriétaire end-to-end de produits à impact mesurable : −50% de fret aérien "
        "via un calculateur CO2, ROI projeté de 2M€/an sur un outil d'optimisation IA. "
        "A conduit un changement comportemental durable chez 200+ utilisateurs — "
        "ils ont modifié leurs pratiques quotidiennes, leurs méthodes de saisie et "
        "utilisent les analytics pour piloter le business et leurs revues annuelles. "
        "Passionné par les produits qui transforment les comportements, "
        "convaincu que la cybersécurité est le défi organisationnel de notre génération."
    ),
    en=(
        "Discovery and innovation-driven Product Manager with 3+ years at L'Oréal. "
        "End-to-end ownership of products with measurable impact: −50% air freight "
        "via a CO2 calculator, 2M€/year projected ROI on an AI optimisation tool. "
        "Drove lasting behavioral change across 200+ users — they changed their daily "
        "habits, data input practices, and now use analytics to manage business "
        "performance and year-end reviews. "
        "Passionate about products that transform behaviors; convinced that "
        "cybersecurity is the defining organisational challenge of our generation."
    ),
)

# ══════════════════════════════════════════════════════════════
# EXPÉRIENCES
# ══════════════════════════════════════════════════════════════

EXPERIENCE = [
    {
        "title"  : bi(
            "Product Manager – Global Supply Chain Analytics",
            "Product Manager – Global Supply Chain Analytics",
        ),
        "company": "L'Oréal",
        "start"  : bi("Janv. 2024", "Jan. 2024"),
        "end"    : bi("Aujourd'hui", "Present"),
        "bullets": [
            bi(
                f"Propriétaire end-to-end d'une suite de {kpi('10+ produits')} analytiques mondiaux "
                f"(Supply Chain) — {kpi('200+ utilisateurs')}, {kpi('NPS 50+')} ; "
                f"pleine autonomie sur {bold('vision, stratégie et roadmap')}, "
                f"définie en continu selon les priorités business.",
                f"End-to-end ownership of a suite of {kpi('10+ analytics products')} "
                f"for global Supply Chain — {kpi('200+ users')}, {kpi('NPS 50+')}; "
                f"full autonomy over {bold('product vision, strategy and roadmap')}, "
                f"continuously shaped by business priorities.",
            ),
            bi(
                f"{bold('Discovery continue')} : 30+ interviews utilisateurs cross-zones/fonctions ; "
                f"prototypage {bold('Figma')} et POCs IA avant construction ; "
                f"hypothèses validées ou abandonnées sur la base des retours — "
                f"dont des pages de dashboards entièrement repensées après feedback utilisateur.",
                f"{bold('Continuous discovery')}: 30+ user interviews cross-zone/function; "
                f"{bold('Figma')} prototyping and AI POCs before building; "
                f"hypotheses validated or discarded based on user feedback — "
                f"including full dashboard redesigns after invalidating initial directions.",
            ),
            bi(
                f"{bold('Impact business & durabilité')} : calculateur CO2 Transport → "
                f"{kpi('−50% de fret aérien')} et alignement de {kpi('7 zones mondiales')} "
                f"sur les mêmes méthodes de calcul (performance DC, coûts DC, CO2 transport) ; "
                f"outil No Waste (ML forecasting + optimisation) → {kpi('2M€/an projeté')} "
                f"(CA préservé, réduction FTEs, destructions évitées), ROI < 1 an.",
                f"{bold('Business & sustainability impact')}: CO2 Transport calculator → "
                f"{kpi('−50% air freight')} and alignment of {kpi('7 global zones')} "
                f"on shared calculation methods (DC performance, DC costs, CO2 transport); "
                f"No Waste tool (ML forecasting + optimisation) → {kpi('2M€/year projected')} "
                f"(preserved revenue, FTE reduction, avoided destructions), ROI < 1 year.",
            ),
            bi(
                f"{bold('Changement comportemental durable')} : les utilisateurs ont modifié "
                f"leur façon de saisir les données, intégré les analytics dans leurs revues "
                f"annuelles pour discuter des bonus et piloter le business quotidiennement — "
                f"adoption mesurée via dashboard NPS, training kits et webinaires.",
                f"{bold('Lasting behavioral change')}: users changed how they input data, "
                f"embedded analytics into year-end reviews to discuss performance bonuses "
                f"and manage business daily — adoption tracked via NPS dashboard, "
                f"training kits and webinars.",
            ),
            bi(
                f"{bold('Innovation')} : initié GenBI / {bold('Talk with your Data')} — "
                f"hypothèse issue de la user discovery : permettre aux utilisateurs métier "
                f"de répondre seuls à leurs questions business sans dépendance IT ; "
                f"de l'interview utilisateur au prototype IA fonctionnel.",
                f"{bold('Innovation')}: championed GenBI / {bold('Talk with your Data')} — "
                f"hypothesis from user discovery: enable business users to answer their "
                f"own questions without IT dependency; "
                f"from user interview to working AI prototype.",
            ),
            bi(
                f"Coordination {bold('5+ business owners')}, {bold('10+ développeurs')}, "
                f"C-level pour comités de pilotage et arbitrages budgétaires "
                f"dans un environnement matriciel mondial.",
                f"Aligned {bold('5+ business owners')}, {bold('10+ developers')}, "
                f"C-level executives for steering committees and budget decisions "
                f"in a global, matrixed organisation.",
            ),
        ],
    },
    {
        "title"  : bi(
            "Chef de Projet – Transformation WMS & Productivité DC",
            "Project Lead – WMS Transformation & DC Productivity",
        ),
        "company": "L'Oréal",
        "start"  : bi("Sept. 2022", "Sept. 2022"),
        "end"    : bi("Déc. 2023", "Dec. 2023"),
        "bullets": [
            bi(
                f"Piloté la transformation {bold('SAP → Manhattan')} : identifié les angles "
                f"morts opérationnels et stratégiques, défini le programme de changement — "
                f"{kpi('+100 cas de test')} exécutés, productivité et conformité "
                f"améliorées et mesurées.",
                f"Led {bold('SAP → Manhattan')} WMS transformation: identified operational "
                f"& strategic blind spots, defined the change programme — "
                f"{kpi('100+ test cases')} executed, productivity and compliance "
                f"improved and measured.",
            ),
            bi(
                f"{bold('Données & visibilité')} : {kpi('+20 rapports BI')} répondant à des "
                f"questions clés sur les coûts DC, la productivité et la conformité — "
                f"informations précédemment indisponibles à la direction.",
                f"{bold('Data & visibility')}: {kpi('20+ BI reports')} answering key questions "
                f"on DC costs, productivity and compliance — insights previously "
                f"unavailable to management.",
            ),
            bi(
                f"{bold('Changement comportemental')} : documentation complète, "
                f"{kpi('~50h de formation')} opérateurs & chefs d'équipe ; "
                f"adoption durable des nouvelles méthodes de travail post-déploiement.",
                f"{bold('Behavioral change')}: full documentation, "
                f"{kpi('~50h training')} for operators & team leaders; "
                f"sustained adoption of new ways of working post-deployment.",
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
                f"Responsabilités senior (fin de stage) : planification, appro & logistique "
                f"catalogue promo Garnier — {kpi('99% service rate')}.",
                f"Senior responsibilities (end of internship): planning, procurement & "
                f"logistics for Garnier's promo catalogue — {kpi('99% service rate')}.",
            ),
            bi(
                f"BI & {bold('stakeholder management')} : rapports de suivi → "
                f"réduction {kpi('−20% des écarts de stock')} avec le copacker.",
                f"BI & {bold('stakeholder management')}: monitoring reports → "
                f"{kpi('−20% stock gap')} reduction with co-packer.",
            ),
        ],
    },
]

# ══════════════════════════════════════════════════════════════
# FORMATION
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
                "Grande École · Data Science, Recherche Opérationnelle, Gestion de Projet.",
                "Grande École · Data Science, Operations Research, Project Management.",
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
                "ERP (SAP), Data Mining, Machine Learning.",
                "ERP (SAP), Data Mining, Machine Learning.",
            ),
        ],
    },
]

# ══════════════════════════════════════════════════════════════
# COMPÉTENCES
# ══════════════════════════════════════════════════════════════

SKILLS = [
    {
        "category": bi("Product Management", "Product Management"),
        "items"   : [
            "Discovery & User Research",
            "Product Strategy & Roadmap",
            "Hypothesis Testing & Figma",
            "Go-to-Market & Adoption",
            "Behavioral Change",
        ],
    },
    {
        "category": bi("Data & IA", "Data & AI"),
        "items"   : [
            "GCP (BigQuery)",
            "SQL",
            "Python (ML)",
            "Power BI (DAX)",
        ],
    },
    {
        "category": bi("Méthodes", "Methods"),
        "items"   : [
            "Agile / Scrum",
            "Change Management",
            "Stakeholder Alignment",
        ],
    },
]

# ══════════════════════════════════════════════════════════════
# LANGUES
# ══════════════════════════════════════════════════════════════

LANGUAGES = [
    {"lang": "Français",           "level": bi("Langue maternelle", "Native")},
    {"lang": "Anglais / English",  "level": bi("C2 — TOEFL ITP 624", "C2 — TOEFL ITP 624")},
    {"lang": "Español / Espagnol", "level": bi("B1/B2", "B1/B2")},
]

# ══════════════════════════════════════════════════════════════
# VIE ASSOCIATIVE & LEADERSHIP
# ══════════════════════════════════════════════════════════════

ASSOCIATIONS = [
    {
        "role"       : bi("Délégué — One Young World",
                          "Delegate — One Young World"),
        "org"        : "One Young World",
        "period"     : "2024 – 2025",
        "description": bi(
            "Sommet mondial RSE & leadership responsable ; "
            "programme 9 mois pour construire un impact positif durable.",
            "Global sustainability & responsible leadership summit; "
            "9-month programme to build lasting positive impact.",
        ),
    },
    {
        "role"       : bi("Président du Bureau des Sports",
                          "President of Sports Committee"),
        "org"        : "Grenoble INP",
        "period"     : "2020 – 2021",
        "description": bi(
            "27 personnes managées, budget géré : 25K€.",
            "27 people managed, €25K budget.",
        ),
    },
]

# ══════════════════════════════════════════════════════════════
# INTÉRÊTS
# ══════════════════════════════════════════════════════════════

INTERESTS = [
    bi("Musique & Art (guitariste et bassiste autodidacte)",
       "Music & Art (self-taught guitarist and bassist)"),
    bi("Ski (10 ans de compétition en club)",
       "Skiing (10 years of club competition)"),
    bi("Force athlétique (niveau régional)",
       "Powerlifting (regional level)"),
]