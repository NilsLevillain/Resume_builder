# 📄 CV Generator — ATS-friendly · Bilingue · GitHub Pages

Générateur de CV professionnel en HTML et PDF, maintenu depuis un seul fichier de données.

🌐 **CV en ligne** → à compléter après activation GitHub Pages

---

## ✨ Fonctionnalités

| Fonctionnalité | Détail |
|---|---|
| 🌍 Bilingue FR / EN | Un seul fichier de données, deux CVs générés |
| 🌙 Dark / Light mode | Toggle avec mémorisation dans le navigateur |
| 📐 Layout 2 colonnes | Sidebar navy + zone principale avec cartes |
| 🏷 Skill tags | Badges arrondis dans la sidebar |
| 📊 KPI badges | Chiffres clés mis en valeur (fond ambre) |
| 🤖 ATS-friendly | Expérience en premier dans le HTML, balises sémantiques |
| 📄 Export PDF | Multi-backend : Playwright → Chrome/Edge → xhtml2pdf |
| 🚀 GitHub Pages | Déploiement automatique via GitHub Actions |

---

## 🗂 Architecture

- `cv_project/`
  - `.github/workflows/generate.yml` — Auto-génération au push sur main
  - `data/` — 🖊 **SEUL DOSSIER À MODIFIER**
    - `__init__.py`
    - `cv_config.py` — Couleurs, police, sections actives
    - `cv_content.py` — Tout le contenu CV (FR + EN)
  - `src/` — ⚙ Moteur de génération, ne pas modifier
    - `__init__.py`
    - `styles.py` — Design system CSS + JS toggle dark mode
    - `builder.py` — Constructeurs HTML par section (2 colonnes)
    - `exporter.py` — Export HTML + PDF (multi-backend)
  - `docs/` — 📁 Généré automatiquement par `generate.py`
    - `index.html` — CV EN, page d'accueil GitHub Pages
    - `fr.html` — CV FR
  - `generate.py` — 🚀 Point d'entrée
  - `requirements.txt`
  - `README.md`

---

## 🚀 Installation & utilisation

**1. Installer les dépendances** : `pip install -r requirements.txt`

**2. Installer Chromium pour le PDF** : `playwright install chromium`

**3. Générer le CV**

- FR + EN : `python generate.py`
- Français uniquement : `python generate.py --lang fr`
- Anglais uniquement : `python generate.py --lang en`

---

## ✏ Modifier le CV

**Règle d'or : ne modifier que `data/cv_content.py`**

### Helpers disponibles

| Helper | Usage |
|---|---|
| `bi("Texte FR", "English text")` | Champ bilingue — à utiliser pour tous les textes traduits |
| `kpi("+200")` | Badge ambre pour les chiffres clés et résultats |
| `bold("mot")` | Met un mot-clé en gras dans une bullet |

### Activer ou désactiver des sections

Dans `data/cv_config.py`, chaque section peut être mise à `True` ou `False` dans le dictionnaire `SECTIONS`.

### Changer les couleurs

Dans `data/cv_config.py`, modifier `ACCENT_COLOR` pour la couleur principale et `SIDEBAR_COLOR` pour le fond de la sidebar.

---

## 🤖 ATS Compatibility

L'expérience professionnelle est placée **en premier dans le HTML**, avant la sidebar. L'ATS lit le fichier HTML de manière linéaire et voit donc : Expériences → Formation → Compétences, dans le bon ordre, quel que soit l'affichage visuel en 2 colonnes.

| Règle ATS | Implémentation |
|---|---|
| Contenu principal en premier | `<main>` avant `<aside>` dans le HTML |
| Balises sémantiques | `header`, `main`, `aside`, `section`, `ul`, `li` |
| Texte pur, pas d'images | 100% HTML texte |
| Police universelle | Arial |
| Dates lisibles | `January 2024 – Present` |
| Labels standards EN | "Work Experience", "Education", "Skills" |

---

## 🚀 GitHub Pages — Déploiement

**Setup initial (une seule fois)**

1. Créer un repo GitHub et pusher le projet
2. Aller dans **Settings → Pages**
3. Source → `Deploy from a branch`
4. Branch : `main` · Folder : `/docs`
5. Sauvegarder — URL disponible en quelques minutes

**Workflow automatique**

À chaque push sur `main` modifiant `data/` ou `src/`, GitHub Actions installe les dépendances, exécute `python generate.py`, puis commit et push `docs/` automatiquement.

| Page | URL |
|---|---|
| CV EN (principal) | `https://USERNAME.github.io/REPO/` |
| CV FR | `https://USERNAME.github.io/REPO/fr.html` |

---

## 📦 Backends PDF

| Priorité | Backend | Qualité | Installation |
|---|---|---|---|
| 1 ⭐ | Playwright | Parfait | `pip install playwright` puis `playwright install chromium` |
| 2 | Chrome / Edge headless | Très bon | Automatique si navigateur déjà installé |
| 3 | xhtml2pdf | Correct | `pip install xhtml2pdf` |
| 4 | Manuel | Parfait | Ouvrir le HTML dans Chrome → `Ctrl+P` → Enregistrer en PDF |

---

## 🔄 Workflow recommandé

1. Modifier `data/cv_content.py`
2. Lancer `python generate.py --lang fr` pour prévisualiser
3. Ouvrir `docs/fr.html` dans le navigateur
4. `git add data/ docs/` → `git commit` → `git push`
5. GitHub Actions redéploie automatiquement ✅

---

## 📁 Fichiers générés

| Fichier | Description |
|---|---|
| `docs/index.html` | CV EN — page principale GitHub Pages |
| `docs/fr.html` | CV FR |
| `docs/cv_nils_levillain_en.pdf` | PDF EN |
| `docs/cv_nils_levillain_fr.pdf` | PDF FR |

> Ces fichiers sont générés automatiquement — ne pas les modifier manuellement.

---

*Généré avec ❤ — [Voir le repo](https://github.com/YOUR_USERNAME/YOUR_REPO)*