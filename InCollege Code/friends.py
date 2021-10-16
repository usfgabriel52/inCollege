import sqlite3
from getpass import getpass

conn = sqlite3.connect('InCollege.db')
c = conn.cursor()

#Requests a friend
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



#finds all friends of user, returns array of usernames
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

#checks if a specific friend is in the table
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

#finds all friend requests for specific user
def findRequests(userName):
    query = """SELECT * FROM requests WHERE requestee = ?"""
    data = (userName)
    return c.execute(query, [data])

#Frinds a specific friend request 
def findSpecificRequest(userName,requester):
    query = """SELECT * FROM requests WHERE userName = ? AND requestee = ?"""
    data = (requester,userName)
    return c.execute(query, data)

#PRIVATE METHOD: Deletes a request From requests table
def deleteRequest(userName,requester):
    query = """DELETE FROM requests WHERE userName  = ? AND requestee = ?"""
    data = (requester,userName)
    c.execute(query,data)
    conn.commit()

#PRIVATE METHOD, Adds friend to friends table 
def addFriend(userName,friend):
    query = """INSERT INTO friends(userName, friend) VALUES(?,?)"""
    data = (userName,friend)
    c.execute(query,data)
    conn.commit()

#Accepts friend request (removes request and adds friends to friends table)
def acceptRequest(userName,requester):
    if findSpecificRequest(userName,requester).fetchall() == []:
        return 0
    deleteRequest(userName,requester)
    addFriend(userName, requester)

#rejects a friend request
def rejectReuest(userName,requester):
    if findSpecificRequest(userName,requester).fetchall() == []:
        return 0
    deleteRequest(userName,requester)

#removes a friend
def removeFriend(userName,friend):
    query = """DELETE FROM friends WHERE userName  = ? AND friend = ?"""
    data = (friend,userName)
    c.execute(query,data)
    conn.commit()
    query = """DELETE FROM friends WHERE userName  = ? AND friend = ?"""
    data = (userName,friend)
    c.execute(query,data)
    conn.commit()
    

