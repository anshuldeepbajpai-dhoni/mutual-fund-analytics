# Data Dictionary

## Project

Mutual Fund Analytics Capstone Project

## Dataset 1: Fund Master

| Column Name   | Data Type | Description                    |
| ------------- | --------- | ------------------------------ |
| amfi_code     | Integer   | Unique AMFI scheme identifier  |
| scheme_name   | Text      | Name of the mutual fund scheme |
| fund_house    | Text      | Asset Management Company (AMC) |
| category      | Text      | Scheme category                |
| sub_category  | Text      | Scheme sub-category            |
| plan          | Text      | Direct/Regular plan            |
| risk_category | Text      | Risk classification            |

Source: 01_fund_master.csv

---

## Dataset 2: NAV History

| Column Name | Data Type | Description              |
| ----------- | --------- | ------------------------ |
| amfi_code   | Integer   | Unique scheme identifier |
| date        | Date      | NAV date                 |
| nav         | Decimal   | Net Asset Value          |

Source: 02_nav_history.csv

---

## Dataset 3: AUM by Fund House

| Column Name | Data Type | Description                       |
| ----------- | --------- | --------------------------------- |
| date        | Date      | Reporting date                    |
| fund_house  | Text      | AMC name                          |
| aum_crore   | Decimal   | Assets Under Management (Crore ₹) |

Source: 03_aum_by_fund_house.csv

---

## Dataset 4: Monthly SIP Inflows

| Column Name      | Data Type | Description                 |
| ---------------- | --------- | --------------------------- |
| month            | Text      | Reporting month             |
| sip_inflow_crore | Decimal   | SIP inflow amount (Crore ₹) |

Source: 04_monthly_sip_inflows.csv

---

## Dataset 5: Category Inflows

| Column Name  | Data Type | Description                 |
| ------------ | --------- | --------------------------- |
| category     | Text      | Mutual fund category        |
| inflow_crore | Decimal   | Net inflow amount (Crore ₹) |

Source: 05_category_inflows.csv

---

## Dataset 6: Industry Folio Count

| Column Name | Data Type | Description               |
| ----------- | --------- | ------------------------- |
| month       | Text      | Reporting month           |
| folio_count | Integer   | Number of investor folios |

Source: 06_industry_folio_count.csv

---

## Dataset 7: Scheme Performance

| Column Name       | Data Type | Description             |
| ----------------- | --------- | ----------------------- |
| amfi_code         | Integer   | Scheme identifier       |
| return_1yr_pct    | Decimal   | One year return (%)     |
| return_3yr_pct    | Decimal   | Three year return (%)   |
| return_5yr_pct    | Decimal   | Five year return (%)    |
| alpha             | Decimal   | Alpha measure           |
| beta              | Decimal   | Beta measure            |
| sharpe_ratio      | Decimal   | Sharpe Ratio            |
| expense_ratio_pct | Decimal   | Expense ratio (%)       |
| aum_crore         | Decimal   | Assets under management |

Source: 07_scheme_performance.csv

---

## Dataset 8: Investor Transactions

| Column Name      | Data Type | Description             |
| ---------------- | --------- | ----------------------- |
| transaction_id   | Integer   | Transaction identifier  |
| investor_id      | Text      | Investor identifier     |
| transaction_date | Date      | Transaction date        |
| amfi_code        | Integer   | Scheme identifier       |
| transaction_type | Text      | SIP/Lumpsum/Redemption  |
| amount_inr       | Decimal   | Transaction amount (₹)  |
| state            | Text      | Investor state          |
| kyc_status       | Text      | KYC verification status |

Source: 08_investor_transactions.csv

---

## Dataset 9: Portfolio Holdings

| Column Name  | Data Type | Description              |
| ------------ | --------- | ------------------------ |
| amfi_code    | Integer   | Scheme identifier        |
| company_name | Text      | Company name             |
| sector       | Text      | Industry sector          |
| weight_pct   | Decimal   | Portfolio allocation (%) |

Source: 09_portfolio_holdings.csv

---

## Dataset 10: Benchmark Indices

| Column Name    | Data Type | Description          |
| -------------- | --------- | -------------------- |
| date           | Date      | Index date           |
| benchmark_name | Text      | Benchmark index name |
| close_value    | Decimal   | Closing index value  |
| return_pct     | Decimal   | Benchmark return (%) |

Source: 10_benchmark_indices.csv

---

# Data Quality Checks Performed

* Removed duplicate records
* Converted date fields to datetime format
* Checked missing values
* Validated NAV values greater than zero
* Standardized transaction types
* Validated transaction amounts
* Verified KYC status values
* Checked expense ratio ranges
* Verified numeric return fields

---

# Database

Database Name: bluestock_mf.db

Database Type: SQLite

Schema Type: Star Schema

Dimension Tables:

* dim_fund
* dim_date

Fact Tables:

* fact_nav
* fact_transactions
* fact_performance
* fact_aum
