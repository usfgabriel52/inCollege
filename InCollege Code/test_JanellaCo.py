import sqlite3
import pytest
import io

import menus
import messages
import verify_acc

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
    