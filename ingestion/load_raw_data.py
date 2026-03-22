import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
"postgresql://opspulse:opspulse@localhost:5432/opspulse_dw"
)

tables = {
"teams": "data/raw/teams/teams.csv",
"services": "data/raw/services/services.csv",
"deployments": "data/raw/deployments/deployments.csv",
"incidents": "data/raw/incidents/incidents.csv"
}

for table, path in tables.items():

    df = pd.read_csv(path)

    df.to_sql(
        table,
        engine,
        schema="raw",
        if_exists="replace",
        index=False
    )

    print(f"Loaded {len(df)} rows into raw.{table}")
