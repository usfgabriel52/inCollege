import sqlite3
from getpass import getpass

conn = sqlite3.connect('Accounts.db')
c = conn.cursor()

#/////////////////////////////////////////////////////////////////////////     UPDATE EMAIL OPTION     ////////////////////////////////////////////////////////////////////////////

def update_email_option(username, password):
    
    for row in c.execute("""SELECT * FROM Accounts"""):
        if username == row[0]:
            if row[4] == 0:
                query = """UPDATE Accounts SET email = 1 WHERE username = ? AND password = ?;"""
            elif row[4] == 1:
                query = """UPDATE Accounts SET email = 0 WHERE username = ? AND password = ?;"""
            
    data = (username, password)        
    c.execute(query, data)
    conn.commit()
    return

#/////////////////////////////////////////////////////////////////////////     UPDATE SMS OPTION     //////////////////////////////////////////////////////////////////////////////

def update_sms_option():
    return

#/////////////////////////////////////////////////////////////////////////     UPDATE ADS OPTION     //////////////////////////////////////////////////////////////////////////////

def update_ad_option():
    return

#/////////////////////////////////////////////////////////////////////////     UPDATE LANGUAGE OPTION     /////////////////////////////////////////////////////////////////////////

def update_lang_option():
    return

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////