import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///database/bluestock_mf.db"
)

processed_path = Path("data/processed")

for file in processed_path.glob("*_clean.csv"):

    df = pd.read_csv(file)

    table_name = file.stem.replace(
        "_clean",
        ""
    )

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"Loaded: {table_name}")

print("All tables loaded successfully.")