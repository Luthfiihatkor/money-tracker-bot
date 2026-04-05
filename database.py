import psycopg2
from config import DATABASE_URL

def connect():
    return psycopg2.connect(DATABASE_URL)
