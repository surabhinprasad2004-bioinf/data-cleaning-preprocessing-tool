import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("data.csv")

print("=" * 50)
print("ORIGINAL DATASET")
print("=" * 50)
print(df)

# -------------------------------
# Handle Missing Values
# -------------------------------
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Fill numerical missing values with median
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Salary"] = df["Salary"].fillna(df["Salary"].median())

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# -------------------------------
# Remove Duplicates
# -------------------------------
duplicates = df.duplicated().sum()

print("\nDuplicate Rows Found:", duplicates)

df.drop_duplicates(inplace=True)

# -------------------------------
# Outlier Detection using IQR
# -------------------------------
numeric_columns = ["Age", "Salary"]

for col in numeric_columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    df = df[
        (df[col] >= lower_bound) &
        (df[col] <= upper_bound)
    ]

# -------------------------------
# Display Cleaned Data
# -------------------------------
print("\n" + "=" * 50)
print("CLEANED DATASET")
print("=" * 50)
print(df)

# -------------------------------
# Save Cleaned Dataset
# -------------------------------
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned dataset saved as 'cleaned_data.csv'")