import sqlite3
from getpass import getpass

conn = sqlite3.connect('PersonalProfile.db')
c = conn.cursor()

def create_job_table():
    #SQL
    query = """CREATE TABLE IF NOT EXISTS PersonalProfile(userName TEXT,title TEXT, major TEXT, universityName TEXT, about TEXT)"""
    c.execute(query)
    conn.commit()
    query = """CREATE TABLE IF NOT EXISTS expierience(userName TEXT, jobId INT, title TEXT, employer TEXT, dateStart Text, dateEnd Text, location TEXT, description TEXT)"""
    c.execute(query)
    conn.commit()
    query = """CREATE TABLE IF NOT EXISTS education(userName TEXT, schoolName TEXT, degree TEXT, yearsAttended INT)"""
    c.execute(query)
    conn.commit() 
def hasProfile(userName):
    for row in c.execute("""SELECT * FROM PersonalProfile"""):
        if(userName == row[0]):
            return True
    return False

def update_profile(userName,section, newValue):
    if(section == "title"):
        query = """UPDATE PersonalProfile SET title = ? WHERE userName = ?"""
    elif(section == "major"):
        query = """UPDATE PersonalProfile SET major = ? WHERE userName = ?"""
    elif(section == "universityName"):
        query = """UPDATE PersonalProfile SET universityName = ? WHERE userName = ?"""
    elif(section == "about"):
        query = """UPDATE PersonalProfile SET about = ? WHERE userName = ?"""
    else:
        return -1
    
    data = (newValue,userName)
    c.execute(query,data)
    conn.commit()
    return 0

def update_job(userName,jobId,section,newValue):
    if(section == "title"):
            query = """UPDATE expierience SET title = ? WHERE userName = ? AND jobId = ?"""
    elif(section == "employer"):
        query = """UPDATE expierience SET employer = ? WHERE userName = ? AND jobId = ?"""
    elif(section == "dateStart"):
        query = """UPDATE expierience SET dateStart = ? WHERE userName = ? AND jobId = ?"""
    elif(section == "dateEnd"):
        query = """UPDATE expierience SET dateEnd = ? WHERE userName = ? AND jobId = ?"""
    elif(section == "location"):
        query = """UPDATE expierience SET location = ? WHERE userName = ? AND jobId = ?"""
    elif(section == "description"):
        query = """UPDATE expierience SET description = ? WHERE userName = ? AND jobId = ?"""
    else:
        return -1

    data = (newValue,userName,jobId)
    c.execute(query,data)
    conn.commit()
    return 0

def update_school(userName,section,newValue):
    if(section == "schoolName"):
            query = """UPDATE education SET schoolName = ? WHERE userName = ?"""
    elif(section == "degree"):
        query = """UPDATE education SET degree = ? WHERE userName = ?"""
    elif(section == "yearsAttended"):
        query = """UPDATE education SET yearsAttended = ? WHERE userName = ?"""
    else:
        return -1

    data = (newValue,userName)
    c.execute(query,data)
    conn.commit()
    return 0

def formatCaps(str):
    str = str.split(' ')
    result = ''
    for i in str:
        i = i.lower()
        tempUpper = i.upper()
        i = tempUpper[0] + i[1:] +" "
        result += i
    result = result[:-1]
    return result

def create_job(userName,jobId):
    query = """INSERT INTO expierience(userName , jobId , title , employer , dateStart , dateEnd , location , description ) VALUES(?,?,?,?,?,?,?,?)"""
    data = (userName,jobId,None,None,None,None,None,None) 
    c.execute(query,data)
    conn.commit() 

    
def create_school(userName):
    query = """INSERT INTO education(userName, schoolName, Degree , yearsAttended) VALUES(?,?,?,?)"""
    data = (userName,None,None,None) 
    c.execute(query,data)
    conn.commit()
    

def create_profile(userName):
    query = """INSERT INTO PersonalProfile(userName,title,major,universityName,about) VALUES(?,?,?,?,?)"""
    data = (userName,None,None,None,None) 
    c.execute(query,data)
    conn.commit()
    


    
    

