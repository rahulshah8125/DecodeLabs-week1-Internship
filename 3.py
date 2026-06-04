import pandas as pd

df = pd.read_excel("Online-Store-Orders.xlsx")

print(df.describe())

print("Total Sales:", df['TotalPrice'].sum())

print("Average Price:", df['UnitPrice'].mean())

print("Maximum Total Price:", df['TotalPrice'].max())