import sqlite3
import pandas as pd
import os

# 讀取資料
year_folder = "src/../output_by_year"

all_data = []

for file in os.listdir(year_folder):
    if file.endswith(".xlsx"):
        path = os.path.join(year_folder, file)
        df = pd.read_excel(path)
        all_data.append(df)

df = pd.concat(all_data, ignore_index=True)

# 統一欄位
df = df.rename(columns={
    "年": "year",
    "月": "month",
    "業者名稱": "operator",
    "數據傳輸量（GBytes）": "total_gb",
    "用戶數": "users",
    "平均每一用戶數據傳輸量（GBytes）": "avg_gb"
})

# 寫入 
db_path = "src/../data/mobile_usage.db"
conn = sqlite3.connect(db_path)

df.to_sql("mobile_usage", conn, if_exists="replace", index=False)

conn.close()

print("SQLite 資料庫建立完成！來源：output_by_year 內的整理後資料")
