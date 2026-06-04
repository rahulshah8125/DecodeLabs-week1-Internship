import pandas as pd

# Load dataset
df = pd.read_excel("Online-Store-Orders.xlsx")

# Display first 5 rows
print(df.head())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Dataset shape
print("\nRows and Columns:")
print(df.shape)

# Column names
print("\nColumns:")
print(df.columns)

# Data types
print("\nData Types:")
print(df.dtypes)