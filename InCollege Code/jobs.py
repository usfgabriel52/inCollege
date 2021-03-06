import sqlite3
from getpass import getpass
from sqlite3.dbapi2 import Error
from datetime import datetime
from update_acc import update_last_applied
from OutputApis import *

conn = sqlite3.connect('InCollege.db')
c = conn.cursor()


# /////////////////////////////////////////////////////////////////////////     ENTER DATA INTO DB     ////////////////////////////////////////////////////////////////////

# inserts login info from user into table
def job_data_entry(title, description, employer, location, salary, posterfirst, posterlast):
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    # gets the current date and time
    current_date = datetime.now()
    # formats the date and time into a string
    formatted_date = current_date.strftime('%Y-%m-%d %H:%M:%S')

    # SQL
    query = """INSERT INTO Jobs(title, description, employer, location, salary, posterfirst, posterlast, datePosted) VALUES(?, ?, ?, ?, ?, ?, ?, ?);"""

    # Stores username, password , firstname , lastname
    data = (title, description, employer, location, salary, posterfirst, posterlast, formatted_date)
    c.execute(query, data)
    conn.commit()

    MyCollegeJobs_append([title, description, employer, location, salary])
    MyCollegeAppliedJobs_WriteOut()

    conn.close()


# /////////////////////////////////////////////////////////////////////////     NUMBER OF JOBS    /////////////////////////////////////////////////////////////////////////

# number of jobs created
def job_created():
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    # SQL
    rows = -1
    try:
        query = """SELECT * FROM Jobs"""
        c.execute(query)
        conn.commit()

        rows = len(c.fetchall())
    except Error:
        rows = 0
    conn.close()
    return rows


# /////////////////////////////////////////////////////////////////////////     POST A JOB    ////////////////////////////////////////////////////////////////////////////

def postJob(posterfirst, posterlast):
    print("\nPost A Job.\n")

    ExistingJobs = 0

    if job_created() < 10:
        title = input("Enter Job Title: ")
        description = input("Enter Job Description: ")
        employer = input("Enter Employer Name: ")
        location = input("Enter Location: ")
        salary = input("Enter Salary: ")

        job_data_entry(title, description, employer, location, salary, posterfirst, posterlast)

        print("Successfully added a job.\n")
    else:
        print("Job limit has been reached please try again later.\n")
    return 0


# returns the application status of the given jobID and username
def check_job_status(username, jobID):
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    pnt = c.execute(
        "SELECT * FROM app_status WHERE (username = '{}' AND jobID = '{}' COLLATE NOCASE)".format(username, jobID)
    )
    check = str(pnt.fetchone())
    if check == "None":
        c.close()
        return None
    else:
        tmp = conn.execute(
            "SELECT * FROM app_status WHERE (username = '{}' AND jobID = '{}' COLLATE NOCASE)".format(
                username, jobID)
        ).fetchall()
        conn.close()
        # returns the status
        return str(tmp[0][2])


# /////////////

# applying for a job menu
def apply_job(job, current_user, firstname, lastname):
    print("Apply for Jobs:")
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    # gets the current date and time
    current_date = datetime.now()

    # checks poster
    poster = getPoster(job[0])
    if poster[1] == firstname and poster[2] == lastname:
        print("You cannot apply for a job you posted!\n")
        return False

    # checking if applied
    status = str(check_job_status(current_user, job[0]))
    if status == "applied":
        print("You already applied for this job!\n")
        return False
    elif status == "saved":  # update the status of the job to applied
        c.execute(
            "UPDATE app_status SET status = 'applied' WHERE username = '{}' AND jobID = '{}'".format(current_user,
                                                                                                     job[0])
        )
    else:  # applied for a job
        c.execute("INSERT INTO app_status VALUES ('{}', '{}', 'applied', '{}')".format(current_user, job[0],
                                                                                       current_date))
        conn.commit()

    # inputs
    grad_date = input("Enter your graduation date (mm/dd/yyyy): ")
    start_date = input("Start date you can begin work (mm/dd/yyyy): ")
    story = input("Why should you get this position: ")

    # insert a row into applications table
    # c.execute("INSERT INTO applications VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(current_user, job[1], job[3], grad_date, start_date, story))
    c.execute("INSERT INTO applications VALUES ('{}', '{}', '{}', '{}', '{}')".format(current_user, job[0], grad_date,
                                                                                      start_date, story))
    conn.commit()
    conn.close()
    # this function updates the date of the last time the user applied for a job
    update_last_applied(current_user)

    # run output APIs
    MyCollegeAppliedJobs_WriteOut()

    return True


# get all the job titles in the database
def getAllJobTitles():
    return c.execute(
        "SELECT id, title FROM Jobs WHERE id NOT IN (SELECT jobID FROM app_status WHERE status == 'deleted')").fetchall()


# get the details of the specified job ID
def getJobDetails(id):
    return c.execute(
        "SELECT * FROM Jobs WHERE id = ? AND id NOT IN (SELECT jobID FROM app_status WHERE status == 'deleted')",
        [id]).fetchone()


