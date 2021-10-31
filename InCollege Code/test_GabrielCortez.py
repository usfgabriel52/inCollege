import sys
import io
from typing import NoReturn
import pytest
from pytest_mock import mocker
import sqlite3
#sys.path.insert(0,'InCollege Code')
import menus
import messages
import verify_acc
import search
import jobs
conn = sqlite3.connect('InCollege.db')
c = conn.cursor()
#tests for stories 4,5,6 on epic 1

# def test_Main_Menu():
#     sys.stdin = io.StringIO('0')
#     assert menus.mainMenu() == 0
#Test Depricated
# def test_findJob():
#     sys.stdin = io.StringIO('1 \n 0\n')
#     assert menus.mainMenu() == 0
#Test Depricated
# def test_findSomeone():
#     sys.stdin = io.StringIO('1 \n 0\n')
#     assert menus.mainMenu() == 0

# def test_skillsMenu():
#     sys.stdin = io.StringIO('4\n1\n2\n3\n4\n5\n0\n0\n')
#     assert menus.mainMenu() == 0   

# #test for new stoies  1, , on Epic 2

# def test_studentSuccessStory():
#     assert messages.printStudentSuccess() == 0

# def test_viewVideo():
#     sys.stdin = io.StringIO('4\n0')
#     assert menus.homeMenu() == None

# def test_CreateAccount():
#     conn = sqlite3.connect('InCollege.db')
#     c = conn.cursor()   
#     for row in c.execute("""SELECT * FROM Accounts"""):
#         assert(search.find_user(row[2],row[3])) == True
#     assert search.find_user("fake","person") == False

# def test_markOrUnMarkJobs():
#     jobs.removeFromSavedJobs("tester123",1)
#     assert jobs.saveJob("tester123",1) == True
#     list = (jobs.getAllSavedJobs("tester123"))
#     i =0
#     list_contains_1 = False
#     while i < len(list):
#         if 1 in list[i]:
#             list_contains_1 = True
#         i += 1
#     assert list_contains_1
#     assert jobs.removeFromSavedJobs("tester123",1) == True


# def test_jobsTablesExist():
#     conn = sqlite3.connect('InCollege.db')
#     c = conn.cursor()
#     assert c.execute("SELECT * FROM Jobs").fetchall() != None
#     assert c.execute("SELECT * FROM app_status").fetchall() != None
#     assert c.execute("SELECT * FROM SavedJobs").fetchall() != None
    

# def test_job_view():
#     conn = sqlite3.connect('InCollege.db')
#     c = conn.cursor()
#     assert jobs.getAllJobTitles() == c.execute("SELECT id, title FROM Jobs").fetchall()
#     assert jobs.getJobDetails(1) == c.execute("SELECT * FROM Jobs WHERE id = ?", [1]).fetchone()

# def test_canDeleteJob():
#     sys.stdin = io.StringIO("a \n b\n c\n d\n e\n1\n")
#     jobs.postJob("test1","test2")

#     assert menus.deleteJobMenu("test1","test2")

def test_addPlusAccount():
    verify_acc.create_tables()
    verify_acc.data_entry("test_user", "test_password", "test_first", "test_last", 1, 1, 1, "English","Plus")
    verify_acc.data_entry("test_user", "test_password", "test_first", "test_last", 1, 1, 1, "English","Standard")
    assert verify_acc.getAccountInfo("test_user")[0][8] == "Plus"
    assert verify_acc.getAccountInfo("test_user")[1][8] == "Standard"
    verify_acc.deleteAccount("test_user")
def test_messages():
    assert messages.store_message("test_user1","test_user2","test_message") == 0
    assert messages.delete_message("test_user1","test_user2","test_message") == 0

def test_displayAllUsers():
    assert messages.displayAllUsers() == 0