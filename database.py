import sqlite3

conn = sqlite3.connect("money.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER,
type TEXT,
amount INTEGER,
category TEXT,
note TEXT,
date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()


def add_transaction(user_id, tipe, amount, category, note):
    cursor.execute(
        "INSERT INTO transactions (user_id,type,amount,category,note) VALUES (?,?,?,?,?)",
        (user_id, tipe, amount, category, note),
    )
    conn.commit()


def get_transactions(user_id):
    cursor.execute(
        "SELECT type,amount,category,note,date FROM transactions WHERE user_id=?",
        (user_id,),
    )
    return cursor.fetchall()


def get_balance(user_id):

    cursor.execute(
        "SELECT SUM(amount) FROM transactions WHERE user_id=? AND type='income'",
        (user_id,),
    )

    income = cursor.fetchone()[0] or 0

    cursor.execute(
        "SELECT SUM(amount) FROM transactions WHERE user_id=? AND type='expense'",
        (user_id,),
    )

    expense = cursor.fetchone()[0] or 0

    return income - expense
