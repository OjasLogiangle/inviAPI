# db_setup.py
import sqlite3

DB_PATH = "company.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Drop old tables if exist
    cur.execute("DROP TABLE IF EXISTS sales")
    cur.execute("DROP TABLE IF EXISTS purchases")

    # Create sales table
    cur.execute("""
    CREATE TABLE sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id TEXT NOT NULL,
        client_name TEXT NOT NULL,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        total_amount REAL NOT NULL,
        status TEXT NOT NULL
    )
    """)

    # Create purchases table
    cur.execute("""
    CREATE TABLE purchases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vendor_id TEXT NOT NULL,
        vendor_name TEXT NOT NULL,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        total_amount REAL NOT NULL,
        status TEXT NOT NULL
    )
    """)

    # Insert placeholder sales
    sales_data = [
        ("C001", "Alpha Retail", "2025-09-01", "10:15:00", 1250.75, "pending"),
        ("C002", "Beta Traders", "2025-09-01", "11:30:00", 3200.00, "paid"),
        ("C003", "Gamma Distributors", "2025-09-02", "14:20:00", 560.40, "overdue")
    ]
    cur.executemany("INSERT INTO sales (client_id, client_name, date, time, total_amount, status) VALUES (?, ?, ?, ?, ?, ?)", sales_data)

    # Insert placeholder purchases
    purchase_data = [
        ("V001", "Delta Supplies", "2025-09-01", "09:10:00", 2000.00, "paid"),
        ("V002", "Epsilon Imports", "2025-09-02", "12:45:00", 1500.50, "pending"),
        ("V003", "Zeta Exporters", "2025-09-02", "16:05:00", 750.25, "paid")
    ]
    cur.executemany("INSERT INTO purchases (vendor_id, vendor_name, date, time, total_amount, status) VALUES (?, ?, ?, ?, ?, ?)", purchase_data)

    conn.commit()
    conn.close()
    print("Database initialized with sample data!")

if __name__ == "__main__":
    init_db()
