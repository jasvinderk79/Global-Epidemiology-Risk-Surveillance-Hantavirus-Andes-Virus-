import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# 1. Resolve relative paths dynamically
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROCESSED_DIR = os.path.join(BASE_DIR, "data_processed")
cleaned_file_path = os.path.join(PROCESSED_DIR, "cleaned_hantavirus.csv")

# 2. Verify file existence
if not os.path.exists(cleaned_file_path):
    print(f"ERROR: Could not find {cleaned_file_path}")
    print("Please run '02_clean_data.py' successfully first!")
    exit(1)

print("Reading cleaned dataset...")
df = pd.read_csv(cleaned_file_path)

# 3. Select numerical features for modeling
numeric_cols = df.select_dtypes(include=['number']).columns.tolist()

if len(numeric_cols) < 2:
    print("ERROR: Not enough numeric columns found in the dataset to train a machine learning model.")
    exit(1)

# Set the last numerical column as the target variable (y) and the rest as features (X)
target_col = numeric_cols[-1]
feature_cols = numeric_cols[:-1]

print(f"Features (X): {feature_cols}")
print(f"Target (y): {target_col}")

X = df[feature_cols].fillna(0)
y = df[target_col].fillna(0)

# Convert continuous targets to discrete categories if necessary for classification
if y.nunique() > 10:
    print("Converting continuous target into binary categories (above/below median)...")
    y = (y > y.median()).astype(int)

# 4. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Train Random Forest Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. Evaluate
predictions = model.predict(X_test)
print("\n--- Model Evaluation Report ---")
print(classification_report(y_test, predictions, zero_division=0))
print("Machine Learning Model Training Complete!")