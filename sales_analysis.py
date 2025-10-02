import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("sales_data.csv")


print("🔹 Dataset Information:")
print(df.info())
print("\n🔹 First 5 Rows:")
print(df.head())
print("\n🔹 Summary Statistics:")
print(df.describe())


plt.figure(figsize=(8,5))
plt.plot(df['Month'], df['Sales'], marker='o', linestyle='-', color='b')
plt.title("Monthly Sales Trend", fontsize=14)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()


plt.figure(figsize=(8,5))
sns.barplot(x='Month', y='Sales', data=df, palette="viridis")
plt.title("Sales per Month", fontsize=14)
plt.show()


print("\n📊 Insights:")
print("- Sales are lowest in January.")
print("- Sales gradually increase across the year.")
print("- Peak sales are in November and December (holiday season).")