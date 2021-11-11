import sqlite3


def CompleteTraining(username,training):
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()
    query = """UPDATE Training SET """+training+""" = ? WHERE username = ?"""
    c.execute (query,["Complete",username])
    conn.commit()
    conn.close

    return 0

def checkTraining(username):
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()
    query = """SELECT * FROM Training WHERE username = ?"""
    userTraining = c.execute (query,[username]).fetchall()[0]
    conn.close()
    return userTraining
    