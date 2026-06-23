import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Extract unique AMFI codes
master_codes = set(fund_master["amfi_code"].unique())
nav_codes = set(nav_history["amfi_code"].unique())

# Validation
missing_codes = master_codes - nav_codes
matched_codes = master_codes.intersection(nav_codes)

print("=" * 60)
print("AMFI CODE VALIDATION REPORT")
print("=" * 60)

print(f"Total Fund Master Codes : {len(master_codes)}")
print(f"Total NAV History Codes : {len(nav_codes)}")
print(f"Matched Codes           : {len(matched_codes)}")
print(f"Missing Codes           : {len(missing_codes)}")

if len(missing_codes) > 0:
    print("\nSample Missing Codes:")
    print(list(missing_codes)[:20])
else:
    print("\n✅ All Fund Master AMFI Codes exist in NAV History.")

print("\n" + "=" * 60)
print("DATA QUALITY SUMMARY")
print("=" * 60)

print(f"Fund Master Rows        : {len(fund_master):,}")
print(f"NAV History Rows        : {len(nav_history):,}")

print(f"\nFund Master Missing Values : {fund_master.isnull().sum().sum()}")
print(f"NAV History Missing Values : {nav_history.isnull().sum().sum()}")

print(f"\nFund Master Duplicates     : {fund_master.duplicated().sum()}")
print(f"NAV History Duplicates     : {nav_history.duplicated().sum()}")

print("\nValidation Completed Successfully.")