import sqlite3
from getpass import getpass
from OutputApis import * 
conn = sqlite3.connect('InCollege.db')
c = conn.cursor()

#Returns True if User is in Personal Profile Database
def hasProfile(userName):

    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    query = """SELECT * FROM PersonalProfile WHERE userName = ?"""
    data = (userName)
    c.execute(query, [data])
    x = c.fetchall()
    if x != []:
        conn.close()
        return True
    conn.close()
    return False

def getProfile(userName):

    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    query = """SELECT * FROM PersonalProfile WHERE userName = ?"""
    data = (userName)
    c.execute(query,[data])
    profile = c.fetchall()
    conn.close()
    return profile

def hasJob(userName,jobId):

    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    query = """SELECT * FROM expierience WHERE userName = ? AND jobId = ?"""
    data = (userName,jobId)
    c.execute(query,data)
    x = c.fetchall()
    if x != []:
        conn.close()
        return True
    conn.close()
    return False

def getJob(userName, jobId):

    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    query = """SELECT * FROM expierience WHERE userName = ? AND jobId = ?"""
    data = (userName,jobId)
    c.execute(query,data)
    job = c.fetchall()
    conn.close()
    return job

def hasSchool(userName):

    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    query = """SELECT * FROM education WHERE userName = ?"""
    data = (userName)
    c.execute(query,[data])
    x = c.fetchall()
    if x != []:
        conn.close()
        return True
    conn.close()
    return False

def getSchool(userName):

    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    query = """SELECT * FROM education WHERE userName = ?"""
    data = (userName)
    c.execute(query,[data])
    school = c.fetchall()
    conn.close()
    return school

#Allows a field in the personal profile table to be updated given username and section
def update_profile(userName,section, newValue):

    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

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
    conn.close()
    MyCollegeProfiles_WriteOut()
    return 0


#Allows a field in the job table to be changed given a username and jobId and section
def update_job(userName,jobId,section,newValue):
    
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

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
        conn.close()
        return -1

    data = (newValue,userName,jobId)
    c.execute(query,data)
    conn.commit()
    conn.close()
    MyCollegeProfiles_WriteOut()
    return 0


#allows school table to be updated given username and section 
def update_school(userName,section,newValue):

    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    if(section == "schoolName"):
            query = """UPDATE education SET schoolName = ? WHERE userName = ?"""
    elif(section == "degree"):
        query = """UPDATE education SET degree = ? WHERE userName = ?"""
    elif(section == "yearsAttended"):
        query = """UPDATE education SET yearsAttended = ? WHERE userName = ?"""
    else:
        conn.close()
        return -1

    data = (newValue,userName)
    c.execute(query,data)
    conn.commit()
    conn.close()
    MyCollegeProfiles_WriteOut()
    return 0

#Formats strings to have the first letter in uppercase of each word and the rest lowercase
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

#inserts username into job table, jobId should be labeled 1-3
def create_job(userName,jobId):
    
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    query = """INSERT INTO expierience(userName , jobId , title , employer , dateStart , dateEnd , location , description ) VALUES(? , ? , ? , ? , ? , ? , ? , ? )"""
    data = (userName,jobId,None,None,None,None,None,None) 
    c.execute(query, data)
    conn.commit()
    conn.close()
    MyCollegeProfiles_WriteOut()


#Adds user to school table    
def create_school(userName):

    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    query = """INSERT INTO education(userName, schoolName, Degree , yearsAttended) VALUES(?,?,?,?)"""
    data = (userName,None,None,None) 
    c.execute(query,data)
    conn.commit()
    conn.close()
    MyCollegeProfiles_WriteOut()
    
#Adds user to Personal Profile Table
def create_profile(userName):

    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    query = """INSERT INTO PersonalProfile(userName,title,major,universityName,about) VALUES(?,?,?,?,?)"""
    data = (userName,None,None,None,None) 
    c.execute(query,data)
    conn.commit()
    MyCollegeProfiles_WriteOut()
    conn.close()


def checkTitle(userName):

    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    for row in c.execute("""SELECT * FROM personalProfile"""):
        if userName == row[0] and row[1] != None:
            conn.close()
            return True
    conn.close()
    return False

def checkMajor(userName):

    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    for row in c.execute("""SELECT * FROM personalProfile"""):
        if userName == row[0] and row[2] != None:
            conn.close()
            return True
    conn.close()
    return False

def checkUniversityName(userName):
    
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    for row in c.execute("""SELECT * FROM personalProfile"""):
        if userName == row[0] and row[3] != None:
            conn.close()
            return True
    conn.close()
    return False

def checkAbout(userName):

    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    for row in c.execute("""SELECT * FROM personalProfile"""):
        if userName == row[0] and row[4] != None:
            conn.close()
            return True
    conn.close()
    return False

def checkJob(userName):
    
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    numjob = 0
    for row in c.execute("""SELECT * FROM experience"""):
        if userName == row[0] and row[1] != None:
            numjob +=1
    conn.close()
    return numjob

def checkSchool(userName):
    
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    for row in c.execute("""SELECT * FROM education"""):
        if userName == row[0]and row[1] != None:
            conn.close()
            return True
    conn.close()
    return False

# get all the personal profile info related to the given username
def getProfileInfo(userName):
    query ="""SELECT * FROM personalProfile WHERE userName=?"""
    data = [userName]

    return c.execute(query, data)

# get all the experience info related to the given username
def getExperienceInfo(userName):
    query = """SELECT * FROM expierience WHERE userName=?"""
    data = [userName]

    return c.execute(query, data)

# get all the education infor related to the given username
def getEducationInfo(userName):
    # get all the information related to the given username
    query = """SELECT * FROM education WHERE userName=?"""
    data = [userName]

    return c.execute(query, data)