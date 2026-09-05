import os
import pandas as pd

# Define relative paths based on project structure
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(BASE_DIR, "data_raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "data_processed")

os.makedirs(PROCESSED_DIR, exist_ok=True)

clinical_file = os.path.join(RAW_DIR, "hantavirus_clinical.csv")
country_file = os.path.join(RAW_DIR, "hantavirus_country_yearly.csv")

print("Reading CSV files...")
df_clinical = pd.read_csv(clinical_file)
df_country = pd.read_csv(country_file)

# Standardize column names to lower case to prevent key mismatch errors
df_clinical.columns = df_clinical.columns.str.strip().str.lower()
df_country.columns = df_country.columns.str.strip().str.lower()

# Identify common link columns across files (e.g., country or iso3)
join_keys = [col for col in ['country', 'iso3'] if col in df_clinical.columns and col in df_country.columns]

if join_keys:
    print(f"Merging data on key(s): {join_keys}...")
    merged_df = pd.merge(df_clinical, df_country, on=join_keys, how="left", suffixes=('', '_yearly'))
else:
    print("No matching join key found. Concatenating available columns...")
    merged_df = pd.concat([df_clinical, df_country], axis=1)

output_path = os.path.join(PROCESSED_DIR, "merged_data.csv")
merged_df.to_csv(output_path, index=False)

print(f"Merge successful! Total rows generated: {len(merged_df)}")
print(f"File saved directly to: {output_path}")