import sqlite3
import pytest
import io
import personalProfile
import menus
import verify_acc
import jobs
import OutputApis
import os.path
import input_APIs
import training
import friends

# #function ro test whether remove friend function works
# def test_removeFriend():
#     friends.removeFriend("nhandang", "test")
#     conn = sqlite3.connect('InCollege.db')
#     c = conn.cursor()
#
#     query = ("SELECT FROM friends WHERE userName  = ? AND friend = ?")
#     data=("nhandang", "test")
#     assert c.execute(query, data) == ""
#
# #function to check user friendlist initiated empty
# def test_initialFriendList():
#     conn = sqlite3.connect('InCollege.db')
#     c = conn.cursor()
#
#     query = ("SELECT FROM friends WHERE userName  = ? ")
#     data=("nhandang")
#     assert c.execute(query, data) == ""
#
# #function to test user can see all list jobs and description
# def test_listJob():
#     conn = sqlite3.connect('InCollege.db')
#     c = conn.cursor()
#     jobs.postJob("asds", "adsd")
#     assert jobs.getAllJobTitles() == c.execute("SELECT id, title FROM Jobs").fetchall()
#     assert jobs.getJobDetails(1) == c.execute("SELECT * FROM Jobs WHERE id = ?", [1]).fetchone()
#
# #function to test user can filter to see job have not applied
# def test_filterNotAppliedJob():
#     conn = sqlite3.connect('InCollege.db')
#     c = conn.cursor()
#     assert jobs.getAllJobTitlesAppliedFor == c.execute("SELECT j.id, j.title FROM Jobs j INNER JOIN app_status a ON j.id = a.jobID WHERE status == 'applied' AND a.username = ?").fetchall()
#
# #function to test for check delete job
# def test_deleteJob():
#     conn = sqlite3.connect('InCollege.db')
#     c = conn.cursor()
#     assert jobs.getAllJobTitlesAppliedFor == c.execute("SELECT * FROM app_status WHERE username = ? AND status = 'deleted").fetchall()
#
# #function to check course take again
# def test_takeAgainJob(username):
#     conn = sqlite3.connect('InCollege.db')
#     c = conn.cursor()
#     assert training.checkTraining(username) == c.execute("SELECT * FROM Training WHERE username = ? ", username).fetchall()[0]


# This function tests the training input API
def test_training_inAPI():
    # Creates a database for the training if one doesnt exist
    verify_acc.create_tables()
    # check if the file exists
    file_exists = os.path.exists('input files\\newtraining.txt')
    assert file_exists == True
    # reads the input API and loads data into database
    input_APIs.readTrainingFile()

    # print the contents of the output API to see it in its original state
    with open('input files\\newtraining.txt', 'r') as f:
        print(f.read())
    f.close()

    return 0

# This function tests the Job input API
def test_job_inAPI():
    # Creates a database for the training if one doesnt exist
    verify_acc.create_tables()
    # check if the file exists
    file_exists = os.path.exists('input files\\newJobs.txt')
    assert file_exists == True
    # reads the input API and loads data into database
    input_APIs.readJobsFile()

    # print the contents of the output API to see it in its original state
    with open('input files\\newJobs.txt', 'r') as f:
        print(f.read())
    f.close()

    return 0

# This function tests the Job output API
def test_job_outAPI():
    # Creates a database for the profiles if one doesnt exisit
    verify_acc.create_tables()
    # overwrite the output API with the data in the system
    OutputApis.MyCollegeJobs_WriteOut()
    # check if the file exists
    file_exists = os.path.exists("output files\\MyCollege_appliedJobs.txt")
    assert file_exists == True

    # print the contents of the output API to see it in its original state
    with open("output files\\MyCollege_appliedJobs.txt", 'r') as f:
        print(f.read())
    f.close()

    # add new job to database
    jobs.job_data_entry("Hardware Engineer", "You do computer things.", "myStartup", "Tampa,FL", "$1.00 / hr", "Larry", "Mason")
    #user apply to new job, check their name will be placed
    jobs.apply_job("Hardware Engineer", "CoolDude123", "John", "Smith")

    # print the contents of the output API to see if the data got changed
    with open("output files\\MyCollege_appliedJobs.txt", 'r') as f:
        print(f.read())
    f.close()

    return 0


# This function tests the user output API
def test_usersProfiles_outAPI():
    # Creates a database for the profiles if one doesnt exisit
    verify_acc.create_tables()
    # overwrite the output API with the data in the system
    OutputApis.MyCollegeJobs_WriteOut()
    # check if the file exists
    file_exists = os.path.exists("output files\\MyCollege_users.txt")
    assert file_exists == True

    # print the contents of the output API to see it in its original state
    with open("output files\\MyCollege_users.txt", 'r') as f:
        print(f.read())
    f.close()

    # add an account if number of accounts in database is less than 10
    if verify_acc.number_rows() < 10:
        verify_acc.data_entry("Lorna", "Shore123@", "Will", "Ramos", 1, 1, 1, "English", "Plus")

    # print the contents of the output API to see if the data got changed
    with open("output files\\MyCollege_users.txt", 'r') as f:
        print(f.read())
    f.close()

    return 0