import sqlite3
import os

#RUN THIS FIRST

DB_FILES = {
    "user": "user_db.sqlite",
    "payments": "payments_db.sqlite",
    "debt": "debt_db.sqlite",
    "history": "history_db.sqlite",
    "mix": "mix_reference_db.sqlite"
}

def setup_databases():
    os.makedirs("databases", exist_ok=True)
    os.chdir("databases")

    # USER DB
    with sqlite3.connect(DB_FILES["user"]) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, name TEXT)")
        conn.executemany("INSERT OR IGNORE INTO users VALUES (?, ?)", [
            (1, 'Ahmed'), (2, 'Sara'), (3, 'John'), (4, 'Fatma'),
            (5, 'Laila'), (6, 'Omar'), (7, 'Noura'), (8, 'Khaled')
        ])

    # PAYMENTS DB
    with sqlite3.connect(DB_FILES["payments"]) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS payments (user_id INTEGER, on_time_payments INTEGER, total_payments INTEGER)")
        conn.executemany("INSERT OR IGNORE INTO payments VALUES (?, ?, ?)", [
            (1, 18, 20), (2, 12, 15), (3, 10, 20), (4, 19, 20),
            (5, 14, 14), (6, 16, 20), (7, 11, 15), (8, 13, 13)
        ])

    # DEBT DB
    with sqlite3.connect(DB_FILES["debt"]) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS debts (user_id INTEGER, used_credit REAL, credit_limit REAL)")
        conn.executemany("INSERT OR IGNORE INTO debts VALUES (?, ?, ?)", [
            (1, 3000, 10000), (2, 1000, 5000), (3, 8000, 10000), (4, 2000, 8000),
            (5, 1000, 4000), (6, 2500, 6000), (7, 6000, 9000), (8, 500, 3000)
        ])

    # HISTORY DB
    with sqlite3.connect(DB_FILES["history"]) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS history (user_id INTEGER, account_age INTEGER, max_age INTEGER)")
        conn.executemany("INSERT OR IGNORE INTO history VALUES (?, ?, ?)", [
            (1, 3, 10), (2, 5, 10), (3, 1, 10), (4, 8, 10),
            (5, 6, 10), (6, 2, 10), (7, 4, 10), (8, 9, 10)
        ])

    # MIX DB
    with sqlite3.connect(DB_FILES["mix"]) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS credit_mix (user_id INTEGER, credit_types_used INTEGER, total_types INTEGER)")
        conn.executemany("INSERT OR IGNORE INTO credit_mix VALUES (?, ?, ?)", [
            (1, 2, 4), (2, 1, 4), (3, 3, 5), (4, 4, 5),
            (5, 3, 4), (6, 2, 5), (7, 1, 3), (8, 4, 5)
        ])

    os.chdir("..")
    print("All Data added")  # Now inside the function

# 🔧 Call the function to set up the DBs
if __name__ == "__main__":
    setup_databases()
