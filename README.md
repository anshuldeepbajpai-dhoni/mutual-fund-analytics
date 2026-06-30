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


# Day 4: Fund Performance Analytics

## Objectives

* Compute return and risk metrics for mutual fund schemes.
* Compare fund performance against benchmark indices.
* Evaluate risk-adjusted returns using financial analytics.
* Generate a composite fund ranking system.

## Performance Metrics Computed

### Daily Returns

Daily returns were calculated using:

```python
daily_return = (NAV_t / NAV_t-1) - 1
```

The distribution of daily returns was validated to identify outliers and understand volatility patterns.

### CAGR Analysis

Computed annualized returns for:

* 1-Year CAGR
* 3-Year CAGR
* 5-Year CAGR

Formula:

```python
CAGR = (NAV_end / NAV_start) ** (1 / years) - 1
```

### Sharpe Ratio

Risk-adjusted returns were calculated using a risk-free rate of 6.5%.

```python
Sharpe = (Rp - Rf) / Std(Rp) × √252
```

Funds were ranked based on annualized Sharpe ratios.

### Sortino Ratio

Downside-risk-adjusted returns were computed using only negative return observations.

```python
Sortino = (Rp - Rf) / Downside_Std × √252
```

### Alpha and Beta

Linear regression against NIFTY 100 benchmark returns was performed using SciPy.

```python
Fund Return = Alpha + Beta × Benchmark Return
```

Annualized Alpha:

```python
Alpha_Annual = Alpha × 252
```

### Maximum Drawdown

Worst peak-to-trough declines were calculated using:

```python
Max Drawdown = NAV / Running_Max - 1
```

Date ranges corresponding to maximum drawdowns were also identified.

### Fund Scorecard

A composite score out of 100 was generated using weighted rankings:

| Metric                     | Weight |
| -------------------------- | ------ |
| 3-Year CAGR                | 30%    |
| Sharpe Ratio               | 25%    |
| Alpha                      | 20%    |
| Expense Ratio (Inverse)    | 15%    |
| Maximum Drawdown (Inverse) | 10%    |

### Benchmark Comparison

The top five funds were compared with:

* NIFTY 50
* NIFTY 100

Additional metrics:

* Tracking Error
* Relative Performance Charts
* Normalized Growth Comparison

## Deliverables

* Performance_Analytics.ipynb
* fund_scorecard.csv
* alpha_beta.csv
* top5_vs_benchmark.png

## Key Findings

### Return Performance

* Several equity schemes delivered strong 3-year CAGR values and consistently outperformed benchmark indices.

### Risk-Adjusted Returns

* Funds with higher Sharpe and Sortino ratios demonstrated superior risk-adjusted performance.

### Alpha Generation

* A number of actively managed schemes generated positive alpha relative to NIFTY 100.

### Market Sensitivity

* Beta analysis revealed varying levels of market exposure across different fund categories.

### Drawdown Analysis

* Large-cap funds generally experienced lower maximum drawdowns compared to mid-cap and small-cap schemes.

### Composite Rankings

* The fund scorecard provided a balanced evaluation framework incorporating returns, risk, costs, and downside protection.

---

## Day 5: Power BI Dashboard

An interactive Power BI dashboard was developed to analyze the Indian mutual fund industry using cleaned and integrated datasets. The dashboard consists of four pages with multiple visualizations, filters, tooltips, drill-through functionality, and hierarchical navigation.

### Page 1: Industry Overview

* KPI Cards: Total AUM, SIP Inflows, Total Folios, Total Schemes
* Industry AUM Growth Trend (2022–2025)
* Top Fund Houses by AUM
* Interactive tooltips and cross-filtering

###  Page 2: Fund Performance

* Risk vs Return Scatter Plot
* NAV Trend Analysis
* Fund Performance Scorecard Table
* Slicers for Scheme Name, Fund House, Category, and Plan
* Drill-through support for detailed fund analysis

###  Page 3: Investor Analysis

* Transaction Volume by Type
* State-wise Investment Distribution Map
* Average Investment by Age Group
* Monthly Transaction Trend
* Filters for State, Gender, Age Group, and City Tier

###  Page 4: SIP & Market Trends

* SIP Inflows vs Market Performance (Dual-Axis Chart)
* Top 5 Category Inflows
* YoY SIP Growth KPI
* Filters for Date Range, Category, and Market Indices

---

## 🔗 Data Model & Hierarchy Structure

### Dataset Relationships

```text
fund_master (amfi_code)
├── fund_performance (amfi_code)
├── nav_history (amfi_code)
└── amc_aum (fund_house)

monthly_sip_inflows (month)
└── benchmark_indices (month)

investor_transactions (date)
└── monthly_sip_inflows (month)
```

### Drill-Down Hierarchies

```text
Date Hierarchy
Year
└── Quarter
    └── Month
        └── Day

Category Hierarchy
Category
└── Sub-Category

Fund Hierarchy
Fund House
└── Scheme Name
    └── Plan Type
```

### Dashboard Navigation Structure

```text
Mutual Fund Dashboard
├── Page 1: Industry Overview
├── Page 2: Fund Performance
│   └── Drill-through: Fund NAV Details
├── Page 3: Investor Analysis
└── Page 4: SIP & Market Trends
```

---

## Dashboard Features

* Interactive slicers and cross-filtering
* Tooltips on all major visualizations
* Drill-through navigation for fund details
* Date and category hierarchies for drill-down analysis
* Bluestock branding and custom theme
* Exported in PBIX, PDF, and PNG formats

## Deliverables

* `bluestock_mf_dashboard.pbix`
* `Dashboard.pdf`
* `Dashboard_Page_01.png`
* `Dashboard_Page_02.png`
* `Dashboard_Page_03.png`
* `Dashboard_Page_04.png`

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
├── dashboard/
│   ├── bluestock_mf_dashboard.pbix
│   ├── Dashboard_Page_01.png
│   ├── Dashboard_Page_02.png
│   ├── Dashboard_Page_03.png
│   ├── Dashboard_Page_04.png
│   └── Dashboard.pdf
│ 
├── notebooks/
│   ├── Day1_Data_Ingestion.ipynb
│   ├── Day2_Data_Cleaning.ipynb
│   ├── EDA_Analysis.ipynb
│   └── Performance_Analytics.ipynb
│
├── scripts/
│   ├── check_columns.py
│   ├── clean_data.py
│   ├── create_db.py
│   ├── data_ingestion.py
│   ├── live_nav_fetch.py
│   ├── load_data.py
│   ├── test_db.py
│   ├── validation.py
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
│   ├── sector_allocation.png
│   ├── nav_trend.png
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
│   ├── day1_summary.md
│   ├── day2_summary.md
│   ├── Data_dictionary.md
│   ├── EDA_findings.md
│   └── Fund_Performance_Analytics.md
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
