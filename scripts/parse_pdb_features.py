from pathlib import Path
import pandas as pd
import numpy as np
from Bio.PDB import PDBParser

raw_dir = Path("results/raw_outputs")
out_path = Path("results/processed/design_features.csv")

parser = PDBParser(QUIET=True)


def compute_radius_of_gyration(coords):
    coords = np.array(coords)
    centroid = coords.mean(axis=0)
    squared_distances = ((coords - centroid) ** 2).sum(axis=1)
    return np.sqrt(squared_distances.mean())


rows = []

for pdb_file in sorted(raw_dir.glob("*.pdb")):
    try:
        structure = parser.get_structure(pdb_file.stem, pdb_file)

        ca_coords = []
        residue_count = 0
        chain_ids = set()

        for model in structure:
            for chain in model:
                chain_ids.add(chain.id)
                for residue in chain:
                    hetflag = residue.id[0]
                    if hetflag != " ":
                        continue

                    residue_count += 1

                    if "CA" in residue:
                        ca_coords.append(residue["CA"].coord)

        radius_of_gyration = None
        if len(ca_coords) > 0:
            radius_of_gyration = compute_radius_of_gyration(ca_coords)

        rows.append(
            {
                "design_id": pdb_file.stem,
                "file_path": str(pdb_file),
                "length": residue_count,
                "num_chains": len(chain_ids),
                "num_ca_atoms": len(ca_coords),
                "radius_of_gyration": radius_of_gyration,
            }
        )

    except Exception as e:
        rows.append(
            {
                "design_id": pdb_file.stem,
                "file_path": str(pdb_file),
                "length": None,
                "num_chains": None,
                "num_ca_atoms": None,
                "radius_of_gyration": None,
                "parse_error": str(e),
            }
        )

df = pd.DataFrame(rows)
out_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(out_path, index=False)

print(f"Saved design features to: {out_path}")
print(f"Number of parsed files: {len(df)}")
print(df.head())