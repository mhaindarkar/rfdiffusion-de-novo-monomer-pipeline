# Environment Notes

## Purpose

This file records practical setup notes for running RFdiffusion and analyzing the generated outputs.

The goal of this repository is not to reproduce the full RFdiffusion installation from scratch inside the repo itself, but to provide a clean, documented project around a small generation run.

## Main idea

This project focuses on:

- running a small RFdiffusion monomer generation job
- storing the resulting PDB files
- analyzing outputs with lightweight Python scripts

## Environment strategy

RFdiffusion typically requires a dedicated environment with multiple dependencies and, in many cases, GPU support.

Because of that, this repository separates:

- the **generation environment**
- the **analysis environment**

This makes the project easier to understand and maintain.

## Expected workflow

1. Run RFdiffusion in a suitable local, cluster, or container-based setup.
2. Save generated PDB files into `results/raw_outputs/`.
3. Use the Python scripts in this repo to collect, parse, rank, and summarize the outputs.

## Notes for this project

- RFdiffusion is used here for **unconditional monomer backbone generation**
- only a small number of designs are generated
- downstream sequence design is intentionally out of scope for version 1

## Analysis-side Python tools

Expected Python packages for the analysis scripts:

- pandas
- numpy
- biopython
- jupyter

## Future extension

Possible next upgrade:

- ProteinMPNN for sequence design on selected RFdiffusion backbones