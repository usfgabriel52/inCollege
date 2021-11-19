import sqlite3
from getpass import getpass
from datetime import datetime

#/////////////////////////////////////////////////////////////////////////     UPDATE EMAIL OPTION     ////////////////////////////////////////////////////////////////////////////

def update_email_option(username, password):
    
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    for row in c.execute("""SELECT * FROM Accounts"""):
        if username == row[0]:
            # 0 means False and 1 means True
            if row[4] == 0:
                query = """UPDATE Accounts SET email = 1 WHERE username = ? AND password = ?;"""
                print("\n Email option is now ON.\n")
            elif row[4] == 1:
                query = """UPDATE Accounts SET email = 0 WHERE username = ? AND password = ?;"""
                print("\n Email option is now OFF.\n")
            
    data = (username, password)        
    c.execute(query, data)
    conn.commit()
    conn.close()
    return

#/////////////////////////////////////////////////////////////////////////     UPDATE SMS OPTION     //////////////////////////////////////////////////////////////////////////////

def update_sms_option(username, password):

    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    for row in c.execute("""SELECT * FROM Accounts"""):
        if username == row[0]:
             # 0 means False and 1 means True
            if row[5] == 0:
                query = """UPDATE Accounts SET sms = 1 WHERE username = ? AND password = ?;"""
                print("\n SMS option is now ON.\n")
            elif row[5] == 1:
                query = """UPDATE Accounts SET sms = 0 WHERE username = ? AND password = ?;"""
                print("\n SMS option is now OFF.\n")
            
    data = (username, password)        
    c.execute(query, data)
    conn.commit()
    conn.close()
    return

#/////////////////////////////////////////////////////////////////////////     UPDATE ADS OPTION     //////////////////////////////////////////////////////////////////////////////

def update_ad_option(username, password):

    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    for row in c.execute("""SELECT * FROM Accounts"""):
        if username == row[0]:
             # 0 means False and 1 means True
            if row[6] == 0:
                query = """UPDATE Accounts SET ads = 1 WHERE username = ? AND password = ?;"""
                print("\n Ads option is now ON.\n")
            elif row[6] == 1:
                query = """UPDATE Accounts SET ads = 0 WHERE username = ? AND password = ?;"""
                print("\n Ads option is now OFF.\n")
            
    data = (username, password)        
    c.execute(query, data)
    conn.commit()
    conn.close()
    return

#/////////////////////////////////////////////////////////////////////////     UPDATE LANGUAGE OPTION     /////////////////////////////////////////////////////////////////////////

def update_lang_option(username, password, lang):
    
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    if(lang == "English"):
        query = """UPDATE Accounts SET language = "English" WHERE username = ? AND password = ?;"""
        print("\n Language is now English.\n")
    elif(lang == "Spanish"):
        query = """UPDATE Accounts SET language = "Spanish" WHERE username = ? AND password = ?;"""
        print("\n Language is now Spanish.\n")

    data = (username, password)        
    c.execute(query, data)
    conn.commit()
    conn.close()
    return

#/////////////////////////////////////////////////////////////////////////     UPDATE LAST LOGIN DATE / TIME      /////////////////////////////////////////////////////////////////////////

def update_last_login(username):
    
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    #gets the current date and time
    current_date = datetime.now()
    # formats the date and time into a string
    formatted_date = current_date.strftime('%Y-%m-%d %H:%M:%S')

    query = """UPDATE Accounts SET lastLogin = ? WHERE username = ?;"""
    data = (formatted_date, username)

    c.execute(query, data)
    conn.commit()
    conn.close()
    return 0

#/////////////////////////////////////////////////////////////////////////     UPDATE LAST APPLIED FOR A JOB DATE / TIME      /////////////////////////////////////////////////////////////////////////

def update_last_applied(username):
    
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    #gets the current date and time
    current_date = datetime.now()
    # formats the date and time into a string
    formatted_date = current_date.strftime('%Y-%m-%d %H:%M:%S')

    query = """UPDATE Accounts SET lastApplied = ? WHERE username = ?;"""
    data = (formatted_date, username)

    c.execute(query, data)
    conn.commit()
    conn.close()
    return 0
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

