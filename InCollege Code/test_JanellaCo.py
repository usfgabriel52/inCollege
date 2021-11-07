import sqlite3
import pytest
import io
from datetime import datetime

import menus
import messages
import verify_acc
import jobs

# test notifications when a new user has joined
def test_newUserNotif(monkeypatch):
    # add a new user
    verify_acc.data_entry("jane", "p@ssw0rD", "Jane", "Doe", 1, 1, 1, "English", "Standard")

    # log in as a different user
    input = "1\njohn\np@ssw0rD\n0\n0"
    monkeypatch.setattr('sys.stdin', io.StringIO(input))

    assert menus.homeMenu() == None

    # delete newly added row
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()
    c.execute("DELETE FROM Accounts WHERE username = 'jane'")
    conn.commit()
    c.close()


def test_jobsNotifs(monkeypatch):
    # should show the number of jobs applied as 2 since the database contains two applications for princess123
    input = "1\nprincess123\nPrincess1@\n1\n0\n0\n0"
    monkeypatch.setattr('sys.stdin', io.StringIO(input))

    assert menus.homeMenu() == None

    # should show a notification about the user not applying for a job recently
    input = "1\nCoolDude123\nCoolDude1@\n1\n0\n0\n0"
    monkeypatch.setattr('sys.stdin', io.StringIO(input))

    assert menus.homeMenu() == None

def test_newJobNotif(monkeypatch):
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    c.execute("UPDATE Accounts SET lastLogin = '2021-11-05 18:14:21' WHERE username = 'CoolDude123'")
    conn.commit()

    # insert a new job into the database
    current_date = datetime.now()
    formatted_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
    c.execute("INSERT INTO Jobs(title, description, employer, location, salary, posterfirst, posterlast, datePosted) "
              "VALUES('Mobile App Developer','need an experienced developer for our mobile app', 'InCollege', 'Tampa, FL', '$60000', 'Anna', 'Collins', ?); ", [formatted_date])
    conn.commit()

    input = "1\nCoolDude123\nCoolDude1@\n1\n0\n0\n0"
    monkeypatch.setattr('sys.stdin', io.StringIO(input))

    assert menus.homeMenu() == None

    c.execute("DELETE FROM Jobs WHERE title = 'Mobile App Developer' AND description = 'need an experienced developer for our mobile app' AND posterfirst = 'Anna' AND posterlast = 'Collins'")
    conn.commit()
    c.close()
