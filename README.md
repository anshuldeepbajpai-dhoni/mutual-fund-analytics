# Mutual Fund Analytics Capstone

## Project Overview

This project focuses on analyzing India's mutual fund ecosystem using data engineering, exploratory data analysis, and performance analytics techniques. The objective is to derive actionable insights from NAV, AUM, SIP, folio, portfolio holdings, and benchmark datasets.

---

## Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* Jupyter Notebook
* Git & GitHub

---

# Day 1: Data Collection & Ingestion

## Objectives

* Collect mutual fund datasets from multiple sources.
* Organize raw data into a structured project directory.
* Create a reproducible data pipeline.

## Tasks Completed

* Downloaded and organized all required datasets.
* Created project folder structure.
* Added raw datasets to the repository.
* Initialized Git and GitHub version control.

## Deliverables

* Raw CSV datasets
* Project directory structure
* Initial documentation

---

# Day 2: Data Cleaning & Preprocessing

## Objectives

* Clean and standardize all datasets.
* Handle missing values and duplicates.
* Convert date columns into proper datetime formats.
* Export processed datasets for analysis.

## Tasks Completed

* Removed duplicate records.
* Handled missing values using appropriate techniques.
* Standardized column names and formats.
* Converted date fields to datetime objects.
* Exported cleaned datasets.

## Processed Files

* 03_aum_by_fund_house_clean.csv
* 04_monthly_sip_clean.csv
* 05_category_inflows_clean.csv
* 06_industry_folio_count_clean.csv
* 07_scheme_performance_clean.csv
* 08_investor_transactions_clean.csv
* 09_portfolio_holdings_clean.csv
* 10_benchmark_indices_clean.csv

## Deliverables

* Data_Cleaning.ipynb
* Cleaned CSV files
* Data quality report

---

# Day 3: Exploratory Data Analysis (EDA)

## Objectives

* Perform exploratory analysis on mutual fund datasets.
* Identify market trends and investment patterns.
* Analyze fund performance and risk metrics.
* Generate publication-quality visualizations.

## Visualizations Created

* NAV Trend Analysis
* SIP Inflow Trend
* Category Inflow Heatmap
* MF Folio Growth Analysis
* State-wise Transaction Distribution
* T30 vs B30 Contribution Analysis
* Sector Allocation Donut Chart
* Sector Concentration (HHI) Analysis
* Rolling 90-Day Sharpe Ratio
* VaR vs CVaR Risk Analysis
* Risk vs Return Bubble Plot
* Fund vs Benchmark Comparison
* Daily Return Correlation Heatmap
* Investor Cohort SIP Analysis
* Top Holdings and Portfolio Analytics

## Key Findings

### Industry Growth

* Total mutual fund folios increased from 13.26 crore to 26.12 crore between 2022 and 2025.

### SIP Trends

* Monthly SIP inflows showed consistent growth, indicating increasing investor participation.

### Geographic Insights

* T30 cities contributed approximately 65.9% of total investments, while B30 cities contributed 34.1%.

### Sector Allocation

* Banking, IT, Pharma, and Automobile sectors dominated portfolio allocations.

### Risk Analysis

* Small-cap and mid-cap funds delivered higher returns but exhibited greater volatility and downside risk.

### Benchmark Performance

* Several actively managed funds outperformed NIFTY 50 and NIFTY 100 benchmarks over the study period.

### Diversification

* Correlation analysis demonstrated moderate diversification opportunities across fund categories.

## Deliverables

* EDA_Analysis.ipynb
* EDA Findings Summary
* 15+ Visualizations
* Exported PNG Charts

---

## Project Structure

mutual-fund-analytics/
│
├── data/
│   ├── raw/
│   │   ├── 01_nav_history.csv
│   │   ├── 02_fund_metadata.csv
│   │   ├── 03_aum_by_fund_house.csv
│   │   ├── 04_monthly_sip_inflows.csv
│   │   ├── 05_category_inflows.csv
│   │   ├── 06_industry_folio_count.csv
│   │   ├── 07_scheme_performance.csv
│   │   ├── 08_investor_transactions.csv
│   │   ├── 09_portfolio_holdings.csv
│   │   └── 10_benchmark_indices.csv
│   │
│   └── processed/
│       ├── 03_aum_by_fund_house_clean.csv
│       ├── 04_monthly_sip_inflows_clean.csv
│       ├── 05_category_inflows_clean.csv
│       ├── 06_industry_folio_count_clean.csv
│       ├── 07_scheme_performance_clean.csv
│       ├── 08_investor_transactions_clean.csv
│       ├── 09_portfolio_holdings_clean.csv
│       └── 10_benchmark_indices_clean.csv
│
├── database/
│   ├── mutual_fund.db
│   ├── schema.sql
│   └── queries.sql
│
├── notebooks/
│   ├── Day1_Data_Ingestion.ipynb
│   ├── Day2_Data_Cleaning.ipynb
│   └── EDA_Analysis.ipynb
│
├── charts/
│   ├── nav_trend.png
│   ├── sip_trend.png
│   ├── category_heatmap.png
│   ├── folio_growth.png
│   ├── state_transactions.png
│   ├── t30_b30_distribution.png
│   ├── sector_allocation.png
│   ├── sector_concentration_hhi.png
│   ├── sharpe_ratio.png
│   ├── var_cvar.png
│   ├── fund_vs_benchmark.png
│   ├── investor_cohort_sip.png
│   ├── correlation_heatmap.png
│   └── risk_return_bubble.png
│
├── reports/
│   ├── Data_Quality_Report.md
│   └── EDA_Findings.md
│
├── requirements.txt
├── README.md
└── .gitignore

---

## Author

**Anshul Deep Bajpai**
B.Tech (CSE - AI & ML)
MG Institute of Management and Technology, Lucknow
