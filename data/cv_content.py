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
    "photo"   : "data/assets/photo.jpg",
}

# ══════════════════════════════════════════════════════════════
# RÉSUMÉ — méthodologie end-to-end, domaine Fulfillment, pas de KPIs
# ══════════════════════════════════════════════════════════════

SUMMARY = bi(
    fr=(
        "Product Manager avec une maîtrise complète du cycle produit : "
        "discovery utilisateur, prototypage, construction, déploiement global "
        "et mesure de l'adoption. "
        "Spécialiste du domaine Fulfillment (Transport, Douane, Entrepôts) "
        "au sein d'organisations mondiales matricielles à forte complexité, "
        "délais courts et exigence budgétaire élevée. "
        "Expert des trois axes qui structurent la performance Supply Chain : "
        "coûts opérationnels, conformité et performance, durabilité. "
        "Passionné par les produits qui transforment durablement les pratiques "
        "dans des environnements à haute exigence."
    ),
    en=(
        "Product Manager with full-cycle ownership: user discovery, prototyping, "
        "build, global deployment and adoption measurement. "
        "Specialist in the Fulfillment domain (Transport, Customs, Warehouses) "
        "within global matrixed organisations operating under high complexity, "
        "tight timelines and budget accountability. "
        "Expert across the three axes structuring Supply Chain performance: "
        "operational costs, compliance and performance, sustainability. "
        "Passionate about products that drive lasting behavioral change "
        "in high-stakes, fast-paced environments."
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
                f"Propriétaire end-to-end d'une suite de {kpi('10+ produits')} analytiques "
                f"mondiaux (Fulfillment : Transport, Douane, Entrepôts) ; "
                f"{kpi('200+ utilisateurs')}, {kpi('NPS 50+')} ; pleine autonomie sur "
                f"{bold('vision, stratégie et roadmap')} pilotée par les priorités business.",
                f"End-to-end ownership of a suite of {kpi('10+ analytics products')} "
                f"for global Fulfillment (Transport, Customs, Warehouses); "
                f"{kpi('200+ users')}, {kpi('NPS 50+')}; full autonomy over "
                f"{bold('product vision, strategy and roadmap')} shaped by business priorities.",
            ),
            bi(
                f"{bold('Discovery continue')} : 30+ interviews utilisateurs "
                f"cross-zones/fonctions ; prototypage {bold('Figma')} et POCs IA avant "
                f"construction ; hypothèses validées ou abandonnées sur la base des retours, "
                f"dont des pages de dashboards entièrement repensées après feedback utilisateur.",
                f"{bold('Continuous discovery')}: 30+ user interviews cross-zone/function; "
                f"{bold('Figma')} prototyping and AI POCs before building; "
                f"hypotheses validated or discarded based on user feedback, "
                f"including full dashboard redesigns after invalidating initial directions.",
            ),
            bi(
                f"{bold('Impact business et durabilité')} : calculateur CO2 Transport "
                f"({kpi('−50% de fret aérien')}) et alignement de {kpi('7 zones mondiales')} "
                f"sur les mêmes méthodes de calcul (coûts DC, performance, CO2) ; "
                f"outil No Waste (ML forecasting + optimisation) : {kpi('2M€/an projeté')} "
                f"(CA préservé, réduction FTEs, destructions évitées), ROI < 1 an.",
                f"{bold('Business and sustainability impact')}: CO2 Transport calculator "
                f"({kpi('−50% air freight')}) and alignment of {kpi('7 global zones')} "
                f"on shared calculation methods (DC costs, performance, CO2); "
                f"No Waste tool (ML forecasting + optimisation): {kpi('2M€/year projected')} "
                f"(preserved revenue, FTE reduction, avoided destructions), ROI < 1 year.",
            ),
            bi(
                f"{bold('Changement comportemental durable')} : les utilisateurs ont modifié "
                f"leur façon de saisir les données, intégré les analytics dans leurs revues "
                f"annuelles pour discuter des bonus et piloter le business quotidiennement ; "
                f"adoption mesurée via dashboard NPS, training kits et webinaires.",
                f"{bold('Lasting behavioral change')}: users changed how they input data, "
                f"embedded analytics into year-end reviews to discuss performance bonuses "
                f"and manage business daily; adoption tracked via NPS dashboard, "
                f"training kits and webinars.",
            ),
            bi(
                f"{bold('Innovation')} : initié GenBI / {bold('Talk with your Data')} : "
                f"hypothèse issue de la user discovery pour permettre aux utilisateurs métier "
                f"de répondre seuls à leurs questions business sans dépendance IT ; "
                f"de l'interview utilisateur au prototype IA fonctionnel.",
                f"{bold('Innovation')}: championed GenBI / {bold('Talk with your Data')}: "
                f"hypothesis from user discovery to enable business users to answer their "
                f"own questions without IT dependency; "
                f"from user interview to working AI prototype.",
            ),
            bi(
                f"Coordination : {bold('5+ business owners')}, {bold('10+ développeurs')}, "
                f"C-level pour comités de pilotage et arbitrages budgétaires "
                f"dans un environnement matriciel mondial.",
                f"Coordination: {bold('5+ business owners')}, {bold('10+ developers')}, "
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
                f"Piloté la transformation {bold('SAP vers Manhattan')} : "
                f"identification des angles morts opérationnels et stratégiques, "
                f"programme de changement défini et exécuté : {kpi('+100 cas de test')}, "
                f"productivité et conformité améliorées et mesurées.",
                f"Led {bold('SAP to Manhattan')} WMS transformation: "
                f"identified operational and strategic blind spots, "
                f"defined and executed the change programme: {kpi('100+ test cases')}, "
                f"productivity and compliance improved and measured.",
            ),
            bi(
                f"{bold('Données et visibilité')} : {kpi('+20 rapports BI')} répondant à "
                f"des questions clés sur les coûts DC, la productivité et la conformité, "
                f"précédemment indisponibles à la direction.",
                f"{bold('Data and visibility')}: {kpi('20+ BI reports')} answering key "
                f"questions on DC costs, productivity and compliance; "
                f"insights previously unavailable to management.",
            ),
            bi(
                f"{bold('Changement comportemental')} : documentation complète, "
                f"{kpi('~50h de formation')} opérateurs et chefs d'équipe ; "
                f"adoption durable des nouvelles méthodes de travail post-déploiement.",
                f"{bold('Behavioral change')}: full documentation, "
                f"{kpi('~50h training')} for operators and team leaders; "
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
                f"Responsabilités senior (fin de stage) : planification, appro et logistique "
                f"du catalogue promo Garnier ({kpi('99% service rate')}).",
                f"Senior responsibilities (end of internship): planning, procurement and "
                f"logistics for Garnier's promo catalogue ({kpi('99% service rate')}).",
            ),
            bi(
                f"BI et {bold('stakeholder management')} : rapports de suivi ayant permis "
                f"une réduction de {kpi('−20% des écarts de stock')} avec le copacker.",
                f"BI and {bold('stakeholder management')}: monitoring reports enabling "
                f"a {kpi('−20% stock gap')} reduction with the co-packer.",
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
# CLIFTON STRENGTHS
# ══════════════════════════════════════════════════════════════

STRENGTHS = [
    {
        "name"  : bi("Compétition", "Competition"),
        "domain": "Influencing",
        "color" : "#E87500",
    },
    {
        "name"  : bi("Réalisateur", "Achiever"),
        "domain": "Executing",
        "color" : "#7B2D8B",
    },
    {
        "name"  : bi("Apprenant", "Learner"),
        "domain": "Strategic Thinking",
        "color" : "#00875A",
    },
]

# ══════════════════════════════════════════════════════════════
# LANGUES
# ══════════════════════════════════════════════════════════════

LANGUAGES = [
    {"lang": "Français",           "level": bi("Langue maternelle", "Native")},
    {"lang": "Anglais / English",  "level": bi("C2 · TOEFL ITP 624", "C2 · TOEFL ITP 624")},
    {"lang": "Español / Espagnol", "level": bi("B1/B2", "B1/B2")},
]

# ══════════════════════════════════════════════════════════════
# VIE ASSOCIATIVE & LEADERSHIP
# ══════════════════════════════════════════════════════════════

ASSOCIATIONS = [
    {
        "role"       : bi("Délégué", "Delegate"),
        "org"        : "One Young World",
        "period"     : "2024 – 2025",
        "description": bi(
            "Sommet mondial RSE et leadership responsable ; "
            "programme 9 mois pour construire un impact positif durable.",
            "Global sustainability and responsible leadership summit; "
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