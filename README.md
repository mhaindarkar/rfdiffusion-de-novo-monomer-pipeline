# RFdiffusion De Novo Monomer Pipeline

A minimal, interview-ready protein design project showing the first stage of modern de novo protein design: **AI-based backbone generation with RFdiffusion**, followed by **basic structural analysis, ranking, and candidate selection**.

## Project goal

This repository demonstrates a small but structured workflow for generating **de novo monomer protein backbones** using RFdiffusion and preparing them for downstream sequence design.

Instead of only running RFdiffusion once, this project aims to show a more realistic workflow:

1. generate multiple candidate backbones
2. collect the generated PDB files
3. extract simple structural features
4. rank and review candidates
5. prepare selected designs for the next stage of design

## Why this project matters

Modern protein design workflows often separate:

- **backbone generation**
- **sequence design**
- **structure validation**
- **experimental testing**

This repository focuses only on the **backbone generation stage**, which is where RFdiffusion fits.

That makes this a clean first project for understanding de novo protein design.

## Workflow

```text
RFdiffusion
   ↓
Generated backbone PDB files
   ↓
Feature extraction
   ↓
Candidate ranking
   ↓
Selection for downstream sequence design