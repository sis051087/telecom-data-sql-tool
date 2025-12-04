import sqlite3
import pandas as pd

# 讀取CSV
df = pd.read_csv("src/../data/行動寬頻用戶每月平均數據用量.csv")

# 清理欄位
df.columns = df.columns.str.strip()

# 年月
df["year"] = df["年月"].astype(str).str.split("/").str[0].astype(int)
df["month"] = df["年月"].astype(str).str.split("/").str[1].astype(int)

# 英文
df = df.rename(columns={
    "業者名稱": "operator",
    "數據傳輸量（GBytes）": "total_gb",
    "用戶數": "users",
    "平均每一用戶數據傳輸量（GBytes）": "avg_gb",
})

# 要存入 DB 的欄位
df = df[["year", "month", "operator", "total_gb", "users", "avg_gb"]]

# 建立 SQLite 資料庫
conn = sqlite3.connect("../data/mobile_usage.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS mobile_usage (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    year INTEGER,
    month INTEGER,
    operator TEXT,
    total_gb REAL,
    users INTEGER,
    avg_gb REAL
);
""")

# 寫入 DB
df.to_sql("mobile_usage", conn, if_exists="append", index=False)

conn.commit()
conn.close()

print("資料庫建立完成！mobile_usage.db 已建立。")
