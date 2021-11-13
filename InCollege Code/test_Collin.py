import pytest
import friends
import sqlite3
import jobs
import update_acc
import verify_acc
import messages
import training 

conn = sqlite3.connect('InCollege.db')
c = conn.cursor()


#function to test for check format of datetime 


# def test_update_last_login():
#    conn = sqlite3.connect('InCollege.db')
#    c = conn.cursor()

#    assert update_acc.getAccountsLogin == c.execute("SELECT formatted_date FROM Accounts WHERE username = ? ").fetchall() 



#function to test for last applied check

#def test_update_last_applied():
    
#     conn = sqlite3.connect('InCollege.db')
#     c = conn.cursor()

#    assert update_acc.getAccountsApplied c.execute("SELECT * FROM Accounts WHERE username = ? AND lastApplied = '?'").fetchall()
#    assert jobs.getAllJobTitlesAppliedFor == c.execute("SELECT j.id, j.title FROM Jobs j INNER JOIN app_status a ON j.id = a.jobID WHERE status == 'applied' AND a.username = ?").fetchall()

#function to test for created account 

#def test_CreateAccount():
#    conn = sqlite3.connect('InCollege.db')
#    c = conn.cursor()   
    
#    for row in c.execute("""SELECT * FROM Accounts"""):
#    assert(search.find_user(row[2],row[3])) == True
#    assert search.find_user("fake","person") == False


#function to test for message 

#def test_messages():
#    assert messages.store_message("test_user1","test_user2","test_message") == 0
#    assert messages.delete_message("test_user1","test_user2","test_message") == 0



#function to test for notification of message
#def test_inboxNotification(monkeypatch):
#    assert messages.inboxNotification("tom") == True  

#    input = "1\ncoco123\nCoco1@\n9\n2\ntom\nwaiting for you\n0\n0\n1\ntom\p@ssw0rD\n0\n0\n"
#    monkeypatch.setattr('sys.stdin', io.StringIO(input))

#    assert menus.homeMenu() == None


#---------------------------------------------------------------------------------#


def test_completeTraining():
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()
    assert training.completeTraining == c.execute("SELECT * FROM Training WHERE username = ?").fetchall()
    
    
    
def CompleteTraining(username,training):
     conn = sqlite3.connect('InCollege.db')
     c = conn.cursor()
    
    
    
 def test_InCollegeLearningMenu():
     sys.stdin = io.StringIO('4\n1\n2\n3\n4\n5\n0\n0\n')
     assert menus.InCollegeLearningMenu() == 0
    
    
    

def test_printAlreadyTakenTraining():
    assert messages.printAlreadytaken() == 0
    

def test_printCompletedTraining():
    assert messages.printCompletedTraining() == 0

def printCourseCancelled():
     assert messages.printCourseCancelled() == 0

