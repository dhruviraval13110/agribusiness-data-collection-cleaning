import pandas as pd

# Load raw FAOSTAT data
input_file = "../data/raw/faostat_india_crops_2015_2024.csv"

df = pd.read_csv(input_file)

print("Original shape:", df.shape)

# Standardize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)
    .str.replace("/", "_", regex=False)
)

# Clean text fields
text_columns = [
    "domain",
    "area",
    "element",
    "item",
    "unit",
    "flag",
    "flag_description"
]

for col in text_columns:
    if col in df.columns:
        df[col] = df[col].astype("string").str.strip()

# Convert numeric columns
numeric_columns = [
    "area_code_m49",
    "element_code",
    "item_code_cpc",
    "year_code",
    "year",
    "value"
]

for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove exact duplicates
df = df.drop_duplicates()

# Basic validation
print("Missing values:")
print(df.isnull().sum())

print("Duplicate rows:", df.duplicated().sum())

print("Negative values:", (df["value"] < 0).sum())

# Save cleaned dataset
output_file = "../data/cleaned/faostat_india_crops_2015_2024_cleaned.csv"

df.to_csv(output_file, index=False)

print("Cleaned shape:", df.shape)
print("Cleaned dataset saved successfully.")
