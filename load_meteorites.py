#!/usr/bin/env python3
"""
Load and summarize NASA Meteorite Landings data.
- Reads a CSV file (local path) with columns that include 'mass (g)' and 'year'.
- Outputs a summary CSV and a simple chart into images/ and outputs/.
"""
import argparse
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

def ensure_dirs():
    os.makedirs("images", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

def parse_args():
    p = argparse.ArgumentParser(description="Process Meteorite Landings CSV")
    p.add_argument("--input", required=True, help="Path to CSV file")
    return p.parse_args()

def load_csv(path):
    df = pd.read_csv(path)
    # Normalize column names
    df.columns = [c.strip() for c in df.columns]
    # Parse year if present
    if "year" in df.columns:
        df["year"] = pd.to_datetime(df["year"], errors="coerce")
        df["year_num"] = df["year"].dt.year
        # decade
        df["decade"] = (df["year_num"] // 10) * 10
    # Parse mass
    mass_col = None
    for cand in ["mass (g)", "mass", "Mass (g)"]:
        if cand in df.columns:
            mass_col = cand
            break
    if mass_col is not None:
        df["mass_g"] = pd.to_numeric(df[mass_col], errors="coerce")
    else:
        df["mass_g"] = None
    return df

def summarize(df):
    out = {}
    if "decade" in df.columns:
        out["count_by_decade"] = (
            df.dropna(subset=["decade"])
              .groupby("decade", as_index=False)
              .size()
              .rename(columns={"size":"count"})
              .sort_values("decade")
        )
    if "mass_g" in df.columns and "year_num" in df.columns:
        out["top10_by_mass"] = (
            df.dropna(subset=["mass_g"])
              .sort_values("mass_g", ascending=False)
              .head(10)
              [["name","recclass","mass_g","year_num","reclat","reclong"]]
        )
    return out

def plot(df):
    # Scatter: year vs mass (log scale)
    if "year_num" in df.columns and "mass_g" in df.columns:
        plt.figure()
        small = df.dropna(subset=["year_num","mass_g"])
        if len(small) == 0:
            return
        plt.scatter(small["year_num"], small["mass_g"], s=10, alpha=0.6)
        plt.yscale("log")
        plt.xlabel("Year")
        plt.ylabel("Mass (g) [log]")
        plt.title("Meteorite Mass vs. Year")
        plt.tight_layout()
        plt.savefig("images/mass_vs_year.png", dpi=160)
        plt.close()

def main():
    args = parse_args()
    ensure_dirs()
    df = load_csv(args.input)
    sums = summarize(df)
    # Write outputs
    if "count_by_decade" in sums:
        sums["count_by_decade"].to_csv("outputs/summary_count_by_decade.csv", index=False)
    if "top10_by_mass" in sums:
        sums["top10_by_mass"].to_csv("outputs/summary_top10_by_mass.csv", index=False)
    plot(df)
    print("Done. See 'outputs/' and 'images/'.")

if __name__ == "__main__":
    sys.exit(main())
