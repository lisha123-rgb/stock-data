import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("stock_data.csv", parse_dates=["Date"])
df.set_index("Date", inplace=True)

print("🔹 Data Sample:")
print(df.head())


plt.figure(figsize=(10,6))
plt.plot(df.index, df["INFY.NS"], label="Infosys")
plt.plot(df.index, df["TCS.NS"], label="TCS")
plt.title("Stock Price Trend (Infosys vs TCS)", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.legend()
plt.grid(alpha=0.3)
plt.show()


returns = df.pct_change().dropna()

plt.figure(figsize=(10,6))
sns.histplot(returns["INFY.NS"], bins=50, color="blue", kde=True, label="Infosys")
sns.histplot(returns["TCS.NS"], bins=50, color="green", kde=True, label="TCS")
plt.title("Distribution of Daily Returns", fontsize=14)
plt.xlabel("Daily Return")
plt.legend()
plt.show()

df["INFY_20MA"] = df["INFY.NS"].rolling(window=20).mean()
df["INFY_50MA"] = df["INFY.NS"].rolling(window=50).mean()

plt.figure(figsize=(10,6))
plt.plot(df.index, df["INFY.NS"], label="Infosys Price", color="blue")
plt.plot(df.index, df["INFY_20MA"], label="20-Day MA", color="orange")
plt.plot(df.index, df["INFY_50MA"], label="50-Day MA", color="red")
plt.title("Infosys Stock with Moving Averages", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.legend()
plt.grid(alpha=0.3)
plt.show()

cumulative_returns = (1 + returns).cumprod()

plt.figure(figsize=(10,6))
plt.plot(cumulative_returns.index, cumulative_returns["INFY.NS"], label="Infosys")
plt.plot(cumulative_returns.index, cumulative_returns["TCS.NS"], label="TCS")
plt.title("Cumulative Returns (Infosys vs TCS)", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Growth of ₹1 Investment")
plt.legend()
plt.grid(alpha=0.3)
plt.show()


print("\n📊 Insights:")
print("- Infosys and TCS both show growth with fluctuations.")
print("- Daily returns show volatility differences between the two stocks.")
print("- Moving averages help identify short-term vs long-term trends.")
print("\n🔹 Final Cumulative Return (2022–2023):")
print(cumulative_returns.tail(1))
