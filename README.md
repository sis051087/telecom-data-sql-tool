# 行動寬頻用戶 SQL 查詢與資料庫管理工具  

## 📌 專案簡介  
本專案將政府開放資料「行動寬頻用戶每月平均數據用量」轉換成 **SQLite 資料庫（mobile_usage.db）**，並提供一個 **互動式查詢工具（query_tool.py）** 讓使用者能快速查詢：

- 各年度平均使用量  
- 各電信業者平均使用量比較  
- 指定年份資料查詢  
- 指定業者資料查詢  

此專案示範如何將原始 CSV 數據轉換為 **可搜尋、可統計、可擴充的資料庫系統**。

---

## 🗂️ 專案結構  
```text
telecom-data-sql-tool/
│── data/
│      ├── 行動寬頻用戶每月平均數據用量.csv
│      └── mobile_usage.db
│
│── sql/
│      └── create_table.sql
│
│── src/
│      ├── build_db.py
│      └── query_tool.py
│
│── README.md
│── requirements.txt
```

---

## ⚙️ 安裝方式（Installation）
### 1️⃣ 安裝必要套件
```
pip install -r requirements.txt
```

requirements.txt 內容：
```
pandas
```

---

## 🛠️ 建立資料庫（Build Database）
進入 src 資料夾後執行：
```
cd src
python3 build_db.py
```
成功後會在 data/ 產生：
```
mobile_usage.db
```

---

## 🔍 啟動查詢工具（Query Tool）
```
python3 query_tool.py
```

會顯示：
```
=== 行動資料查詢工具 ===
1. 年度平均使用量
2. 業者平均使用量比較
3. 查詢指定年份
4. 查詢指定業者
5. 離開
```

---

## 📊 查詢功能示例（Examples）

### 1️⃣ 年度平均使用量
```
108 年：13.52 GB
109 年：18.90 GB
110 年：24.31 GB
...
```

### 2️⃣ 業者平均使用量比較
```
中華電信：22.01 GB
遠傳電信：23.88 GB
台灣大哥大：21.65 GB
...
```

### 3️⃣ 查詢指定年份（例：110）
```
(110, 1, '中華電信', 1200000.0, 600000, 20.00)
...
```

### 4️⃣ 查詢指定業者（例：中華電信）
```
(110, 5, '中華電信', 1350000.0, 620000, 21.77)
...
```

---

## 🧠 技術亮點
- 使用 pandas 做資料清洗、欄位重命名、型別轉換  
- 設計 SQLite 資料表結構  
- Python sqlite3 執行 SQL 查詢  
- 查詢包含 GROUP BY、AVG、條件查詢  
- 自製終端機互動查詢工具

---

## 🏁 專案總結  
本專案展示 CSV 轉資料庫、SQL 查詢與 Python 自動化整合流程。  

未來可延伸：

- 月份範圍查詢  
- API / Web 查詢介面  
