from pathlib import Path
import pandas as pd

raw_dir = Path("results/raw_outputs")
out_path = Path("results/summary.csv")

rows = []

for file in sorted(raw_dir.glob("*.pdb")):
    rows.append(
        {
            "design_id": file.stem,
            "file_path": str(file),
            "selected": "no",
            "notes": "",
        }
    )

df = pd.DataFrame(rows)

out_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(out_path, index=False)

print(f"Saved summary table to: {out_path}")
print(f"Number of PDB files found: {len(df)}")
print(df.head())