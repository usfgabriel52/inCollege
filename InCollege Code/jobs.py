import sqlite3
from getpass import getpass
from sqlite3.dbapi2 import Error

conn = sqlite3.connect('InCollege.db')
c = conn.cursor()


#/////////////////////////////////////////////////////////////////////////     ENTER DATA INTO DB     ////////////////////////////////////////////////////////////////////

#inserts login info from user into table
def job_data_entry(title, description, employer, location, salary, posterfirst, posterlast):
    #SQL
    query = """INSERT INTO Jobs(title, description, employer, location, salary, posterfirst, posterlast) VALUES(?, ?, ?, ?, ?, ?, ?);"""
    
    #Stores username, password , firstname , lastname 
    data = (title, description, employer, location, salary, posterfirst, posterlast)
    c.execute(query, data)
    conn.commit()

#/////////////////////////////////////////////////////////////////////////     NUMBER OF JOBS    /////////////////////////////////////////////////////////////////////////

#number of jobs created 
def job_created():
    #SQL
    rows = -1
    try:
        query = """SELECT * FROM Jobs"""
        c.execute(query)
        conn.commit()
        
        rows = len(c.fetchall())
    except Error:
        rows = 0
    return rows

#/////////////////////////////////////////////////////////////////////////     POST A JOB    ////////////////////////////////////////////////////////////////////////////

def postJob(posterfirst, posterlast):
    
    print("\nPost A Job.\n")

    ExistingJobs = 0
    
    if job_created() < 5:
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

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#username shows job selected, or returns "0" to go back
def list_jobs(username):
    c = sqlite3.connect('InCollege.db')
    conn = c.cursor()

    jobs = conn.execute("SELECT * FROM jobs").fetchall()
    store_list = []
    count = 1
    print("0. Back")
    for i in jobs:
        
        #sends  title posted
        store_list.append(i)
        tmp = check_job_status(username, i[1], i[0])
        print(str(count) + ". " +  "Title: " + str(i[1]) + "\t Employer: " + str(i[3]) + "\t Location: " + str(i[4]) + "\t Salary: " + str(i[5]) + "\t Description: " + str(i[2]) + "\t Status:"+ tmp)
        count += 1
    
    c.close()

    selection = job_selection(count-1)
    if(selection == 0):
        return 0

    return store_list[selection-1]

#/////////////

def apply_job(job, current_user):
    print("Apply for Jobs:")
    c = sqlite3.connect('InCollege.db')
    conn = c.cursor()    

    #checks poster
    if(str(job[0]) == str(current_user)):
        print("Posted job, cannot apply.")
        return

    #checking if applied, if not it will 
    status = str(check_job_status(current_user, job[1], job[0]))
    if status == "applied":
        print("Already applied")
        return
    elif status == "saved":
        conn.execute("UPDATE app_status SET status = 'applied' WHERE username = '{}' AND title = '{}' AND status = 'saved'".format(current_user, job[1]))
   
    else:
        conn.execute("INSERT INTO app_status VALUES ('{}', '{}', '{}', 'applied')".format(current_user, job[1], job[0]))

    #inputs 
    grad_date = input("Graduation date (mm/dd/yyyy)\n")
    start_date = input("Start date you can begin work (mm/dd/yyyy)\n")
    story = input("Why should you get this position.\n")
    
    #insert application to table
    conn.execute("INSERT INTO applications VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(current_user, job[1], job[3], grad_date, start_date, story))
    c.commit()
