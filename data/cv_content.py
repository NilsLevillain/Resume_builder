"""
CV — Bilingue FR / EN
Adapté pour : Tech Product Owner - Beauty Tech Agentic Platform @ L'Oréal
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
        "Analytics Product Owner | Global Supply Chain @ L'Oréal",
        "Analytics Product Owner | Global Supply Chain @ L'Oréal",
    ),
    "email"   : "levillain.nils@gmail.com",
    "phone"   : "+33 06 69 56 69 37",
    "location": "Paris, France",
    "linkedin": "linkedin.com/in/nils-levillain",
    "github"  : "github.com/NilsLevillain",
    "photo"   : "data/assets/photo.jpg",
}

# ══════════════════════════════════════════════════════════════
# RÉSUMÉ
# ══════════════════════════════════════════════════════════════
SUMMARY = bi(
    fr=(
        "Analytics Product Owner avec 3+ ans d'expérience chez L'Oréal dans la gestion "
        "du cycle de vie complet de produits data et IA. "
        "Expert en définition de vision stratégique, construction de roadmaps techniques "
        "et pilotage d'équipes agiles dans un environnement cloud et BI (GCP, PBI). "
        "Reconnu pour ma capacité à traduire des besoins métier complexes en solutions "
        "technologiques innovantes (Agentic AI, Data Viz / Simulation) et à fédérer des "
        "équipes mondiales (ingénieurs IT, designers, data scientists, stakeholders). "
        "Passionné par la conduite du changement et l'adoption de l'IA à grande échelle."
    ),
    en=(
        "Analytics Product Owner with 3+ years at L'Oréal managing the entire lifecycle "
        "of data and AI products. "
        "Expert in defining strategic vision, building technical roadmaps, "
        "and leading agile teams in a cloud & BI environment (GCP, PBI). "
        "Recognized for translating complex business needs into innovative "
        "technological solutions (Agentic AI, Data Viz / Simulation) and aligning global "
        "teams (IT engineers, designers, data scientists, stakeholders). "
        "Passionate about driving adoption and upskilling communities for AI at scale."
    ),
)

# ══════════════════════════════════════════════════════════════
# EXPÉRIENCES
# ══════════════════════════════════════════════════════════════
EXPERIENCE = [
    {
        "title"  : bi(
            "Analytics Product Owner : Global Supply Chain",
            "Analytics Product Owner : Global Supply Chain",
        ),
        "company": "L'Oréal",
        "start"  : bi("Janv. 2024", "Jan. 2024"),
        "end"    : bi("Aujourd'hui", "Present"),
        "bullets": [
            bi(
                f"Vision et {bold('stratégie produit')} : propriétaire end-to-end d'une suite de {kpi('10+ produits')} ; "
                f"définition de la {bold('roadmap technique')} et priorisation du backlog (SNOW) "
                f"en alignement avec les ambitions globales de L'Oréal.",
                f"Product vision and {bold('strategy')}: end-to-end ownership of a suite of {kpi('10+ products')}; "
                f"defined the {bold('technical roadmap')} and prioritized the backlog (SNOW) "
                f"in alignment with L'Oréal's global ambitions.",
            ),
            bi(
                f"Innovation et {bold('Agentic AI')} : préparation de produits basés sur les LLMs "
                f"(modèles sémantiques, frameworks de test, agents conversationnels) en collaboration avec l'IT engineering ; "
                f"pilotage des débuts de l'initiative GenBI / Talk with your Data pour {kpi('200+ utilisateurs')} mondiaux.",
                f"Innovation and {bold('Agentic AI')}: preparing LLM-based products "
                f"(semantic models, test frameworks, talk to your data agents) in collaboration with IT engineering; "
                f"spearheaded the beginning of GenBI / Talk with your Data initiative for {kpi('200+ global users')}.",
            ),
            bi(
                f"Technologie cloud : conception et déploiement de solutions scalables sur "
                f"{bold('Google Cloud (GCP / BigQuery)')} ; traduction de besoins complexes en "
                f"exigences claires pour les équipes de développement.",
                f"Cloud technology: designed and deployed scalable solutions on "
                f"{bold('Google Cloud (GCP / BigQuery)')}; translated complex business needs into "
                f"clear requirements for development teams.",
            ),
            bi(
                f"Collaboration globale : pont quotidien entre l'IT et le business (Global et 7 Zones) ; "
                f"gestion des parties prenantes à tous les niveaux hiérarchiques, incluant le {bold('C-level')}.",
                f"Global collaboration: daily bridge between IT and business (Global and 7 Zones); "
                f"managed stakeholders at all hierarchical levels, including {bold('C-level')} executives.",
            ),
            bi(
                f"Adoption et upskilling : plan d'engagement garantissant l'adoption des plateformes ({kpi('NPS 50+')}) ; "
                f"animation de {bold('sharing sessions')} (frameworks webapps, IA pour PM) pour la "
                f"montée en compétences des collègues sur les nouvelles initiatives tech.",
                f"Adoption and upskilling: engagement plan driving platform adoption ({kpi('NPS 50+')}); "
                f"led {bold('sharing sessions')} (webapp frameworks, AI for PMs) to "
                f"upskill colleagues on new tech initiatives.",
            ),
        ],
    },
    {
        "title"  : bi(
            "WMS Tech Project Lead : Transformation & Adoption",
            "WMS Tech Project Lead : Transformation & Adoption",
        ),
        "company": "L'Oréal",
        "start"  : bi("Sept. 2022", "Sept. 2022"),
        "end"    : bi("Déc. 2023", "Dec. 2023"),
        "bullets": [
            bi(
                f"Pilotage de projet Agile : exécution d'un programme de transformation système "
                f"majeur (SAP vers Manhattan) incluant design, configuration, {kpi('100+ cas de test')} validés "
                f"et conformité technique assurée.",
                f"Agile project management: executed a major system transformation program "
                f"(SAP to Manhattan) with design, configuration, {kpi('100+ test cases')} validated "
                f"and technical compliance ensured.",
            ),
            bi(
                f"Stakeholder management : alignement des équipes IT, opérations et partenaires "
                f"externes pour délivrer des produits de haute qualité dans des délais courts.",
                f"Stakeholder management: aligned IT teams, operations, and external partners "
                f"to deliver high-quality products within tight deadlines.",
            ),
            bi(
                f"Conduite du changement : rédaction de la documentation technique et animation de "
                f"{kpi('~50h de formation')} pour garantir l'adoption et la satisfaction autour des nouveaux outils "
                f"afin de générer de l'impact business.",
                f"Change management: drafted technical documentation and led "
                f"{kpi('~50h of training')} to guarantee the adoption & satisfaction of new tools "
                f"to drive business impact.",
            ),
        ],
    },
    {
        "title"  : bi("Copacking Planner", "Copacking Planner"),
        "company": "L'Oréal",
        "start"  : bi("Janv. 2022", "Jan. 2022"),
        "end"    : bi("Juil. 2022", "Jul. 2022"),
        "bullets": [
            bi(
                f"Performance opérationnelle : planification et logistique des catalogues promotionnels, "
                f"atteignant un {kpi('taux de service de 99%')}.",
                f"Operational performance: managed planning and logistics for promotional catalogues, "
                f"achieving a {kpi('99% service rate')}.",
            ),
            bi(
                f"Analyse de données : création de dashboards de suivi permettant une "
                f"réduction de {kpi('20% des écarts')} via une collaboration étroite avec les partenaires.",
                f"Data analysis: built monitoring dashboards enabling a "
                f"{kpi('20% gap reduction')} through close collaboration with partners.",
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
            "Diplôme d'Ingénieur : Data, Systèmes d'Information & Supply Chain",
            "Engineering Degree: Data, Information Systems & Supply Chain",
        ),
        "school" : "Grenoble INP – Génie Industriel",
        "start"  : "2019",
        "end"    : "2022",
        "bullets": [
            bi(
                "Spécialisation : Data Science, Recherche Opérationnelle, Gestion de Projet Tech.",
                "Specialization: Data Science, Operations Research, Tech Project Management.",
            ),
        ],
    },
    {
        "degree" : bi(
            "Échange Académique : Informatique & Génie Industriel",
            "Academic Exchange: Computer Science & Industrial Engineering",
        ),
        "school" : "École Polytechnique de Montréal",
        "start"  : "2021",
        "end"    : "2022",
        "bullets": [
            bi(
                "Machine Learning, Data Mining, Optimisation.",
                "Machine Learning, Data Mining, Optimization.",
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
            "Product Vision & Strategy",
            "Technical Roadmap",
            "Agile / Scrum",
            "Continuous Discovery",
        ],
    },
    {
        "category": bi("Technology Acumen", "Technology Acumen"),
        "items"   : [
            "Google Cloud (GCP)",
            "Agentic AI & LLMs",
            "BigQuery / SQL",
            "Python (ML)",
        ],
    },
    {
        "category": bi("Adoption & Leadership", "Adoption & Leadership"),
        "items"   : [
            "Stakeholder Management",
            "Global Collaboration",
            "Upskilling & Training",
            "Change Management",
        ],
    },
]

# ══════════════════════════════════════════════════════════════
# FORCES (Fixes)
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
    {"lang": "Français", "level": bi("Langue maternelle", "Native")},
    {"lang": "English", "level": bi("C2 : TOEFL ITP 624", "C2: TOEFL ITP 624")},
    {"lang": "Spanish", "level": bi("B1/B2", "B1/B2")},
]

# ══════════════════════════════════════════════════════════════
# VIE ASSOCIATIVE
# ══════════════════════════════════════════════════════════════
ASSOCIATIONS = [
    {
        "role"       : bi("Délégué", "Delegate"),
        "org"        : "One Young World",
        "period"     : "2024 : 2025",
        "description": bi(
            "Sommet mondial RSE et leadership responsable.",
            "Global sustainability and responsible leadership summit.",
        ),
    },
    {
        "role"       : bi("Président du Bureau des Sports", "President of Sports Committee"),
        "org"        : "Grenoble INP",
        "period"     : "2020 : 2021",
        "description": bi(
            "27 personnes managées, budget de 25 000 euros.",
            "27 people managed, 25,000 euros budget.",
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