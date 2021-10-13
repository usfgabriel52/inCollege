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

def requestFriend(userName,requestee):
    if findSpecificFriend(userName, requestee).fetchall() != []:
        return 0
    if findSpecificRequest(requestee,userName).fetchall() != []:
        return 1
    if findSpecificRequest(userName,requestee).fetchall() != []:
        #acceptRequest
        return 2
    query = """INSERT INTO requests(userName,requestee) VALUES(?,?)"""
    data = (userName,requestee)
    c.execute(query,data)
    conn.commit()
    return 3

def findFriends(userName):
    query = """SELECT * FROM friends WHERE userName = ?"""
    data = (userName)
    f = []
    friendArr = c.execute(query, [data])
    for friend in friendArr:
        f.append(friend[1])
    query = """SELECT * FROM friends WHERE friend = ?"""
    data = (userName)
    friendArr = c.execute(query, [data])
    for friend in friendArr:
        f.append(friend[0])
    return f


def findSpecificFriend(userName,friend):
    query = """SELECT * FROM friends WHERE userName = ? AND friend = ?"""
    data = (userName,friend)
    checkFriend  = c.execute(query, data)
    if checkFriend.fetchall() == []:
        query = """SELECT * FROM friends WHERE userName = ? AND friend = ?"""
        data = (friend,userName)
        return c.execute(query, data)
    else:
        return checkFriend

def findRequests(userName):
    query = """SELECT * FROM requests WHERE requestee = ?"""
    data = (userName)
    return c.execute(query, [data])

def findSpecificRequest(userName,requester):
    query = """SELECT * FROM requests WHERE userName = ? AND requestee = ?"""
    data = (requester,userName)
    return c.execute(query, data)
    
def deleteRequest(userName,requester):
    query = """DELETE FROM requests WHERE userName  = ? AND requestee = ?"""
    data = (requester,userName)
    c.execute(query,data)
    conn.commit()

def addFriend(userName,friend):
    query = """INSERT INTO friends(userName, friend) VALUES(?,?)"""
    data = (userName,friend)
    c.execute(query,data)
    conn.commit()
def acceptRequest(userName,requester):
    if findSpecificRequest(userName,requester).fetchall() == []:
        return 0
    deleteRequest(userName,requester)
    addFriend(userName, requester)


def rejectReuest(userName,requester):
    if findSpecificRequest(userName,requester).fetchall() == []:
        return 0
    deleteRequest(userName,requester)

def removeFriend(userName,friend):
    query = """DELETE FROM friends WHERE userName  = ? AND friend = ?"""
    data = (friend,userName)
    c.execute(query,data)
    conn.commit()
    query = """DELETE FROM friends WHERE userName  = ? AND friend = ?"""
    data = (userName,friend)
    c.execute(query,data)
    conn.commit()
    

