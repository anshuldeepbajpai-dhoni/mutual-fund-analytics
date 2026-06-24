-- Top 5 AMCs by AUM
SELECT fund_house,aum_crore
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV
SELECT AVG(nav)
FROM fact_nav;

-- Monthly NAV Trend
SELECT strftime('%Y-%m',date),
AVG(nav)
FROM fact_nav
GROUP BY 1;

-- SIP Growth
SELECT month,
sip_inflow_crore
FROM monthly_sip_inflows;

-- Transactions by State
SELECT state,
COUNT(*)
FROM fact_transactions
GROUP BY state;

-- Expense Ratio < 1%
SELECT scheme_name,
expense_ratio_pct
FROM dim_fund d
JOIN fact_performance p
ON d.amfi_code=p.amfi_code
WHERE expense_ratio_pct < 1;

-- Top 5 Funds by 5Y Return
SELECT scheme_name,
return_5yr_pct
FROM dim_fund d
JOIN fact_performance p
ON d.amfi_code=p.amfi_code
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- Category-wise Funds
SELECT category,
COUNT(*)
FROM dim_fund
GROUP BY category;

-- Average Alpha
SELECT AVG(alpha)
FROM scheme_performance;

-- Portfolio Sector Exposure
SELECT sector,
SUM(weight_pct)
FROM portfolio_holdings
GROUP BY sector;