# get all the jobs posted by the given first name and last name
def getJobsByPoster(pFname, pLname):
    return c.execute("SELECT * FROM Jobs id WHERE id NOT IN (SELECT jobID FROM app_status WHERE status == 'deleted') "
                     "AND posterfirst = ? AND posterlast = ?", [pFname, pLname]).fetchall()


# delete a job in the database, including all the applications and remove the job from a user's saved list
def deleteJob(jobID):
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    if len(c.execute("SELECT * FROM app_status WHERE jobID = ?", [jobID]).fetchall()) == 0:
        # insert a row into app_status that indicates a job is deleted if there are no related applications
        c.execute("INSERT INTO app_status VALUES (NULL, ?, 'deleted', NULL)", [jobID])
    else:
        # update every status of entries related to that jobID to deleted
        c.execute("UPDATE app_status SET status = 'deleted' WHERE jobID = ?", [jobID])

    c.execute("DELETE FROM SavedJobs WHERE jobID = ?", [jobID])  # delete rows from SavedJobs

    conn.commit()
    conn.close()

    # run output APIs
    MyCollegeJobs_WriteOut()
    MyCollegeAppliedJobs_WriteOut()
    MyCollegeSavedJobs_WriteOut()

    return True


# add a job in the SavedJobs table
def saveJob(username, jobID):
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    try:

        c.execute("INSERT INTO SavedJobs VALUES (?,?)", [username, jobID])
        conn.commit()

        c.execute("INSERT INTO app_status VALUES ('{}', '{}', 'saved', NULL)".format(username, jobID))
        conn.commit()

        conn.close()

        # run output APIs
        MyCollegeSavedJobs_WriteOut()

        return True
    except:
        conn.close()
        return False


# remove a row from the SavedJobs table
def removeFromSavedJobs(username, jobID):
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    c.execute("DELETE FROM app_status WHERE username = ? AND jobID = ?", [username, jobID])
    c.execute("DELETE FROM SavedJobs WHERE username = ? AND jobID = ?", [username, jobID])

    conn.commit()
    conn.close()

    # run output APIs
    MyCollegeSavedJobs_WriteOut()
    return True


# gets job details by in the Jobs table associated with the given title
def getJobDetailsByTitle(title):
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    return c.execute("SELECT * FROM Jobs WHERE title = ?", [title]).fetchall()


# get all the rows in SavedJobs associated with the given username
def getAllSavedJobs(username):
    return c.execute(
        "SELECT j.id, j.title, j.description, j.employer, j.location, j.salary, j.posterfirst, j.posterlast FROM SavedJobs s INNER JOIN Jobs j ON s.jobID = j.id "
        "WHERE username = ?", [username]).fetchall()


# get the poster of the given job ID
def getPoster(jobID):
    return c.execute("SELECT id, posterfirst, posterlast FROM Jobs WHERE id = ?", [jobID]).fetchone()


# get the rows associated with the username given from the app_status table
def getDeletedApplications(username):
    return c.execute("SELECT * FROM app_status WHERE username = ? AND status = 'deleted'", [username]).fetchall()


# gets all the job titles the given username has applied for
def getAllJobTitlesAppliedFor(username):
    return c.execute(
        "SELECT j.id, j.title FROM Jobs j INNER JOIN app_status a ON j.id = a.jobID WHERE status == 'applied' AND a.username = ?",
        [username]).fetchall()


# this function will display the number of jobs the user has applied for
def applied_jobs_notification(user):
    jobs = getAllJobTitlesAppliedFor(user)
    print("\nYou have currently applied for ", len(jobs), " jobs.\n")
    return 0


# function for notifying the user that a job they have applied for has been deleted
def checkAppliedJobsDelete(username):
    jobsDeleted = c.execute(
        "SELECT j.title FROM Jobs j INNER JOIN app_status a ON j.id = a.jobID WHERE status == 'deleted' AND a.username = ?",
        [username]).fetchall()
    print("\nJob that you applied for has been deleted: ")
    for job in jobsDeleted:
        print("\n")
        print(job)


# this function is to get the new posted job title
def getNewJobTitleNoti(username):
    newJobs = c.execute(
        "SELECT title FROM Jobs WHERE datePosted > (SELECT DATETIME(lastLogin) FROM Accounts WHERE username = ?)",
        [username]).fetchall()

    for newJob in newJobs:
        print("A new job " + newJob[0] + " has been posted.")


# checks if the given username hasn't applied for a job for 7 days
def moreThan7DaysApply(username):
    lastTimeApply = c.execute(
        "SELECT * FROM app_status WHERE dateApplied > datetime('now', '-7 days') AND status = 'applied' AND username = ?",
        [username]).fetchall()

    if lastTimeApply == None:
        return True
    else:
        return False


# notification for new users in the database
def getNewUserNoti(username):
    newUsers = c.execute(
        "SELECT firstname, lastname FROM Accounts WHERE dateCreated > (SELECT DATETIME(lastLogin) FROM Accounts WHERE username = ?)",
        [username]).fetchall()

    for newUser in newUsers:
        print(newUser[0] + " " + newUser[1] + " has joined inCollege")
