import sqlite3
from pathlib import Path

Path("database").mkdir(exist_ok=True)

conn = sqlite3.connect(
    "database/bluestock_mf.db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS fund_master (
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS nav_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    date DATE,
    nav REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS investor_transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    investor_id TEXT,
    transaction_date DATE,
    amount REAL
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")