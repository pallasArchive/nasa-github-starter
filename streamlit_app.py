import pandas as pd
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Meteorite Landings Explorer", layout="wide")

st.title("🌠 Meteorite Landings Explorer")
st.markdown("Upload a CSV (e.g., NASA Meteorite Landings) to explore basic stats.")

uploaded = st.file_uploader("Upload CSV", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
else:
    sample = Path("data/meteorites_sample.csv")
    if sample.exists():
        df = pd.read_csv(sample)
        st.info("Using included sample dataset (upload your own to replace).")
    else:
        st.stop()

# Normalize columns
df.columns = [c.strip() for c in df.columns]
if "year" in df.columns:
    df["year"] = pd.to_datetime(df["year"], errors="coerce")
    df["year_num"] = df["year"].dt.year
    df["decade"] = (df["year_num"] // 10) * 10
if "mass (g)" in df.columns:
    df["mass_g"] = pd.to_numeric(df["mass (g)"], errors="coerce")
elif "mass" in df.columns:
    df["mass_g"] = pd.to_numeric(df["mass"], errors="coerce")

left, right = st.columns(2)
with left:
    st.subheader("Quick Stats")
    st.write(df[["name","recclass"]].head(10))
with right:
    if "decade" in df.columns:
        st.subheader("Counts by Decade")
        st.bar_chart(df.dropna(subset=["decade"]).groupby("decade").size())

st.markdown("---")
st.caption("Starter app — extend with maps, filters, and more!")
