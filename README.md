# Wine Quality – Analýza (UCI)

> Prehľadný repozitár s notebookom pre analýzu kvality vín (červené/ biele) zo zdroja UCI ML Repository.

- **Autor:** Sabína Švecková
- **Dátový zdroj:** UCI Machine Learning Repository – *Wine Quality*  
  URL: https://archive.ics.uci.edu/dataset/186/wine+quality
- **Licencia kódu:** MIT (pozri súbor `LICENSE`)  
- **Licencia datasetu:** Patrí pôvodnému autorovi/ UCI; pozri súbor `DATASET_NOTICE.md`.

## Štruktúra

```
.
├── data
│   ├── raw
│   │   ├── winequality-red.csv
│   │   ├── winequality-white.csv
│   │   └── winequality.names
│   └── processed/              # (gitignored)
├── notebooks
│   ├── zadanie_Sveckova.ipynb            # originál
│   └── zadanie_Sveckova_clean.ipynb      # bez výstupov (na GitHub odporúčané)
├── reports
│   └── figures/                 # exportované grafy (gitignored *.png/*.svg)
├── src/                         # (voliteľné) pomocné skripty
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Rýchly štart

### 1) Klonovanie a prostredie
```bash
git clone <tvoj-repo-url> wine-quality-project
cd wine-quality-project

# Vytvor a aktivuj virtuálne prostredie (príklad s venv)
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/ Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

### 2) Spustenie Jupyteru
```bash
jupyter notebook
```
Otvor si `notebooks/zadanie_Sveckova.ipynb` (plná verzia) alebo `notebooks/zadanie_Sveckova_clean.ipynb` (bez výstupov).

### 3) Export grafov
V notebooku ulož grafy do `reports/figures/` (adresár je pripravený).

## Obsah analýzy (stručne)
- Načítanie `winequality-red.csv` a `winequality-white.csv`
- Deskriptívna štatistika, vizualizácia rozdelení, korelácie
- Modelovanie (napr. regresia/ klasifikácia kvality), porovnanie metrik
- Záver a odporúčania

## Poznámky k datasetu
- Pôvodný dataset môže obsahovať špecifiká (typy premenných, rozsahy, chýbajúce hodnoty/ outliery).
- Pred použitím v produkcii odporúčam pridať dátovú validáciu a testy.

## Ako pridať do GitHubu
```bash
# v koreňovom priečinku projektu:
git init
git add .
git commit -m "Initial commit: wine quality analysis (UCI)"
git branch -M main
git remote add origin <tvoj-repo-url>
git push -u origin main
```
