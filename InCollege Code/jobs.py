import sqlite3
from getpass import getpass
from sqlite3.dbapi2 import Error

conn = sqlite3.connect('InCollege.db')
c = conn.cursor()


# /////////////////////////////////////////////////////////////////////////     ENTER DATA INTO DB     ////////////////////////////////////////////////////////////////////

# inserts login info from user into table
def job_data_entry(title, description, employer, location, salary, posterfirst, posterlast):
    # SQL
    query = """INSERT INTO Jobs(title, description, employer, location, salary, posterfirst, posterlast) VALUES(?, ?, ?, ?, ?, ?, ?);"""

    # Stores username, password , firstname , lastname
    data = (title, description, employer, location, salary, posterfirst, posterlast)
    c.execute(query, data)
    conn.commit()


# /////////////////////////////////////////////////////////////////////////     NUMBER OF JOBS    /////////////////////////////////////////////////////////////////////////

# number of jobs created
def job_created():
    # SQL
    rows = -1
    try:
        query = """SELECT * FROM Jobs"""
        c.execute(query)
        conn.commit()

        rows = len(c.fetchall())
    except Error:
        rows = 0
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


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# username shows job selected, or returns "0" to go back
def list_jobs(username):
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    jobs = c.execute("SELECT * FROM jobs").fetchall()
    store_list = []
    count = 1
    print("0. Back")
    for i in jobs:
        # sends  title posted
        store_list.append(i)
        tmp = check_job_status(username, i[1], i[0])
        print(str(count) + ". " + "Title: " + str(i[1]) + "\t Employer: " + str(i[3]) + "\t Location: " + str(
            i[4]) + "\t Salary: " + str(i[5]) + "\t Description: " + str(i[2]) + "\t Status:" + tmp)
        count += 1

    conn.close()

    selection = job_selection(count - 1)
    if (selection == 0):
        return 0

    return store_list[selection - 1]


# //////////

def check_job_status(username, title, posted):
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    pnt = c.execute(
        "SELECT * FROM app_status WHERE (username = '{}' AND title = '{}' AND posted = '{}' COLLATE NOCASE)".format(
            username, title, posted))
    check = str(pnt.fetchone())
    if check == "None":
        c.close()
        return "None"
    else:
        tmp = conn.execute(
            "SELECT * FROM app_status WHERE (username = '{}' AND title = '{}' AND posted = '{}' COLLATE NOCASE)".format(
                username, title, posted)).fetchall()
        conn.close()
        # returns the status
        return str(tmp[0][3])


# /////////////

def apply_job(job, current_user):
    print("Apply for Jobs:")
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    # checks poster
    if (str(job[0]) == str(current_user)):
        print("Posted job, cannot apply.")
        return

    # checking if applied
    status = str(check_job_status(current_user, job[1], job[0]))
    if status == "applied":
        print("Already applied")
        return
    elif status == "saved":
        c.execute(
            "UPDATE app_status SET status = 'applied' WHERE username = '{}' AND title = '{}' AND status = 'saved'".format(
                current_user, job[1]))

    else:
        c.execute("INSERT INTO app_status VALUES ('{}', '{}', '{}', 'applied')".format(current_user, job[1], job[0]))

    # inputs
    grad_date = input("Graduation date (mm/dd/yyyy)\n")
    start_date = input("Start date you can begin work (mm/dd/yyyy)\n")
    story = input("Why should you get this position.\n")

    # insert app
    c.execute(
        "INSERT INTO applications VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(current_user, job[1], job[3],
                                                                                      grad_date, start_date, story))
    conn.commit()

    # /////////

    # for deletion

def job_deleted(username):
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()
    tmp = c.execute("SELECT * FROM app_status WHERE username = '{}' AND status = 'deleted'".format(username))
    if str(tmp.fetchone()) == "None":
        conn.close()
        return False
    else:
        c.execute("DELETE FROM app_status WHERE username = '{}' AND status = 'deleted'".format(username))
        conn.commit()
        conn.close()
    return True

# get all the job titles in the database
def getAllJobTitles():
    return c.execute("SELECT id, title FROM Jobs").fetchall()


# get the details of the specified job ID
def getJobDetails(id):
    return c.execute("SELECT * FROM Jobs WHERE id = ?", [id]).fetchone()


# get all the jobs posted by the given first name and last name
def getJobsByPoster(pFname, pLname):
    return c.execute("SELECT * FROM Jobs WHERE posterfirst = ? AND posterlast = ?", [pFname, pLname]).fetchall()

# TODO: delete associated applications when a job is deleted

# delete a job in the database
def deleteJob(jobID):
    c.execute("DELETE FROM Jobs WHERE id = ?", [jobID])
    conn.commit()
    return True


# add a job in the SavedJobs table
def saveJob(username, jobID):
    try:
        c.execute("INSERT INTO SavedJobs VALUES (?,?)", [username, jobID])
        conn.commit()
        return True
    except:
        return False


# remove a row from the SavedJobs table
def removeFromSavedJobs(username, jobID):
    c.execute("DELETE FROM SavedJobs WHERE username = ? AND jobID = ?", [username, jobID])
    conn.commit()
    return True


# get all the rows in SavedJobs associated with the given username
def getAllSavedJobs(username):
    return c.execute("SELECT j.id, j.title, j.description, j.employer, j.location, j.salary, j.posterfirst, j.posterlast FROM SavedJobs s INNER JOIN Jobs j ON s.jobID = j.id "
                     "WHERE username = ?", [username]).fetchall()