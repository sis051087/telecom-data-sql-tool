from fastapi import FastAPI
import sqlite3
import pandas as pd

app = FastAPI()

@app.get("/usage")
def get_usage(year: int, operator: str):
    conn = sqlite3.connect("./data/mobile_usage.db")
    df = pd.read_sql_query(f"SELECT * FROM table WHERE year={year} AND operator='{operator}'", conn)
    return df.to_dict()
