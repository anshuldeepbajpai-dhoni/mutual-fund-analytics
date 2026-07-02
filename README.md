# Bluestock Mutual Fund Analytics/Capstone Program

An end-to-end fintech analytics project developed as part of the **Bluestock Fintech Data Analyst Capstone Program**. The project builds a complete mutual fund analytics ecosystem, including ETL pipelines, SQL database design, exploratory data analysis, performance and risk metrics, advanced analytics, and an interactive Power BI dashboard.

---

## Project Objective

The objective of this project is to create a data-driven mutual fund analytics platform that helps investors and analysts:

- Compare fund performance using risk-adjusted metrics.
- Track industry trends in AUM, SIP inflows, and folio growth.
- Analyze investor demographics and transaction behavior.
- Evaluate funds against benchmark indices.
- Generate actionable insights through dashboards and advanced analytics.

## Updated Project Structure

```text
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
│       ├── 01_fund_master_clean.csv
│       ├── 02_nav_history_clean.csv
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
│   └── bluestock_mf.db
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── Final_Submission/
│   ├── schema.sql
│   └── queries.sql
│ 
├── dashboard/
│   ├── bluestock_mf_dashboard.pbix
│   ├── Dashboard_Page_01.png
│   ├── Dashboard_Page_02.png
│   ├── Dashboard_Page_03.png
│   ├── Dashboard_Page_04.png
│   └── Dashboard.pdf
│ 
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_EDA_analysis.ipynb
│   ├── 04_Performance_Analytics.ipynb
│   └── 05_Advanced_analytics.ipynb
│
├── scripts/
│   ├── check_columns.py
│   ├── clean_data.py
│   ├── compute_metrics.py
│   ├── create_db.py
│   ├── data_ingestion.py
│   ├── etl_pipeline.py
│   ├── live_nav_fetch.py
│   ├── load_data.py
│   ├── recommender.py
│   ├── test_db.py
│   └── validation.py
│
├── charts/
│   ├── age_distribution.png
│   ├── aum_growth
│   ├── benchmark_trend.png
│   ├── category_heatmap.png
│   ├── correlation_matrix.png
│   ├── daily_distribution.png
│   ├── folio_growth.png
│   ├── gender_distribution.png
│   ├── nav_trend.png
│   ├── risk_return.png
│   ├── rolling_sharpe_chart.png
│   ├── sector_allocation.png
│   ├── sector_hhi_comparison.png
│   ├── sector_market_value.png
│   ├── sip_boxplot.png
│   ├── sip_trend.png
│   ├── sip_trend2.png
│   ├── state_transactions.png
│   ├── stock_price_dist.png
│   ├── t30_b30.png
│   ├── top_holdings.png
│   └──top5_vs_benchmark.png
│
├── outputs/
│   ├── cagr_analysis.csv
│   ├── sharpe_ratio.csv
│   ├── sortino_ratio.csv
│   ├── alpha_beta.csv
│   ├── max_drawdown.csv
│   ├── tracking_error.csv
│   └── fund_scorecard.csv
│
├── reports/
│   ├── Advanced_insights.md
│   ├── day1_summary.md
│   ├── day2_summary.md
│   ├── Data_dictionary.md
│   ├── EDA_findings.md
│   └── Fund_Performance_Analytics.md
│ 
├── reports_adv_ana/
│   ├── cohort_analysis.csv
│   ├── sector_hhi_report.csv
│   ├── sip_continuity_report.csv
│   └── var_cvar_report.csv
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Author

**Anshul Deep Bajpai**
B.Tech (CSE - AI & ML)
MG Institute of Management and Technology, Lucknow




## 📈 Dataset Overview

| Dataset | Records |
|----------|----------|
| Fund Master | 40 |
| NAV History | 46,000 |
| AUM by Fund House | 90 |
| Monthly SIP Inflows | 48 |
| Category Inflows | 144 |
| Industry Folio Count | 21 |
| Scheme Performance | 40 |
| Investor Transactions | 32,778 |
| Portfolio Holdings | 322 |
| Benchmark Indices | 8,050 |

### Key Statistics

- **40 Mutual Fund Schemes**
- **10 Fund Houses**
- **46K NAV Records**
- **32.8K Transactions**
- **5,000 Investors**
- **4.5 Years of Historical Data**

---

## ⚙️ Technology Stack

### Programming & Analytics
- Python
- Pandas
- NumPy
- SciPy
- Scikit-Learn

### Database
- SQLite
- SQL

### Visualization
- Matplotlib
- Seaborn
- Power BI

### Development Tools
- Jupyter Notebook
- VS Code
- Git & GitHub

---

## 🔄 ETL Pipeline

The ETL workflow follows:

```text
Extract → Transform → Load → Analyse → Visualise
```

### Extract
- Load 10 raw CSV datasets
- Validate schema and datatypes

### Transform
- Handle missing values
- Forward-fill NAV data for non-trading days
- Standardize categorical variables
- Validate business rules

### Load
- Store cleaned data in:
  - Processed CSV files
  - SQLite database

### Analyse
Compute:

- CAGR
- Sharpe Ratio
- Sortino Ratio
- Alpha
- Beta
- Maximum Drawdown
- VaR
- CVaR
- Composite Fund Score

---

## 🗄️ Database Design

The project uses a **Star Schema**:

### Dimension Table
- dim_fund

### Fact Tables
- fact_nav
- fact_transactions
- fact_performance
- fact_portfolio
- fact_aum
- fact_sip_industry
- fact_category_inflows
- fact_folio_count
- fact_benchmark

Indexes are created on:

- amfi_code
- date

for efficient querying.

---

## 🔍 Exploratory Data Analysis

The EDA notebook contains **16 analytical visualizations**, including:

### Industry Analysis
- AUM Growth by Fund House
- Monthly SIP Trends
- Folio Growth

### Fund Analysis
- NAV Trends
- Return Correlation Heatmaps
- Category-wise Inflows

### Investor Analysis
- Age Group Distribution
- SIP Amount Analysis
- Geographic Distribution
- T30 vs B30 Analysis

### Portfolio Analysis
- Sector Allocation
- Concentration Risk

---

## 📊 Performance Analytics

The project computes:

| Metric | Description |
|----------|-------------|
| CAGR | Annualized Growth Rate |
| Sharpe Ratio | Risk-Adjusted Return |
| Sortino Ratio | Downside Risk Measure |
| Alpha | Excess Return vs Benchmark |
| Beta | Market Sensitivity |
| Maximum Drawdown | Worst Peak-to-Trough Decline |
| VaR (95%) | Value at Risk |
| CVaR | Conditional Value at Risk |

---

## 🏆 Composite Fund Scorecard

The final score is calculated as:

```text
Score =
30% × 3-Year Return
+ 25% × Sharpe Ratio
+ 20% × Alpha
+ 15% × Expense Ratio (Inverse)
+ 10% × Maximum Drawdown (Inverse)
```

### Top Ranked Fund

**Kotak Flexicap Fund - Regular Growth**

- Score: 71.8/100
- 3-Year Return: 15.7%

---

## 🧠 Advanced Analytics

The advanced analytics module includes:

### Risk Analytics
- Historical VaR (95%)
- Conditional VaR (CVaR)
- Rolling Sharpe Ratios

### Investor Behaviour Analysis
- Age Cohorts
- City Tier Analysis
- Income Group Analysis
- Transaction Patterns

### Recommendation System
Risk-based fund recommendations:

### Conservative
- Debt Funds
- Low Beta
- Low Drawdown

### Moderate
- Hybrid Funds
- Balanced Risk Profiles

### Aggressive
- Equity Funds
- High CAGR
- Higher Risk Tolerance

---

## 📊 Interactive Dashboard

The Power BI dashboard consists of **4 pages**:

### 1. Industry Overview
- KPI Cards
- AUM Trends
- AMC Comparison

### 2. Fund Performance
- Return vs Risk Analysis
- Composite Scorecard
- NAV vs Benchmark

### 3. Investor Analytics
- Geographic Distribution
- Demographics
- Transaction Patterns

### 4. SIP & Market Trends
- SIP Inflows
- Benchmark Movements
- Category Inflows

Every page includes interactive slicers for:

- Fund House
- Category
- State
- Age Group
- City Tier

---

## 📌 Key Findings

- SIP inflows reached **₹31,002 Cr** in Dec-2025.
- Total mutual fund folios doubled from **13.26 Cr to 26.12 Cr**.
- SBI Mutual Fund leads industry AUM with **₹12.5 Lakh Cr**.
- Small-cap funds exhibit the highest volatility and VaR.
- T30 cities contribute approximately **66%** of transaction volume.
- Banking and IT dominate sector allocations.

---

## 🚀 How to Run

### Clone Repository

```bash
git clone https://github.com/anshuldeepbajpai-dhoni/Bluestock-mutual-fund-analytics.git
cd bluestock-mf-capstone
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run ETL Pipeline

```bash
python scripts/etl_pipeline.py
```

### Compute Metrics

```bash
python scripts/compute_metrics.py
```

### Run Recommender

```bash
python scripts/recommender.py
```

---

## 📑 Deliverables

| ID | Deliverable | Status |
|----|-------------|---------|
| D1 | ETL Pipeline | ✅ |
| D2 | SQLite Database | ✅ |
| D3 | EDA Analysis | ✅ |
| D4 | Performance Metrics | ✅ |
| D5 | Power BI Dashboard | ✅ |
| D6 | Advanced Analytics | ✅ |
| D7 | Final Report & Presentation | ✅ |

---

## 📚 Data Sources

- AMFI India
- mfapi.in
- NSE India
- BSE India

All data is used strictly for educational purposes.

---

## 👨‍💻 Author

**Anshul Deep Bajpai**  
B.Tech (AI & ML) | MG Institute of Management & Technology, Lucknow  
Data Analyst Intern – Bluestock Fintech

---

## ⚠️ Disclaimer

This project is developed solely for educational and academic purposes. It does not constitute investment advice. Mutual fund investments are subject to market risks. Please read all scheme-related documents carefully before investing.