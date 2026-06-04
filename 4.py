import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("Online-Store-Orders.xlsx")

# Bar chart
plt.figure(figsize=(8,5))
sns.barplot(x='Quantity', y='TotalPrice', data=df)

plt.title("Quantity vs Total Price")
plt.show()

# Histogram
plt.figure(figsize=(8,5))
sns.histplot(df['TotalPrice'], bins=20)

plt.title("Total Price Distribution")
plt.show()