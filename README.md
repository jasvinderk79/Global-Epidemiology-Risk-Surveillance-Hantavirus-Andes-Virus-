# Global Epidemiology & Risk Surveillance — Hantavirus / Andes Virus

End-to-end health analytics pipeline that merges multi-source clinical and registry data to predict patient mortality risk and visualize outbreak patterns.

## Problem
Public health responders needed a way to combine multi-source clinical and registry data on Hantavirus/Andes Virus cases to identify which patients were at highest mortality risk, and to understand outbreak patterns geographically.

## What this project does
- Built an end-to-end **Python / DuckDB / SQL** pipeline to clean and merge multi-source clinical and registry datasets, with automated type-casting and missing-value imputation
- Trained a **Random Forest Classifier** (Scikit-Learn) to predict patient mortality risk — ICU admission and mechanical ventilation emerged as the strongest clinical risk drivers
- Built a **3-view interactive Tableau dashboard**: a choropleth outbreak map, a demographic risk breakdown, and a clinical severity matrix, designed for executive-level reporting

## Tools & Stack
Python · Pandas · DuckDB · SQL · Scikit-Learn · Tableau

## Dashboard
🔗 [View the live Tableau dashboard](https://public.tableau.com/app/profile/jasvinder.kaur8501/vizzes) *(link to the specific viz once published)*

## Outcome
A reusable pipeline and dashboard that turns raw multi-source health data into a clear, risk-ranked view that decision-makers can act on directly, without needing to touch the underlying data themselves.

## Author
Jasvinder Kaur — [LinkedIn](https://www.linkedin.com/in/jasvinder-kaur-406b13285/) · [Kaggle](https://www.kaggle.com/jasvinderkaur13)
