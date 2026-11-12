# Yamuna River BOD Compliance Checker

A Python-based environmental data analysis tool that evaluates the Biochemical Oxygen Demand (BOD) of the Yamuna River using official Central Pollution Control Board (CPCB) monitoring data from 2024 and 2025.

 ## Project Overview
Surface water monitoring datasets often exist in static PDF reports, making year-over-year compliance tracking difficult. This script automates benchmarking against a 3.0 mg/L BOD benchmark.

It processes geographic monitoring stations (from Yamunotri down to Etawah), calculates mid-range BOD levels (midpoint of each station's annual minimum and maximum), and visually flags stations exceeding the benchmark of 3.0 mg/L.

## Key Insights
- Upstream stations (Yamunotri, Hathnikund) stay at or below the benchmark.
- Central Delhi stations show mid-range BOD of about 23.5 to 43.0 mg/L, up to about 14x the benchmark.
- Mathura, Agra and Etawah are lower than Delhi but still about 3 to 4x the benchmark.
- The tool automatically generates a compliance_log.csv isolating all stations above the benchmark for quick review.

## Tech Stack
Language: Python  
Data Processing: Pandas  
Visualization: Matplotlib  

# About
Developed as an applied engineering project, bridging the gap between chemical process calculations and Python-driven data analysis.
