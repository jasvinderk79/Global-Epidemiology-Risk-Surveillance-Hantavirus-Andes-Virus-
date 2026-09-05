import os
import pandas as pd

# Define relative paths based on project structure
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROCESSED_DIR = os.path.join(BASE_DIR, "data_processed")

merged_file_path = os.path.join(PROCESSED_DIR, "merged_data.csv")
cleaned_file_path = os.path.join(PROCESSED_DIR, "cleaned_hantavirus.csv")

# Verify if the merged_data.csv exists before reading
if not os.path.exists(merged_file_path):
    print(f"ERROR: Could not find {merged_file_path}")
    print("Please make sure you ran '01_merge_data.py' successfully first!")
    exit(1)

print("Reading merged dataset...")
df = pd.read_csv(merged_file_path)

# 1. Standardize column names (lowercase, no spaces)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 2. Convert date columns to datetime if present
date_cols = [col for col in df.columns if 'date' in col or 'year' in col]
for col in date_cols:
    try:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    except Exception:
        pass

# 3. Fill missing numerical values with median values
numeric_cols = df.select_dtypes(include=['number']).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# 4. Save the cleaned dataset
df.to_csv(cleaned_file_path, index=False)

print("Data cleaning completed successfully!")
print(f"Cleaned dataset saved to: {cleaned_file_path}")