# Cleaning Log

## Project

Agribusiness Data Collection and Cleaning

## Data Source

FAOSTAT - Crops and livestock products

## Dataset Selection

- Country: India
- Crops: Rice, Wheat, Maize (corn), Cotton lint, ginned, Sugar cane
- Years: 2015 to 2024
- Elements: Area harvested, Production Quantity, Yield
- File format: CSV

## Initial Data Profiling

The downloaded dataset contained 129 rows and 15 columns.

Initial checks were performed for:

- Data types
- Missing values
- Duplicate records
- Numeric values
- Year range
- Basic descriptive statistics

## Cleaning Steps Performed

1. Standardized column names.
2. Removed extra spaces from text fields.
3. Converted numeric fields to numeric data types.
4. Checked for missing values.
5. Checked for duplicate rows.
6. Checked for negative values.
7. Verified that years were within the selected 2015-2024 range.
8. Investigated potential outliers using the IQR method.
9. Saved the cleaned dataset as a separate CSV file.

## Data Quality Results

- Duplicate rows found: 0
- Selected year range: 2015-2024
- Original dataset size: 129 rows and 15 columns
- Cleaned dataset was saved separately from the raw dataset.

## Outlier Handling

Potential outliers were identified using the Interquartile Range (IQR) method.

Outliers were not automatically deleted. Agricultural production can naturally vary between crops and years, so unusual values should be checked against the original source and agricultural context before removal.

## Output

The cleaned dataset is stored separately in the `data/cleaned/` folder.

The original downloaded dataset is preserved in the `data/raw/` folder.
