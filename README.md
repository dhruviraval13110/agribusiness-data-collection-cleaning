# Agribusiness Data Collection and Cleaning

This project is part of my Junior Data Analyst – Agribusiness Virtual Internship at YuvaIntern.

## Objective

The purpose of this project is to collect a real public agriculture dataset and prepare it for analysis by applying data profiling, cleaning and quality checks.

## Dataset Used

The project uses agriculture data from FAOSTAT.

- Country: India
- Crops: Rice, Wheat, Maize (corn), Cotton lint, ginned, Sugar cane
- Years: 2015-2024
- Elements: Area harvested, Production Quantity and Yield
- Original dataset size: 129 rows and 15 columns

## Data Quality Checks

The dataset was checked for:

- Missing values
- Duplicate records
- Data types
- Numeric values
- Year range
- Unusual values and potential outliers

The initial profiling found **0 duplicate rows**.

## Cleaning Performed

1. Standardized column names
2. Cleaned text fields
3. Converted numeric fields
4. Checked missing values
5. Checked duplicate records
6. Checked negative values
7. Validated the selected year range
8. Investigated potential outliers using the IQR method
9. Exported the cleaned dataset separately

Potential outliers were investigated rather than automatically removed because agricultural production can naturally vary between crops and years.

## Tools Used

- Python
- Pandas
- NumPy
- JupyterLab
- Git
- GitHub

## Workflow

Public Data Source
        ↓
Data Acquisition
        ↓
Data Profiling
        ↓
Data Cleaning
        ↓
Data Validation
        ↓
Outlier Investigation
        ↓
Cleaned Dataset

## Project Structure

```text
data/
├── raw/
│   └── faostat_india_crops_2015_2024.csv
└── cleaned/
    └── faostat_india_crops_2015_2024_cleaned.csv

metadata/
├── cleaning_log.md
├── data_dictionary.csv
└── source_register.csv

notebooks/
└── data_profiling_cleaning.ipynb

scripts/
└── clean_agriculture_data.py

reports/
└── Week 2 internship report
