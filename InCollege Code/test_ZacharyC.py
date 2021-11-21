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

#this function tests if you can create up to and no more than 10 accounts
def test_maximum_num_accounts():
    
    #Creates a database for the profiles if one doesnt exisit
    verify_acc.create_tables()
    
    #creates 10 user accounts
    verify_acc.data_entry("zchenoweth", "Chenoweth1@", "Zachary", "Chenoweth", 1, 1, 1, "English","Plus")
    verify_acc.data_entry("CoolDude123", "CoolDude1@", "John", "Smith", 1, 1, 1, "English","Standard")
    verify_acc.data_entry("tester123", "Tester123@", "Anna", "Collins", 1, 1, 1, "English","Plus")
    verify_acc.data_entry("Coder321", "Coder321@", "Henry", "Potter", 1, 1, 1, "English","Standard")
    verify_acc.data_entry("princess123", "Princess1@", "Lucy", "Johnson", 1, 1, 1, "English","Plus")
    verify_acc.data_entry("kingofpop1", "Hehe1234@", "Michael", "Jackson", 1, 1, 1, "English","Standard")
    verify_acc.data_entry("metalhead123", "Metallica1@", "James", "Hetfield", 1, 1, 1, "English","Plus")
    verify_acc.data_entry("Sweetypie", "Sweetpie1@", "Mary", "Noname", 1, 1, 1, "English","Standard")
    verify_acc.data_entry("fakeperson", "Fake1234@", "Fake", "Person", 1, 1, 1, "English","Plus")
    verify_acc.data_entry("Noideas123", "Noideas1@", "Larry", "Mason", 1, 1, 1, "English","Standard")

    print("Test to add 11th account(should print all accounts are full):")
    #should print that accounts are all full
    assert menus.createAccountMenu() == 0

    return

#THis function tests the jobs output API (Call this function to run it)
def test_jobs_outAPI():
    
    #Creates a database for the profiles if one doesnt exisit
    verify_acc.create_tables()
    #overwrite the output API with the data in the system
    OutputApis.MyCollegeJobs_WriteOut()
    #check if the file exists
    file_exists = os.path.exists("output files\\MyCollege_job.txt")
    assert file_exists == True

    #add new job to the database
    jobs.job_data_entry("Software Engineer", "You do computer things.", "myStartup", "Tampa,FL", "$1.00 / hr", "Fake", "Person")
    
    #print the contents of the output API to see if the data got changed
    with open("output files\\MyCollege_job.txt", 'r') as f:
        print(f.read())
    f.close()

    #add new job to the database
    jobs.job_data_entry("Hardware Engineer", "You do computer things.", "myStartup", "Tampa,FL", "$1.00 / hr", "Larry", "Mason")
    
    #print the contents of the output API to see if the data got changed
    with open("output files\\MyCollege_job.txt", 'r') as f:
        print(f.read())
    f.close()
    
    #delete a job from the database
    job = jobs.getJobsByPoster("Fake", "Person")  
    toDelete = 1
    jobs.deleteJob(job[int(toDelete)-1][0])  

    #print the contents of the output API to see if the data got changed
    with open("output files\\MyCollege_job.txt", 'r') as f:
        print(f.read())
    f.close()
            
    return 0


# This fuction tests the saved jobs output API ( You need to call the test_maximum_num_accounts() then this function to test it)
def test_savedJobs_outAPI():
    
    #Creates a database for the profiles if one doesnt exisit
    verify_acc.create_tables()
    #overwrite the output API with the data in the system
    OutputApis.MyCollegeSavedJobs_WriteOut()
    #check if the file exists
    file_exists = os.path.exists("output files\\MyCollege_savedJobs.txt")
    assert file_exists == True

    #save a job as a user
    job = jobs.getAllJobTitles() 
    toView = 1
    jobs.saveJob("zchenoweth", job[int(toView)-1][0])

    #print the contents of the output API to see if the data got changed
    with open("output files\\MyCollege_savedJobs.txt", 'r') as f:
        print(f.read())
    f.close()

    #save a job under a different userr
    jobs.saveJob("kingofpop1", job[int(toView)-1][0])

    #print the contents of the output API to see if the data got changed
    with open("output files\\MyCollege_savedJobs.txt", 'r') as f:
        print(f.read())
    f.close()

    #remove a job from the saved list
    jobs.removeFromSavedJobs("zchenoweth", job[int(toView)-1][0])

    #print the contents of the output API to see if the data got changed
    with open("output files\\MyCollege_savedJobs.txt", 'r') as f:
        print(f.read())
    f.close()

    return 0


# This fuction tests the training output API ( You need to call the test_maximum_num_accounts() then this function to test it)
def test_training_outAPI():

    #Creates a database for the profiles if one doesnt exisit
    verify_acc.create_tables()
    #overwrite the output API with the data in the system
    OutputApis.MyCollegeJobs_WriteOut()
    #check if the file exists
    file_exists = os.path.exists("output files\\MyCollege_training.txt")
    assert file_exists == True

    #print the contents of the output API to see it in its original state    
    with open("output files\\MyCollege_training.txt", 'r') as f:
        print(f.read())
    f.close()

    #complete a training as a user
    training.CompleteTraining("zchenoweth", 1)
    
    #print the contents of the output API to see if the data got changed
    with open("output files\\MyCollege_training.txt", 'r') as f:
        print(f.read())
    f.close()

    #Complete a training as another user
    training.CompleteTraining("kingofpop1", 1)
    
    #print the contents of the output API to see if the data got changed
    with open("output files\\MyCollege_training.txt", 'r') as f:
        print(f.read())
    f.close()

    return 0


# This function tests the user output API
def test_users_outAPI():

    #Creates a database for the profiles if one doesnt exisit
    verify_acc.create_tables()
    #overwrite the output API with the data in the system
    OutputApis.MyCollegeJobs_WriteOut()
    #check if the file exists
    file_exists = os.path.exists("output files\\MyCollege_users.txt")
    assert file_exists == True
    
    #print the contents of the output API to see it in its original state 
    with open("output files\\MyCollege_users.txt", 'r') as f:
        print(f.read())
    f.close()

    #add an account if number of accounts in database is less than 10
    if verify_acc.number_rows() < 10:
        verify_acc.data_entry("Lorna", "Shore123@", "Will", "Ramos", 1, 1, 1, "English","Plus")

    #print the contents of the output API to see if the data got changed
    with open("output files\\MyCollege_users.txt", 'r') as f:
        print(f.read())
    f.close()
    
    return 0  


#This function tests the student accounts input API
def test_studentAccounts_inAPI():

    #Creates a database for the profiles if one doesnt exisit
    verify_acc.create_tables()
    #check if the file exists
    file_exists = os.path.exists('input files\\studentAccounts.txt')
    assert file_exists == True
    #reads the input API and loads data into database
    input_APIs.readAccountsFile()
    
    #print the contents of the output API to see it in its original state 
    with open('input files\\studentAccounts.txt', 'r') as f:
        print(f.read())
    f.close()
    
    return 0  

# YOU CAN UNCOMMENT THESE FUNCTION CALLS TO TEST ALL THE FUNCTIONS

# test_maximum_num_accounts()
# test_jobs_outAPI()
# test_savedJobs_outAPI()
# test_training_outAPI()
# test_users_outAPI()
# test_studentAccounts_inAPI()
