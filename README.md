# Yamuna River BOD Compliance Checker

A Python-based environmental data analysis tool that evaluates the Biochemical Oxygen Demand (BOD) of the Yamuna River using official Central Pollution Control Board (CPCB) monitoring data from 2024 and 2025.

 ## Project Overview
Surface water monitoring datasets often exist in static PDF reports, making year-over-year compliance tracking difficult. This script automates regulatory benchmarking against official CPCB limits. 

It processes geographic monitoring stations (from Yamunotri down to Etawah), calculates average BOD levels, and visually flags stations exceeding the safe limit of 3.0 mg/L.

## Key Insights
* Upstream stations remain well within legal limits.
* Entering urban corridors causes BOD levels to spike massively, exceeding safe limits by over 20x.
* The tool automatically generates a `compliance_log.csv` isolating all violating stations for quick executive review.

## Tech Stack
Language: Python  
Data Processing: Pandas  
Visualization: Matplotlib  

# About
Developed as an applied engineering project, bridging the gap between chemical process calculations and Python-driven data analysis.
