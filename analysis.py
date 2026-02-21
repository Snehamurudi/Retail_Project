import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Sample - Superstore.csv", encoding='latin1')

# Show first rows
print(df.head())

# Convert date
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Create Inventory Days
df['Inventory_Days'] = np.random.randint(1, 100, size=len(df))

# Correlation
corr = df[['Inventory_Days', 'Profit']].corr()
print("\nCorrelation:\n", corr)

# Plot
sns.scatterplot(x='Inventory_Days', y='Profit', data=df)
plt.title("Inventory Days vs Profit")
plt.show()
