# AQI India Analyser
# By Padma Shree
# Project Start Date: 28-03-2026

import pandas as pd

# Step 1 - Load the real data
df = pd.read_csv(r"C:\Users\Padma shree jena\Desktop\PadduDS_Journey\05_resources\datasets\city_day.csv")

# Step 2 - Understand the data
print("=== AQI INDIA ANALYSER ===")
print("Total records:", len(df))
print("Total cities:", df["City"].nunique())
print("Date range:", df["Date"].min(), "to", df["Date"].max())
print("\nFirst 5 rows:")
print(df.head())

# Step 3 - Check missing values
print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

# Step 4 - See all 26 cities
print("\n=== ALL CITIES ===")
print(df["City"].unique())

# Step 5 - Clean the data
print("\n=== CLEANING DATA ===")

# Remove rows where AQI is missing
df_clean = df.dropna(subset=["AQI"])
print("Rows after cleaning:", len(df_clean))
print("Rows removed:", len(df) - len(df_clean))

# Confirm no missing AQI values now
print("Missing AQI values now:", df_clean["AQI"].isnull().sum())

# Step 6 - Find most and least polluted cities
print("\n=== CITY AQI ANALYSIS ===")

city_aqi = df_clean.groupby("City")["AQI"].mean().round(1)
city_aqi = city_aqi.sort_values(ascending=False)

print("Most polluted cities:")
print(city_aqi.head(5))

print("\nLeast polluted cities:")
print(city_aqi.tail(5))

# Step 7 - Which month has worst AQI?
print("\n=== MONTHLY AQI ANALYSIS ===")

df_clean["Date"] = pd.to_datetime(df_clean["Date"])
df_clean["Month"] = df_clean["Date"].dt.month

monthly_aqi = df_clean.groupby("Month")["AQI"].mean().round(1)
print(monthly_aqi)

worst_month = monthly_aqi.idxmax()
best_month = monthly_aqi.idxmin()
print("\nWorst month number:", worst_month)
print("Best month number:", best_month)

# Step 8 - Draw our first chart!
import matplotlib.pyplot as plt

print("\n=== DRAWING CHARTS ===")

# Chart 1 - Most polluted cities
city_aqi.head(10).plot(kind="bar", color="red", figsize=(10,6))
plt.title("Top 10 Most Polluted Cities in India (2015-2020)")
plt.xlabel("City")
plt.ylabel("Average AQI")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r"C:\Users\Padma shree jena\Desktop\PadduDS_Journey\01_phase1\aqi_india_analyser\outputs\charts\most_polluted_cities.png")
plt.show()
print("Chart saved!!")

# Chart 2 - Monthly AQI trend
plt.figure(figsize=(10,6))
monthly_aqi.plot(kind="line", color="blue", marker="o")
plt.title("Monthly AQI Trend across India (2015-2020)")
plt.xlabel("Month")
plt.ylabel("Average AQI")
plt.xticks(range(1,13), ["Jan","Feb","Mar","Apr","May","Jun",
                          "Jul","Aug","Sep","Oct","Nov","Dec"])
plt.tight_layout()
plt.savefig(r"C:\Users\Padma shree jena\Desktop\PadduDS_Journey\01_phase1\aqi_india_analyser\outputs\charts\monthly_trend.png")
plt.show()
print("Chart 2 saved!!")

# Chart 3 - Least polluted cities
plt.figure(figsize=(10,6))
city_aqi.tail(10).plot(kind="bar", color="green")
plt.title("Top 10 Cleanest Cities in India (2015-2020)")
plt.xlabel("City")
plt.ylabel("Average AQI")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r"C:\Users\Padma shree jena\Desktop\PadduDS_Journey\01_phase1\aqi_india_analyser\outputs\charts\cleanest_cities.png")
plt.show()
print("Chart 3 saved!!")