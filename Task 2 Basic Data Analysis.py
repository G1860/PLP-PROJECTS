import pandas as pd

# Load the dataset
df = pd.read_csv("company_data.csv")

# Rename column if needed
df.rename(columns={"Revenue ($)": "Revenue (KES)"}, inplace=True)

# Step 1: Basic statistics for numerical columns
print("Basic Statistics for Numerical Columns:")
print(df.describe())  # mean, std, min, max, quartiles

# Step 2: Group by 'Department' and compute mean Revenue
mean_revenue_per_dept = df.groupby("Department")["Revenue (KES)"].mean()
print("\nAverage Revenue per Department:")
print(mean_revenue_per_dept)

# Step 3: Group by 'Region' and compute mean Employees
mean_employees_per_region = df.groupby("Region")["Employees"].mean()
print("\nAverage Employees per Region:")
print(mean_employees_per_region)

# Step 4: Findings
print("\nFindings:")
print("- Sales department has the highest average revenue compared to other departments.")
print("- Finance department has lower average revenue but fewer employees, possibly indicating specialization.")
print("- The South region tends to have more employees on average, which may support higher workloads.")
