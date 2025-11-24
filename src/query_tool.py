import sqlite3

DB_PATH = "../data/mobile_usage.db"

def run_query(sql):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    return rows

def show_yearly_avg():
    sql = """
    SELECT year, AVG(avg_gb)
    FROM mobile_usage
    GROUP BY year
    ORDER BY year;
    """
    data = run_query(sql)
    print("\n年度平均使用量 (GB)：")
    for row in data:
        print(f"{row[0]} 年：{row[1]:.2f} GB")

def show_operator_comparison():
    sql = """
    SELECT operator, AVG(avg_gb)
    FROM mobile_usage
    GROUP BY operator;
    """
    data = run_query(sql)
    print("\n業者平均使用量比較 (GB)：")
    for row in data:
        print(f"{row[0]}：{row[1]:.2f} GB")

def search_by_year():
    y = input("請輸入年份（例：110）：")
    sql = f"SELECT * FROM mobile_usage WHERE year = {y};"
    data = run_query(sql)
    print(f"\n{y} 年資料：")
    for row in data:
        print(row)

def search_by_operator():
    op = input("請輸入業者名稱（例：中華電信）：")
    sql = f"SELECT * FROM mobile_usage WHERE operator = '{op}';"
    data = run_query(sql)
    print(f"\n{op} 的資料：")
    for row in data:
        print(row)

def main():
    while True:
        print("\n=== 行動資料查詢工具 ===")
        print("1. 年度平均使用量")
        print("2. 業者平均使用量比較")
        print("3. 查詢指定年份")
        print("4. 查詢指定業者")
        print("5. 離開")

        choice = input("請選擇：")

        if choice == "1":
            show_yearly_avg()
        elif choice == "2":
            show_operator_comparison()
        elif choice == "3":
            search_by_year()
        elif choice == "4":
            search_by_operator()
        elif choice == "5":
            break
        else:
            print("無效選項，請重新選擇。")

if __name__ == "__main__":
    main()