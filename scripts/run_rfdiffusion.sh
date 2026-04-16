#!/usr/bin/env bash
set -euo pipefail

OUTPUT_DIR="results/raw_outputs"
NUM_DESIGNS=10
MIN_LENGTH=70
MAX_LENGTH=100

mkdir -p "${OUTPUT_DIR}"

echo "RFdiffusion monomer generation"
echo "Output directory: ${OUTPUT_DIR}"
echo "Number of designs: ${NUM_DESIGNS}"
echo "Target length range: ${MIN_LENGTH}-${MAX_LENGTH}"

echo
echo "This script is currently a project placeholder."
echo "Replace the command section below with your working RFdiffusion command."
echo
echo "Expected result:"
echo "- generated PDB files saved into ${OUTPUT_DIR}"
echo "- one file per design"
echo
echo "Once generation is complete, run:"
echo "python scripts/collect_results.py"
echo "python scripts/parse_pdb_features.py"
echo "python scripts/rank_designs.py"

# ------------------------------------------------------------
# Replace this block with your actual RFdiffusion command
# Example only: keep as placeholder until your RFdiffusion setup works
# ------------------------------------------------------------

echo
echo "[PLACEHOLDER] No RFdiffusion command has been executed yet."