CREATE SCHEMA IF NOT EXISTS mutual_funds;

CREATE TABLE mutual_funds.01_fund_master (
    amfi_code BIGINT PRIMARY KEY,
    fund_house VARCHAR(255),
    scheme_name VARCHAR(500),
    category VARCHAR(255),
    sub_category VARCHAR(255),
    plan VARCHAR(100),
    launch_date DATE,
    benchmark VARCHAR(500),
    expense_ratio_pct NUMERIC(6,2),
    exit_load_pct NUMERIC(6,2),
    min_sip_amount NUMERIC(12,2),
    min_lumpsum_amount NUMERIC(12,2),
    fund_manager VARCHAR(255),
    risk_category VARCHAR(100),
    sebi_category_code VARCHAR(50)
);

CREATE TABLE mutual_funds.02_nav_history (
    amfi_code BIGINT,
    nav_date DATE,
    nav NUMERIC(10,4)
);