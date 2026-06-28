# Fund Performance Analytics

## Overview

This module performs advanced performance analysis on mutual fund schemes using historical NAV data and benchmark indices. The objective is to evaluate returns, risk, and overall fund quality through multiple financial metrics.

---

## Objectives

* Calculate daily returns for all mutual fund schemes.
* Measure annualized returns using CAGR.
* Evaluate risk-adjusted performance using Sharpe and Sortino ratios.
* Compute Alpha and Beta relative to benchmark indices.
* Analyze maximum drawdowns.
* Generate a composite fund scorecard.
* Compare top-performing funds against benchmark indices.

---

## Datasets Used

| Dataset                          | Description                                           |
| -------------------------------- | ----------------------------------------------------- |
| `02_nav_history_clean.csv`       | Historical NAV values for all mutual fund schemes     |
| `10_benchmark_indices_clean.csv` | Nifty 50 and Nifty 100 benchmark data                 |
| `01_fund_master_clean.csv`       | Fund metadata including expense ratios and categories |

---

## Performance Metrics

### 1. Daily Returns

Daily returns are calculated using:

```python
daily_return = (NAV_t / NAV_(t-1)) - 1
```

This metric measures the day-to-day percentage change in fund NAV.

---

### 2. Compound Annual Growth Rate (CAGR)

CAGR is computed for:

* 1 Year
* 3 Years
* 5 Years

Formula:

```python
CAGR = (NAV_end / NAV_start) ** (1 / years) - 1
```

CAGR provides a standardized measure of long-term investment growth.

---

### 3. Sharpe Ratio

The Sharpe Ratio evaluates risk-adjusted returns:

```python
Sharpe = (Rp - Rf) / Std(Rp) * sqrt(252)
```

Where:

* Rp = Average daily return
* Rf = Risk-free rate (6.5%)
* Std(Rp) = Standard deviation of returns

Higher values indicate better risk-adjusted performance.

---

### 4. Sortino Ratio

Sortino Ratio focuses only on downside volatility:

```python
Sortino = (Rp - Rf) / Downside_Std * sqrt(252)
```

This provides a more accurate assessment of downside risk.

---

### 5. Alpha and Beta

Alpha and Beta are estimated using linear regression against Nifty 100 returns.

```python
Fund Return = Alpha + Beta × Benchmark Return
```

Definitions:

* Alpha measures excess return over the benchmark.
* Beta measures market sensitivity.

Annualized Alpha:

```python
Alpha_Annual = Alpha × 252
```

---

### 6. Maximum Drawdown

Maximum Drawdown measures the largest decline from a historical peak.

Formula:

```python
Max Drawdown = NAV / Running_Max - 1
```

This metric helps evaluate downside risk during market corrections.

---

## Fund Scorecard

A composite score out of 100 is generated using weighted rankings:

| Metric                     | Weight |
| -------------------------- | ------ |
| 3-Year CAGR                | 30%    |
| Sharpe Ratio               | 25%    |
| Alpha                      | 20%    |
| Expense Ratio (Inverse)    | 15%    |
| Maximum Drawdown (Inverse) | 10%    |

The final score helps identify top-performing mutual fund schemes.

---

## Benchmark Comparison

The top five funds are compared against:

* Nifty 50
* Nifty 100

Analysis includes:

* Normalized performance charts
* Tracking error calculations

Tracking Error Formula:

```python
Tracking Error = Std(Fund Return - Benchmark Return) * sqrt(252)
```

---

## Deliverables

The following outputs are generated:

```text
Performance_Analytics.ipynb
fund_scorecard.csv
alpha_beta.csv
top5_vs_benchmark.png
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* SciPy
* Jupyter Notebook

---

## Key Outcomes

* Evaluated mutual fund performance using return and risk metrics.
* Identified top-performing funds through composite scoring.
* Compared fund performance against benchmark indices.
* Measured downside risk using drawdown and Sortino analysis.
* Generated analytical outputs for reporting and visualization.
