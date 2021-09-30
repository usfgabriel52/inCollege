#imports all functions from messages.py
from messages import *
#imports all functions from search.py
from search import *
#imports all functions from jobs.py
from jobs import *

logged_in = []

#/////////////////////////////////////////////////////////////////////////     HOME MENU     /////////////////////////////////////////////////////////////////////////

def homeMenu():
    
    print("Welcome to InCollege.")
    #prints the student success story found on messages.py
    printStudentSuccess()
    
    while True:   
        #prints the home menu
        printHomeMenu()
        print("(5) Useful Links Menu\n"
              "(6) InCollege Important Links Menu\n")
        #gets user input
        select = input("Enter command: ")

        if(select == "1" or select == "2" or select == "3" or select == "4" or select == "0"or select == "5"or select == "6"):
            break
        else:
            #if user inputs an incorrect value an this function prints an error message
            printInvalidEntry()
            continue

    if(select == "1"):
        loginMenu()
    elif(select == "2"):
        createAccountMenu()
    elif(select == "3"):
        searchPeople()
    elif(select == "4"):
        print("\nVideo is now playing...\n")
    elif (select == "5"):
        usefulLinksMenu()
    elif (select == "6"):
        impLinksMenu()
    elif(select == "0"):
        print("Thank you for using InCollege!")
        quit()
    else:
        printInvalidEntry()

#/////////////////////////////////////////////////////////////////////////     LOGIN MENU     /////////////////////////////////////////////////////////////////////////

def loginMenu():
    
    print("\nLog In to InCollege\n")
    
    create_table()
    
    if number_rows() == 0:
        print("No users in the system. Please create an account.")
        return

    found = False

    while not found:  # continue looping as long as user inputs invalid login info
        # get input from the user
        username = input("Enter username: ")
        password = input("Enter password: ")

        # check if username and password are valid
        found = login(username, password)
        if not found:
            print("Incorrect username/password, please try again\n")
    print("\nYou have successfully logged in\n")
    global logged_in 
    #gets the first and last name of the current user that is logged in
    logged_in = current_user(username, password)
    mainMenu()

#/////////////////////////////////////////////////////////////////////     CREATE ACCOUNT MENU     ////////////////////////////////////////////////////////////////////

def createAccountMenu():
    
    print("\nCreate a New Account\n")

    create_table()

    if number_rows() < 5:
        username = input("Enter username: ")
        password = input("Enter password: ")
        firstname = input("Enter First Name: ")
        lastname = input("Enter Last Name: ")

        # check if username is unique and password is valid
        if not unique_user(username) and password_check(password):
            data_entry(username, password,firstname,lastname)
            print("Successfully created an account\n")
    else:
        print("All permitted accounts have been created, please come back later\n")
    return 0

#/////////////////////////////////////////////////////////////////////////     MAIN MENU     /////////////////////////////////////////////////////////////////////////

def mainMenu():
    
    while True:
        #prints the main menu
        printMainMenu()
        #gets user input
        opt = input("Enter command: ")

        if int(opt) == 1: #search for job
            jobMenu()
        elif int(opt) == 2:  
            searchPeople()
        elif int(opt) == 3:  # learn a new skill
            skillMenu()
        elif int(opt) == 4:
            usefulLinksMenu()
        elif int(opt) == 5:
            impLinksMenu()
        elif int(opt) == 0:
            global logged_in
            logged_in = []
            print("You have sucessfully logged out!\n")
            break
        else:
            printInvalidEntry()
    return 0

#/////////////////////////////////////////////////////////////////////////     SKILL MENU     /////////////////////////////////////////////////////////////////////////

def skillMenu():
    
    while True:
        #prints the list of skills
        printSkillList()
        #gets user input
        skill = input("Select a skill: ")
    
        if skill != "0":
            #prints an under construction message
            printUnderConstruction()
        elif skill == "0":
            break
        else:
            printInvalidEntry()
    return 0

#/////////////////////////////////////////////////////////////////////////     JOB MENU     ///////////////////////////////////////////////////////////////////////////

def jobMenu():
    
    while True:
        print("\nJob search/internship.\n")

        printJobMenu()
        #creates a database for jobs if one doesnt exist.
        create_job_table()

        select = input("Enter Command: ")

        if select == "1":
            postJob(logged_in[0], logged_in[1])
        elif select == "0":
            break
        else:
            printInvalidEntry()

    return


# /////////////////////////////////////////////////////////////////////////     USEFUL LINKS MENU     /////////////////////////////////////////////////////////////////////////

def usefulLinksMenu():
    print("Useful Links Menu\n"
          "(1) General\n"
          "(2) Browse InCollege\n"
          "(3) Business Solutions\n"
          "(4) Directories\n")

    # gets user input
    opt = input("Enter command: ")

    if int(opt) == 1:
        usefulGenralGroup()
    elif int(opt) == 2:
        printUnderConstruction()
    elif int(opt) == 3:
        printUnderConstruction()
    elif int(opt) == 4:
        printUnderConstruction()
    else:
        printInvalidEntry()
    return 0

# /////////////////////////////////////////////////////////////////////////     IMPORTANT LINKS MENU     /////////////////////////////////////////////////////////////////////////

def impLinksMenu():

    print("InCollege Important Links Menu\n"
          "(1) A Copyright Notice\n"
          "(2) About\n"
          "(3) Accessibility\n"
          "(4) User Agreement\n"
          "(5) Privacy Policy\n"
          "(6) Cookie Policy\n"
          "(7) Copyright Policy\n"
          "(8) Brand Policy\n"
          "(9) Guest Controls\n"
          "(10) Languages\n")

    # gets user input
    opt = input("Enter command: ")

    if int(opt) == 1:
        usefulGenralGroup()
    elif int(opt) == 2:
        printUnderConstruction()
    elif int(opt) == 3:
        printUnderConstruction()
    elif int(opt) == 4:
        printUnderConstruction()
    elif int(opt) == 5:
        printUnderConstruction() #change to call Guest Controls function
    elif int(opt) == 6:
        printUnderConstruction()
    elif int(opt) == 7:
        printUnderConstruction()
    elif int(opt) == 8:
        printUnderConstruction()
    elif int(opt) == 9:
        printUnderConstruction() #change to call Guest Controls function
    elif int(opt) == 10:
        printUnderConstruction() #change to call Languages function
    else:
        printInvalidEntry()

    return 0

# /////////////////////////////////////////////////////////////////////////     USEFUL GENERAL GROUP MENU     /////////////////////////////////////////////////////////////////////////

def usefulGenralGroup():
    print("Useful Links Menu\n"
          "(1) Sign Up\n"
          "(2) Help Center\n"
          "(3) About\n"
          "(4) Press\n"
          "(5) Blog\n"
          "(6) Careers\n"
          "(7) Developers\n")

    # gets user input
    opt = input("Enter command: ")

    if int(opt) == 1:
        createAccountMenu()
    elif int(opt) == 2:
        print("We're here to help")
    elif int(opt) == 3:
        print("In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide")
    elif int(opt) == 4:
        print( "In College Pressroom: Stay on top of the latest news, updates, and reports")
    elif int(opt) == 5:
        printUnderConstruction()
    elif int(opt) == 6:
        printUnderConstruction()
    elif int(opt) == 7:
        printUnderConstruction()
    else:
        printInvalidEntry()

    return 0


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
