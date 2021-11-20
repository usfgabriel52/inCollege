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





#This function tests if the format for major and university name meets the specified requirements 
def test_formatCaps():
    assert personalProfile.formatCaps("hEllO WoRLD!!!") == "Hello World!!!"
    assert personalProfile.formatCaps("hEllO") == "Hello"
    assert personalProfile.formatCaps("This is A test") == "This Is A Test"
    return



# this function tests to see if the show my network menu appears properly
def test_show_my_network(monkeypatch):
    input = '0\n'
    monkeypatch.setattr('sys.stdin', io.StringIO(input))
    assert menus.friendsMenu() == 1
    return



def test_jobs_outAPI():
    
    #Creates a database for the profiles if one doesnt exisit
    verify_acc.create_tables()
    OutputApis.MyCollegeJobs_WriteOut()
    file_exists = os.path.exists("output files\\MyCollege_job.txt")
    assert file_exists == True

    jobs.job_data_entry("Software Engineer", "You do computer things.", "myStartup", "Tampa,FL", "$1.00 / hr", "Fake", "Person")
    
    with open("output files\\MyCollege_job.txt", 'r') as f:
        print(f.read())
    f.close()

    jobs.job_data_entry("Hardware Engineer", "You do computer things.", "myStartup", "Tampa,FL", "$1.00 / hr", "Larry", "Mason")
    
    with open("output files\\MyCollege_job.txt", 'r') as f:
        print(f.read())
    f.close()
    
    job = jobs.getJobsByPoster("Fake", "Person")  
    toDelete = 1
    jobs.deleteJob(job[int(toDelete)-1][0])  

    with open("output files\\MyCollege_job.txt", 'r') as f:
        print(f.read())
    f.close()
            
    return 0



def test_savedJobs_outAPI():
    
    #Creates a database for the profiles if one doesnt exisit
    verify_acc.create_tables()
    OutputApis.MyCollegeSavedJobs_WriteOut()
    file_exists = os.path.exists("output files\\MyCollege_savedJobs.txt")
    assert file_exists == True

    job = jobs.getAllJobTitles() 
    toView = 1
    jobs.saveJob("zchenoweth", job[int(toView)-1][0])

    with open("output files\\MyCollege_savedJobs.txt", 'r') as f:
        print(f.read())
    f.close()

    jobs.saveJob("kingofpop1", job[int(toView)-1][0])

    with open("output files\\MyCollege_savedJobs.txt", 'r') as f:
        print(f.read())
    f.close()

    jobs.removeFromSavedJobs("zchenoweth", job[int(toView)-1][0])

    with open("output files\\MyCollege_savedJobs.txt", 'r') as f:
        print(f.read())
    f.close()

    return 0



def test_training_outAPI():

    #Creates a database for the profiles if one doesnt exisit
    verify_acc.create_tables()
    OutputApis.MyCollegeJobs_WriteOut()
    file_exists = os.path.exists("output files\\MyCollege_training.txt")
    assert file_exists == True

    training.CompleteTraining("zchenoweth", 1)
    
    with open("output files\\MyCollege_training.txt", 'r') as f:
        print(f.read())
    f.close()

    training.CompleteTraining("kingofpop1", 1)
    
    with open("output files\\MyCollege_training.txt", 'r') as f:
        print(f.read())
    f.close()

    return 0



def test_users_outAPI():

    #Creates a database for the profiles if one doesnt exisit
    verify_acc.create_tables()
    OutputApis.MyCollegeJobs_WriteOut()
    file_exists = os.path.exists("output files\\MyCollege_users.txt")
    assert file_exists == True
    
    with open("output files\\MyCollege_users.txt", 'r') as f:
        print(f.read())
    f.close()

    if verify_acc.number_rows() < 10:
        verify_acc.data_entry("Lorna", "Shore123@", "Will", "Ramos", 1, 1, 1, "English","Plus")

    with open("output files\\MyCollege_users.txt", 'r') as f:
        print(f.read())
    f.close()
    
    return 0  



def test_studentAccounts_inAPI():

    #Creates a database for the profiles if one doesnt exisit
    verify_acc.create_tables()
    input_APIs.readAccountsFile()
    file_exists = os.path.exists('input files\\studentAccounts.txt')
    assert file_exists == True

    with open('input files\\studentAccounts.txt', 'r') as f:
        print(f.read())
    f.close()
    
    return 0  