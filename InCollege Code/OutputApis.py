import sqlite3


###MyCollege_jobs.txt "myCollegeJob"


### WriteOut overwrite the entire file with the information in the SQL Database
### Use if job is removed or on startup if the data in the file doesnt match the SQL database
def MyCollegeJobs_WriteOut():
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()
    query = """SELECT * FROM Jobs id WHERE id NOT IN (SELECT jobID FROM app_status WHERE status == 'deleted')"""
    jobsarr = c.execute(query).fetchall()
    conn.close()
    myCollegeJob =open("output files\\MyCollege_job.txt","w+")
    for job in jobsarr:
        myCollegeJob.write(job[1]+"\n")
        myCollegeJob.write(job[2]+"\n")
        myCollegeJob.write(job[3]+"\n")
        myCollegeJob.write(job[4]+"\n")
        myCollegeJob.write(job[5]+"\n")
        myCollegeJob.write("=====\n")
    myCollegeJob.close()
    return 0

def MyCollegeJobs_append(job):
    myCollegeJob=open("output files\\MyCollege_job.txt","a")
    myCollegeJob.write(job[0]+"\n")
    myCollegeJob.write(job[1]+"\n")
    myCollegeJob.write(job[2]+"\n")
    myCollegeJob.write(job[3]+"\n")
    myCollegeJob.write(job[4]+"\n")
    myCollegeJob.write("=====\n")
    myCollegeJob.close()
    return 0


####MyCollege_Profiles
def MyCollegeProfiles_WriteOut():
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()
    query = """SELECT * FROM PersonalProfile"""
    profiles = c.execute(query).fetchall()
    myCollegeProfile =open( "output files\\MyCollege_profiles.txt","w+")
    for profile in profiles:
        myCollegeProfile.write(profile[0]+"\n")
        myCollegeProfile.write(profile[1]+"\n")
        myCollegeProfile.write(profile[2]+"\n")
        myCollegeProfile.write(profile[3]+"\n")
        myCollegeProfile.write(profile[4]+"\n")
        query = """SELECT * FROM education WHERE userName = ?"""
        edcucation = c.execute(query,[profile[0]]).fetchall()
        for ed in edcucation:
            myCollegeProfile.write(ed[1]+"\n")
            myCollegeProfile.write(ed[2]+"\n")
            myCollegeProfile.write(ed[3]+"\n")
        query = "SELECT * FROM expierience WHERE userName = ?"
        expierience = c.execute(query,[profile[0]]).fetchall()
        for exp in expierience:
            for index in range(1,7):
                myCollegeProfile.write(exp[index]+"\n")

        myCollegeProfile.write("=====\n")
    conn.close()
    myCollegeProfile.close()
    return 0


###MyCollegeUsers

def MyCollegeUsers_WriteOut():
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()
    query = """SELECT * FROM Accounts"""
    accounts = c.execute(query).fetchall()
    conn.close()
    myCollegeUsers =open( "output files\\MyCollege_users.txt","w+")
    for users in accounts:
        myCollegeUsers.write(users[0]+" "+users[8]+"\n")
    myCollegeUsers.close()
    return 0

def MyCollegeUsers_Append(user,status):
    myCollegeUsers =open( "output files\\MyCollege_users.txt","a")
    myCollegeUsers.write(user+" "+status+"\n")
    myCollegeUsers.close()
    return 0

def MyCollegeTraining_WriteOut():
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()
    users = c.execute("""SELECT username FROM Accounts""").fetchall()
    training = open("output files\\MyCollege_training.txt","w+")
    for user in users:
        training.write(user[0]+"\n")
        query = """SELECT title FROM Training T INNER JOIN Courses C ON T.course_id = C.id WHERE username = ? AND status = 'Complete'"""
        result = c.execute(query, [user[0]]).fetchall()
        for t in result:
            training.write(t[0] + "\n")
        training.write("=====\n")
    training.close()
    conn.close()
    return 0

def MyCollegeAppliedJobs_WriteOut():
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()
    query = """SELECT * FROM Jobs"""
    jobs = c.execute(query).fetchall()
    appliedJobs = open("output files\\MyCollege_appliedJobs.txt","w+")
    for job in jobs:
        appliedJobs.write(job[1]+"\n")
        query = """SELECT * FROM applications WHERE jobID = ?"""
        applicants =  c.execute(query,[job[0]]).fetchall()
        for applicant in applicants:
            appliedJobs.write(applicant[0] + " "+ applicant[4] +"\n")
        appliedJobs.write("=====\n")
    appliedJobs.close()
    conn.close()
    return 0



### MyCollegeSavedJobs

def MyCollegeSavedJobs_WriteOut():
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()
    query = """SELECT * FROM Accounts"""
    users = c.execute(query).fetchall()
    savedJobs = open("output files\\MyCollege_savedJobs.txt","w+")
    for user in users:
        query = """SELECT * FROM SavedJobs WHERE username = ?"""

        jobs = c.execute(query,[user[0]]).fetchall()
        if jobs != []:
            savedJobs.write(user[0]+"\n")
            for job in jobs:
                query = """SELECT * FROM Jobs WHERE id = ?"""
                jobName = c.execute(query,[job[1]]).fetchall()
                savedJobs.write(jobName[0][1] + "\n")
            savedJobs.write("=====\n")
    savedJobs.close()
    conn.close()
    return 0


    ###Startup Runall

def RunallOutputAPIS():
    MyCollegeSavedJobs_WriteOut()
    MyCollegeTraining_WriteOut()
    MyCollegeJobs_WriteOut()
    MyCollegeProfiles_WriteOut()
    MyCollegeUsers_WriteOut()
    MyCollegeAppliedJobs_WriteOut()
