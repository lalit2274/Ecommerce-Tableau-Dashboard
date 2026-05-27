import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("train.csv")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Title missing હોય તો Unknown
df['title'] = df['title'].fillna('Unknown')

# Rating numeric convert + missing = 0
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce').fillna(0)

# Categorical missing = Unknown
df['maincateg'] = df['maincateg'].fillna('Unknown')
df['platform'] = df['platform'].fillna('Unknown')

# Numeric columns
numeric_cols = [
    'actprice1',
    'norating1',
    'noreviews1',
    'star_5f',
    'star_4f'
]

# Missing numeric values = 0
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

# Clean title spaces
df['title'] = df['title'].str.strip()

# Optional new column
df['review_to_rating_ratio'] = df['noreviews1'] / (df['norating1'] + 1)

# Save cleaned file
df.to_csv("cleaned_ecommerce_data.csv", index=False)

print("Cleaning completed!")
print(df.isnull().sum())
print(df.shape)
