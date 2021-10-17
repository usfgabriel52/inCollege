import pytest
import friends
import sqlite3

#function ro test whether remove friend function works
def test_removeFriend():
    friends.removeFriend("nhandang", "test")
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    query = ("SELECT FROM friends WHERE userName  = ? AND friend = ?")
    data=("nhandang", "test")
    assert c.execute(query, data) == ""

#function to check user friendlist initiated empty
def test_initialFriendList():
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    query = ("SELECT FROM friends WHERE userName  = ? ")
    data=("nhandang")
    assert c.execute(query, data) == ""
