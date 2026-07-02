from pathlib import Path
import pandas as pd
import sqlite3


BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
DB_PATH = BASE_DIR / "database" / "bluestock_mf.db"


def load_csv(file_name):
    """Load a CSV file safely."""
    file_path = RAW_DIR / file_name

    if not file_path.exists():
        raise FileNotFoundError(f"{file_name} not found")

    return pd.read_csv(file_path)


def save_processed(df, file_name):
    """Save processed dataframe."""
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DIR / file_name, index=False)


def load_to_sqlite(df, table_name, conn):
    """Load dataframe into SQLite."""
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"Loaded {table_name}")


def main():
    try:
        print("Starting ETL Pipeline...")

        DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(DB_PATH)

        files = {
            "01_fund_master.csv": "fund_master",
            "02_nav_history.csv": "nav_history",
            "03_aum_by_fund_house.csv": "aum_by_fund_house",
            "04_monthly_sip_inflows.csv": "monthly_sip_inflows",
            "05_category_inflows.csv": "category_inflows",
            "06_industry_folio_count.csv": "industry_folio_count",
            "07_scheme_performance.csv": "scheme_performance",
            "08_investor_transactions.csv": "investor_transactions",
            "09_portfolio_holdings.csv": "portfolio_holdings",
            "10_benchmark_indices.csv": "benchmark_indices"
        }

        for file_name, table_name in files.items():
            df = load_csv(file_name)

            # Add any cleaning logic here if required

            save_processed(df, file_name)
            load_to_sqlite(df, table_name, conn)

        conn.close()

        print("ETL completed successfully!")

    except Exception as e:
        print(f"ETL failed: {e}")


if __name__ == "__main__":
    main()