import pytest
import friends
import sqlite3
import jobs
import update_acc
import verify_acc
import messages
import training 




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


#function to test for training query complete

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






