import sqlite3
import pytest
import io

import menus
import messages

# test for notification
def test_inboxNotification(monkeypatch):
    assert messages.inboxNotification("john") == True  # must return true because the database has messages for john
    assert messages.inboxNotification("kingofpop1") == False  # must return false because there's no messages for kingofpop1

    input = "1\nprincess123\nPrincess1@\n9\n2\njohn\nHow are you?\n0\n0\n1\njohn\p@ssw0rD\n0\n0\n"
    monkeypatch.setattr('sys.stdin', io.StringIO(input))

    assert menus.homeMenu() == None

def test_replyInbox(monkeypatch):
    assert messages.inbox("kingofpop1", "Standard") == -1  # should return -1 because there's no messages

    # test replying
    input = "1\n1\nprincess123\nHi there\n"
    monkeypatch.setattr('sys.stdin', io.StringIO(input))
    assert messages.inbox("john", "Standard") == 1

 # test deletion
def test_deletionInbox(monkeypatch):
    input = "1\njohn\np@ssw0rD\n9\n1\n1\n2\n0\n0\n"
    monkeypatch.setattr('sys.stdin', io.StringIO(input))
    assert menus.homeMenu() == None