import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

# 1. Sales Trend (Line Chart)
plt.figure(figsize=(10,5))
plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# 2. Profit Distribution (Pie Chart)
plt.figure(figsize=(7,7))
plt.pie(
    df["Profit"],
    labels=df["Month"],
    autopct="%1.1f%%"
)
plt.title("Profit Contribution by Month")
plt.show()

# 3. Orders Analysis (Bar Chart)
plt.figure(figsize=(10,5))
plt.bar(df["Month"], df["Orders"])
plt.title("Monthly Orders")
plt.xlabel("Month")
plt.ylabel("Orders")
plt.show()

# 4. Sales vs Profit (Scatter Plot)
plt.figure(figsize=(8,5))
plt.scatter(df["Sales"], df["Profit"])
plt.title("Sales vs Profit Relationship")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()

print("\nDashboard Generated Successfully!")
print("\nHighest Sales Month:")
print(df.loc[df["Sales"].idxmax()])