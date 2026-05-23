

import pandas as pd
import numpy as np

# ── Load Data ──────────────────────────────
df = pd.read_csv("data/tmdb_5000_movies.csv")
print("Dataset loaded! Shape:", df.shape)

# ── Basic Info ─────────────────────────────
print("\nFirst 5 rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nBasic Statistics:")
print(df.describe())

# ── Clean Data ─────────────────────────────
df = df.dropna(subset=["release_date", "revenue", "budget"])
df["release_year"] = pd.to_datetime(df["release_date"]).dt.year

# ── Key Insights ───────────────────────────
print(f"\nTotal Movies     : {len(df)}")
print(f"Year Range       : {df['release_year'].min()} - {df['release_year'].max()}")
print(f"Average Rating   : {df['vote_average'].mean():.2f}")
print(f"Average Revenue  : ${df['revenue'].mean():,.0f}")
print(f"Average Budget   : ${df['budget'].mean():,.0f}")

# ── Top 10 Highest Rated Movies ────────────
print("\nTop 10 Highest Rated Movies:")
top_rated = df[df["vote_count"] > 100].nlargest(10, "vote_average")[["title", "vote_average", "release_year"]]
print(top_rated.to_string(index=False))

# ── Top 10 Highest Revenue Movies ──────────
print("\nTop 10 Highest Revenue Movies:")
top_revenue = df.nlargest(10, "revenue")[["title", "revenue", "release_year"]]
print(top_revenue.to_string(index=False))