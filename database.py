import sqlite3
import pandas as pd
import os

csv_path="simulation/status.csv"
db_path="simulation/smart_home.db"

os.makedirs("simulation",exist_ok=True)

conn=sqlite3.connect(db_path)

df=pd.read_csv(csv_path)

df.to_sql(
    "sensor_data",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Database Updated Successfully")