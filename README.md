# Invoice Automator 🧾

Générateur de **factures PDF** à partir d’un **fichier CSV** (clients, articles, TVA, total).

---

## 🚀 Objectif
- Simplifier la création de factures depuis un tableau CSV.  
- Générer automatiquement des fichiers PDF avec un format standardisé.  
- (Optionnel) Ajouter un logo, une numérotation automatique et un export par email.  

---

## ⚙️ Installation (mode développement)

Créer un environnement virtuel et installer les dépendances nécessaires :

```bash
python -m venv .venv
# Windows : .venv\Scripts\activate
# macOS/Linux :
source .venv/bin/activate

pip install -U pip
pip install pandas fpdf2
