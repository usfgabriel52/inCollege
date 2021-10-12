import sqlite3
from getpass import getpass

conn = sqlite3.connect('InCollege.db')
c = conn.cursor()

def create_friends_tables():
    query = """CREATE TABLE IF NOT EXISTS friends(userName TEXT,friend TEXT)"""
    c.execute(query)
    conn.commit()
    query = """CREATE TABLE IF NOT EXISTS requests(userName TEXT, requestee TEXT)"""
    c.execute(query)
    conn.commit()
