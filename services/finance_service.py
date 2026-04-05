from database import connect
from datetime import datetime


def add_transaction(t_type, amount, category, note):

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO transactions(type,amount,category,note,date)
        VALUES(%s,%s,%s,%s,%s)
        """,
        (t_type, amount, category, note, datetime.now())
    )

    conn.commit()
    conn.close()


def get_transactions():

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM transactions")

    data = cur.fetchall()

    conn.close()

    return data
