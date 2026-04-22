# Section-B_G-12_Profit-Track
# Profit Track

Retail analytics project using Walmart sales dataset.

## Goal
Analyze sales trends, holiday impact, store performance, and revenue insights.

## Team Roles
- Project Lead:
- Data Lead:
- ETL Lead:

## Structure
data/
notebooks/
reports/
tableau/
docs/

## Data Pipeline
- **Extraction**: The raw dataset (`Walmart-Retail-Dataset.csv`) is loaded and inspected via `notebooks/01_extraction.ipynb`. Due to formatting inconsistencies, bad lines are skipped to ensure stable parsing.
- **Cleaning**: Data is processed using `notebooks/02_cleaning.ipynb` leveraging the custom `basic_clean` function from `scripts/etl_pipeline.py`. This standardizes all column names to snake_case, removes duplicates, and trims whitespace from string columns. The final cleaned dataset is exported to `data/processed/cleaned_dataset.csv` and used for downstream EDA and Tableau reporting.