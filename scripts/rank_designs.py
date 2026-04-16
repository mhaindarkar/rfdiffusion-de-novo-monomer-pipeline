from pathlib import Path
import pandas as pd
import numpy as np

features_path = Path("results/processed/design_features.csv")
summary_path = Path("results/summary.csv")

if not features_path.exists():
    raise FileNotFoundError(f"Missing input file: {features_path}")

df = pd.read_csv(features_path)

if df.empty:
    raise ValueError("No design features found. Make sure PDB files exist in results/raw_outputs/")

# Keep only rows with valid radius_of_gyration
valid_df = df.dropna(subset=["radius_of_gyration"]).copy()

if valid_df.empty:
    raise ValueError("No valid structures with radius_of_gyration found.")

rog_min = valid_df["radius_of_gyration"].min()
rog_max = valid_df["radius_of_gyration"].max()

if np.isclose(rog_min, rog_max):
    valid_df["compactness_score"] = 1.0
else:
    valid_df["compactness_score"] = 1 - (
        (valid_df["radius_of_gyration"] - rog_min) / (rog_max - rog_min)
    )

valid_df = valid_df.sort_values(
    by=["compactness_score", "length"],
    ascending=[False, False]
).reset_index(drop=True)

valid_df["rank"] = valid_df.index + 1
valid_df["selected"] = valid_df["rank"].apply(lambda x: "yes" if x <= 3 else "no")
valid_df["notes"] = valid_df["selected"].map(
    {"yes": "selected as top compact candidate", "no": ""}
)

final_columns = [
    "rank",
    "design_id",
    "file_path",
    "length",
    "num_chains",
    "num_ca_atoms",
    "radius_of_gyration",
    "compactness_score",
    "selected",
    "notes",
]

valid_df = valid_df[final_columns]
valid_df.to_csv(summary_path, index=False)

print(f"Saved ranked summary to: {summary_path}")
print(valid_df.head())