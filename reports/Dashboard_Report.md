# Day 5 Report: Power BI Mutual Fund Dashboard

## Overview

This task focused on developing an interactive Power BI dashboard for analyzing the Indian mutual fund industry. The dashboard integrates multiple cleaned datasets and provides insights into industry growth, fund performance, investor behavior, and SIP trends through visual analytics and interactive features.

---

## Objectives

* Import and model cleaned mutual fund datasets.
* Build a multi-page interactive Power BI dashboard.
* Implement relationships using common keys.
* Add tooltips, slicers, drill-through, and drill-down functionality.
* Apply Bluestock branding and theme.
* Export dashboard deliverables in multiple formats.

---

## Data Integration

The following datasets were imported into Power BI:

* Fund Master
* Fund Performance
* NAV History
* AMC AUM Data
* Monthly SIP Inflows
* Benchmark Indices
* Investor Transactions
* Category Inflows

Relationships were created using `amfi_code`, `fund_house`, `month`, and `date` fields to enable cross-filtering and integrated analysis.

---

## Data Model Structure

```text
fund_master (amfi_code)
├── fund_performance (amfi_code)
├── nav_history (amfi_code)
└── amc_aum (fund_house)

monthly_sip_inflows (month)
└── benchmark_indices (month)

investor_transactions (date)
└── category_inflows (month)
```

---

## Dashboard Structure

```text
Mutual Fund Dashboard
├── Page 1: Industry Overview
├── Page 2: Fund Performance
│   └── Drill-through: Fund NAV Details
├── Page 3: Investor Analysis
└── Page 4: SIP & Market Trends
```

---

## Page 1: Industry Overview

### Visualizations

* KPI Cards

  * Total AUM
  * SIP Inflows
  * Total Folios
  * Total Schemes
* Industry AUM Growth Trend (2022–2025)
* Top Fund Houses by AUM

### Features

* Interactive tooltips
* Cross-filtering
* Consistent dashboard theme

---

## Page 2: Fund Performance

### Visualizations

* Risk vs Return Scatter Plot
* NAV Trend Analysis
* Fund Performance Scorecard Table
* Fund Selection Slicers

### Features

* Tooltips on all charts
* Drill-through to detailed NAV page
* Dynamic filtering by category, plan, and fund house

---

## Page 3: Investor Analysis

### Visualizations

* Transaction Volume by Type
* State-wise Investment Distribution
* Average Investment by Age Group
* Monthly Transaction Trends

### Features

* State filters
* Gender filters
* City Tier filters
* Age Group filters

---

## Page 4: SIP & Market Trends

### Visualizations

* SIP Inflows vs Market Performance
* Top 5 Category Inflows
* YoY SIP Growth KPI
* Portfolio Holdings Table

### Features

* Date-based filtering
* Category filtering
* Index selection

---

## Hierarchy Structure

### Date Hierarchy

```text
Year
└── Quarter
    └── Month
        └── Day
```

### Fund Hierarchy

```text
Fund House
└── Scheme Name
    └── Plan Type
```

### Category Hierarchy

```text
Category
└── Sub-Category
```

---

## Interactive Features

The dashboard includes several interactive capabilities:

* Slicers and filters
* Cross-filtering between visuals
* Tooltips on all major charts
* Drill-through navigation
* Drill-down hierarchies
* Bluestock branding and theme integration

---

## Deliverables

The following files were generated and submitted:

```text
bluestock_mf_dashboard.pbix
Dashboard.pdf
page1.png
page2.png
page3.png
page4.png
```

---

## Conclusion

The Power BI Mutual Fund Dashboard successfully transforms raw financial datasets into meaningful business insights through interactive visualizations and analytics. The project demonstrates practical skills in data modeling, dashboard design, business intelligence, and user-centric visualization using Microsoft Power BI.
