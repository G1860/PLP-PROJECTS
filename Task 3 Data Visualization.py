import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("company_data.csv")

# Ensure revenue column has correct name
df.rename(columns={"Revenue ($)": "Revenue (KES)"}, inplace=True)

# 1. Line chart – Trends of revenue over time 
import numpy as np
df['Date'] = pd.date_range(start="2024-01-01", periods=len(df), freq='W')

plt.figure(figsize=(8,5))
plt.plot(df['Date'], df['Revenue (KES)'], marker='o', linestyle='-', color='blue')
plt.title("Revenue Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue (KES)")
plt.grid(True)
plt.show()

# 2. Bar chart – Average revenue per department
avg_rev_per_dept = df.groupby("Department")["Revenue (KES)"].mean()
avg_rev_per_dept.plot(kind='bar', color='orange', figsize=(7,5))
plt.title("Average Revenue per Department")
plt.xlabel("Department")
plt.ylabel("Average Revenue (KES)")
plt.show()

# 3. Histogram – Distribution of Revenue
plt.figure(figsize=(7,5))
plt.hist(df["Revenue (KES)"], bins=6, color='purple', edgecolor='black')
plt.title("Distribution of Revenue (KES)")
plt.xlabel("Revenue (KES)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot – Revenue vs Employees
plt.figure(figsize=(7,5))
plt.scatter(df["Employees"], df["Revenue (KES)"], color='green')
plt.title("Employees vs Revenue (KES)")
plt.xlabel("Employees")
plt.ylabel("Revenue (KES)")
plt.grid(True)
plt.show()
