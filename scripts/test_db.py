import sqlite3

conn = sqlite3.connect("database/bluestock_mf.db")

print("Database Connected Successfully")

conn.close()