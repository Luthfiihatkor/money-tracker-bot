from database import connect


def init_db():

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS transactions(
        id SERIAL PRIMARY KEY,
        type TEXT,
        amount INT,
        category TEXT,
        note TEXT,
        date TIMESTAMP
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS goals(
        id SERIAL PRIMARY KEY,
        name TEXT,
        target INT,
        saved INT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS bills(
        id SERIAL PRIMARY KEY,
        name TEXT,
        amount INT,
        due_date DATE
    )
    """)

    conn.commit()
    conn.close()
