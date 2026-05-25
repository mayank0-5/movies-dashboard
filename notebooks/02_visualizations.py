

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ast

# ── Load Data ──────────────────────────────
df = pd.read_csv("data/tmdb_5000_movies.csv")
df = df.dropna(subset=["release_date", "revenue", "budget"])
df["release_year"] = pd.to_datetime(df["release_date"]).dt.year

# ── Chart 1: Movies Per Year ────────────────
plt.figure(figsize=(14, 5))
df["release_year"].value_counts().sort_index().plot(kind="bar", color="steelblue")
plt.title("Number of Movies Released Per Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("notebooks/chart1_movies_per_year.png")
plt.show()
print("Chart 1 saved!")

# ── Chart 2: Rating Distribution ────────────
plt.figure(figsize=(8, 5))
sns.histplot(df["vote_average"], bins=20, color="coral", kde=True)
plt.title("Movie Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("notebooks/chart2_rating_distribution.png")
plt.show()
print("Chart 2 saved!")

# ── Chart 3: Budget vs Revenue ──────────────
plt.figure(figsize=(8, 5))
plt.scatter(df["budget"], df["revenue"], alpha=0.4, color="steelblue")
plt.title("Budget vs Revenue")
plt.xlabel("Budget ($)")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("notebooks/chart3_budget_vs_revenue.png")
plt.show()
print("Chart 3 saved!")

# ── Chart 4: Top 10 Highest Revenue Movies ──
plt.figure(figsize=(10, 6))
top10 = df.nlargest(10, "revenue")
sns.barplot(x="revenue", y="title", data=top10, palette="viridis")
plt.title("Top 10 Highest Revenue Movies")
plt.xlabel("Revenue ($)")
plt.ylabel("Movie")
plt.tight_layout()
plt.savefig("notebooks/chart4_top10_revenue.png")
plt.show()
print("Chart 4 saved!")

print("\nAll charts saved!")