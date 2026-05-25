

import pandas as pd
import plotly.express as px
import streamlit as st

# ── Load Data ──────────────────────────────
df = pd.read_csv("data/tmdb_5000_movies.csv")
df = df.dropna(subset=["release_date", "revenue", "budget"])
df["release_year"] = pd.to_datetime(df["release_date"]).dt.year

# ── App Title ───────────────────────────────
st.set_page_config(page_title="🎬 Movies Dashboard", layout="wide")
st.title("🎬 Movies Analytics Dashboard")
st.write("Explore trends, ratings, and revenues from 5000+ movies!")

# ── Sidebar Filters ─────────────────────────
st.sidebar.header("🔍 Filters")

year_range = st.sidebar.slider(
    "Select Year Range",
    int(df["release_year"].min()),
    int(df["release_year"].max()),
    (2000, 2017)
)

min_rating = st.sidebar.slider("Minimum Rating", 0.0, 10.0, 6.0)

# ── Filter Data ─────────────────────────────
filtered = df[
    (df["release_year"] >= year_range[0]) &
    (df["release_year"] <= year_range[1]) &
    (df["vote_average"] >= min_rating)
]

# ── KPI Cards ───────────────────────────────
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)
col1.metric("🎬 Total Movies", len(filtered))
col2.metric("⭐ Avg Rating", f"{filtered['vote_average'].mean():.2f}")
col3.metric("💰 Avg Revenue", f"${filtered['revenue'].mean():,.0f}")
col4.metric("🎯 Avg Budget", f"${filtered['budget'].mean():,.0f}")

st.markdown("---")

# ── Chart 1: Movies Per Year ────────────────
st.subheader("📈 Movies Released Per Year")
movies_per_year = filtered["release_year"].value_counts().sort_index().reset_index()
movies_per_year.columns = ["Year", "Count"]
fig1 = px.bar(movies_per_year, x="Year", y="Count", color="Count", color_continuous_scale="Blues")
st.plotly_chart(fig1, use_container_width=True)

# ── Chart 2: Rating Distribution ────────────
st.subheader("⭐ Rating Distribution")
fig2 = px.histogram(filtered, x="vote_average", nbins=20, color_discrete_sequence=["coral"])
st.plotly_chart(fig2, use_container_width=True)

# ── Chart 3: Budget vs Revenue ──────────────
st.subheader("💰 Budget vs Revenue")
fig3 = px.scatter(filtered, x="budget", y="revenue",
                  hover_name="title", color="vote_average",
                  color_continuous_scale="Viridis")
st.plotly_chart(fig3, use_container_width=True)

# ── Chart 4: Top 10 Movies by Revenue ───────
st.subheader("🏆 Top 10 Highest Revenue Movies")
top10 = filtered.nlargest(10, "revenue")[["title", "revenue", "vote_average"]]
fig4 = px.bar(top10, x="revenue", y="title", orientation="h",
              color="vote_average", color_continuous_scale="Viridis")
st.plotly_chart(fig4, use_container_width=True)

# ── Raw Data Table ───────────────────────────
st.markdown("---")
st.subheader("📋 Raw Data")
st.dataframe(filtered[["title", "release_year", "vote_average", "budget", "revenue"]].reset_index(drop=True))