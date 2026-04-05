import sqlite3

conn = sqlite3.connect("money.db",check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS transaksi(
id INTEGER PRIMARY KEY AUTOINCREMENT,
user INTEGER,
tipe TEXT,
jumlah INTEGER,
kategori TEXT,
wallet TEXT,
note TEXT,
tanggal TEXT
)
""")

conn.commit()
