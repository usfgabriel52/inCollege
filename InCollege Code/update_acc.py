import sqlite3
from getpass import getpass

conn = sqlite3.connect('Accounts.db')
c = conn.cursor()

#/////////////////////////////////////////////////////////////////////////     UPDATE EMAIL OPTION     ////////////////////////////////////////////////////////////////////////////

def update_email_option(username, password):
    
    for row in c.execute("""SELECT * FROM Accounts"""):
        if username == row[0]:
            # 0 means False and 1 means True
            if row[4] == 0:
                query = """UPDATE Accounts SET email = 1 WHERE username = ? AND password = ?;"""
            elif row[4] == 1:
                query = """UPDATE Accounts SET email = 0 WHERE username = ? AND password = ?;"""
            
    data = (username, password)        
    c.execute(query, data)
    conn.commit()
    return

#/////////////////////////////////////////////////////////////////////////     UPDATE SMS OPTION     //////////////////////////////////////////////////////////////////////////////

def update_sms_option(username, password):
   
    for row in c.execute("""SELECT * FROM Accounts"""):
        if username == row[0]:
             # 0 means False and 1 means True
            if row[5] == 0:
                query = """UPDATE Accounts SET sms = 1 WHERE username = ? AND password = ?;"""
            elif row[5] == 1:
                query = """UPDATE Accounts SET sms = 0 WHERE username = ? AND password = ?;"""
            
    data = (username, password)        
    c.execute(query, data)
    conn.commit()
    return

#/////////////////////////////////////////////////////////////////////////     UPDATE ADS OPTION     //////////////////////////////////////////////////////////////////////////////

def update_ad_option(username, password):
    
    for row in c.execute("""SELECT * FROM Accounts"""):
        if username == row[0]:
             # 0 means False and 1 means True
            if row[6] == 0:
                query = """UPDATE Accounts SET ads = 1 WHERE username = ? AND password = ?;"""
            elif row[6] == 1:
                query = """UPDATE Accounts SET ads = 0 WHERE username = ? AND password = ?;"""
            
    data = (username, password)        
    c.execute(query, data)
    conn.commit()
    return

#/////////////////////////////////////////////////////////////////////////     UPDATE LANGUAGE OPTION     /////////////////////////////////////////////////////////////////////////

def update_lang_option(username, password):
    for row in c.execute("""SELECT * FROM Accounts"""):
        if username == row[0]:
            if row[7] == "English":
                query = """UPDATE Accounts SET language = "Spanish" WHERE username = ? AND password = ?;"""
            elif row[7] == "Spanish":
                query = """UPDATE Accounts SET language = "English" WHERE username = ? AND password = ?;"""
            
    data = (username, password)        
    c.execute(query, data)
    conn.commit()
    return

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////