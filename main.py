from fastapi import FastAPI
import sqlite3
import pandas as pd

app = FastAPI()

@app.get("/usage")
def get_usage(year: int, operator: str):
    conn = sqlite3.connect("./data/mobile_usage.db")

    df = pd.read_sql_query(
        """
        SELECT *
        FROM mobile_usage
        WHERE year = ?
          AND operator = ?
        """,
        conn,
        params=(year, operator)
    )

    conn.close()
    return df.to_dict(orient="records")
