CREATE TABLE IF NOT EXISTS mobile_usage (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    year INTEGER,
    month INTEGER,
    operator TEXT,
    total_gb REAL,
    users INTEGER,
    avg_gb REAL
);