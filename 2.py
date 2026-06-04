import pandas as pd

# Loads dataset
a = pd.read_excel(r"C:\Users\RAHUL SHAH\OneDrive\Desktop\intership of ds\Online-Store-Orders.xlsx")

# Dataset shape the before cleaning
print("Dataset Shape Before Cleaning:")
print(a.shape)

# Checks missing values
print("\nMissing Values Before Cleaning:")
print(a.isnull().sum())

# Checks duplicate rows
print("\nDuplicate Rows Before Cleaning:")
print(a.duplicated().sum())

# Removes duplicate rows
df = a.drop_duplicates()

# Filling  missing values
df = a.fillna(0)

# Convert Date column to the datetime format inthe sheets
df['Date'] = pd.to_datetime(df['Date'])

# Dataset shape after the cleaning
print("\nDataset Shape After Cleaning:")
print(a.shape)

# Checking missing values again in sheet
print("\nMissing Values After Cleaning:")
print(a.isnull().sum())

# Checking the  duplicate rows againin sheet
print("\nDuplicate Rows After Cleaning:")
print(a.duplicated().sum())

# Display the first 5 rows of it 
print("\nCleaned Dataset Preview:")
print(a.head())

# Save cleaned dataset
df.to_excel("Cleaned_Online_Store_Orders.xlsx", index=False)

print("\nCleaned dataset saved successfully!")