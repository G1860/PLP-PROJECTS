# ==============================
# Task 1: Load and Explore the Dataset
# ==============================

import pandas as pd

# Step 1: Loading my dataset 
df = pd.read_csv("company_data.csv")

# Step 2: Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Step 3: Explore the dataset structure
print("\nDataset Info:")
print(df.info())

# Step 4: Check for missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Step 5: Clean the dataset 
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# If string/object column has missing values, fill with 'Unknown'
string_cols = df.select_dtypes(include=['object']).columns
df[string_cols] = df[string_cols].fillna("Unknown")

# Alternative: Drop rows with missing values instead
# df = df.dropna()

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())
