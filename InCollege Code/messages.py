from personalProfile import *
from friends import findFriends
from verify_acc import unique_user
from training import *
import verify_acc as acc
import menus as menu


#/////////////////////////////////////////////////////////////////////////     SEND MESSAGES    ////////////////////////////////////////////////////////////////////////////////

def send_message(sender, membership):

    if membership == "Standard":

        displayFriends(sender)

        recipient = input("\nEnter the username of the person you want to send a message to: ")

        if is_friend(sender,recipient):
            message = input("\nPlease enter your message: ")
            store_message(sender, recipient, message)
            print("\nMessage Has Been Sent.\n")
        else:
            print("I'm sorry, you are not friends with that person.")

    elif membership == "Plus":

        displayAllUsers()

        recipient = input("\nEnter the username of the person you want to send a message to: ")

        if unique_user(recipient):
            message = input("\nPlease enter your message: ")
            store_message(sender, recipient, message)
            print("\nMessage Has Been Sent.\n")
        else:
            print("I'm sorry, This person is not in the system yet.")

    return 0

#/////////////////////////////////////////////////////////////////////////     STORE MESSAGES    ////////////////////////////////////////////////////////////////////////////////

def store_message(sender, recipient, text):

    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    query = """INSERT INTO messages (sender, recipient, text) VALUES(?, ?, ?);"""

    data = (sender,recipient, text)
    c.execute(query, data)
    conn.commit()
    conn.close()
    return 0

#///////////////////

def inboxNotification(username):
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    inlist = c.execute("SELECT * FROM messages WHERE recipient = '{}'".format(username)).fetchall()

    conn.close()

    if len(inlist):
        return True
    else:
        return False




#//////// validation of input
def user_input(maxIn):

    my_select = input("\nEnter selection: ")

    numSelect = int(my_select)
    while not my_select.isnumeric() or (numSelect > maxIn or numSelect < 1):
        my_select = input("\nEnter a valid selection: ")
        numSelect = int(my_select)

    return int(my_select)

#/////////

def inbox(username, membership):
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    inlist = c.execute("SELECT * FROM messages WHERE recipient = '{}'".format(username)).fetchall()

    if len(inlist) != 0:
        print("\nInbox:")
        count = 1
        for i in inlist:
            print("\n{}. {}:\t{}".format(count, i[0], i[2]))
            count += 1

        #    option to reply or delete
        print("\nSelect a message to reply / delete, or 0 to go back.")
        message_select = user_input(len(inlist))

        print("\n0. Go back\n1. Reply\n2. Delete")
        option_select = user_input(2)

        if option_select == 1:
        #   sends reply
            send_message(username, membership)
            print("Reply sent.")
            conn.close()
            return 1

        else:
            #   deletes message
            c.execute("DELETE FROM messages WHERE sender = '{}' AND recipient = '{}' AND text = '{}'".
                    format(inlist[message_select][0], inlist[message_select][1], inlist[message_select][2]))
            print("\nMessage has been deleted.")
            conn.commit()
            conn.close()
            return 0

    #  inbox empty
    else:
        print("\n  The inbox is empty")
        conn.close()
        return -1
    conn.close()
    return None


#///////////////////////


def displayFriends(currUser):
    print("\nFriends list:")
    friends = findFriends(currUser)
    if len(friends) > 0:
        i = 1
        for f in findFriends(currUser):
            print(str(i) + ". " + f[1] + " " + f[2] + " (" + f[0] + ")")
            i += 1
        print("\n")
        return 1
    else:
        print("You don't have any friends!\n")
    return None



def displayAllUsers():

    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    print("\n")
    print("{:<15} {:<15} {:<15}".format('Username:', 'First Name:', 'Last Name:'))
    for row in c.execute("""SELECT * FROM Accounts"""):
        print("{:<15} {:<15} {:<15}".format(row[0], row[2], row[3]))
    print("\n")
    conn.close()
    return 0



def is_friend(userName,friend):

    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    query = """SELECT friend FROM friends WHERE username = ? AND friend = ?"""
    data = [userName, friend]
    c.execute(query, data)
    tuple = c.fetchall()
    conn.close()
    return len(tuple) != 0


def delete_message(sender,recipient,text):
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    query = """DELETE FROM messages WHERE recipient = ? AND sender = ? AND text = ?"""
    data = (sender, recipient, text)
    c.execute(query, data)
    conn.commit()
    conn.close()
    return 0

#/////////////////////////////////////////////////////////////////////////     PRINT SUCCESS STORY     /////////////////////////////////////////////////////////////////////////

def printStudentSuccess():
    print("\nInCollege is an amazing way to learn skills and search for a job.\n"
          "Being a college student, I struggled to find a job in my field that I was interested in and worked well with my school schedule.\n"
          "However, after signing up with InCollege I was able to find the job of my dreams and learn some very valuable skills along the way.\n"
          "I highly recommend InCollege to anyone who is searching for a job, wants to learn new skills, or meet some amazing people.\n"
          "\n - John Smith.\n")
    return 0

#/////////////////////////////////////////////////////////////////////////     PRINT HOME MENU     ////////////////////////////////////////////////////////////////////////////

def printHomeMenu():
    print("(1) Login\n"
          "(2) Register\n"
          "(3) Find A Person\n"
          "(4) View Video\n"
          "(5) Useful Links Menu\n"
          "(6) InCollege Important Links Menu\n"
          "(7) Training\n"
          "(0) Exit\n")
    return 0

#/////////////////////////////////////////////////////////////////////////     PRINT INVALID ENTRY     ////////////////////////////////////////////////////////////////////////

def printInvalidEntry():
    print("\nINVALID ENTRY PLEASE TRY AGAIN.\n")

#/////////////////////////////////////////////////////////////////////////     PRINT UNDER CONSTRUCTION     ///////////////////////////////////////////////////////////////////

def printUnderConstruction():
    print("\nUnder Construction...\n")
    return 0

#/////////////////////////////////////////////////////////////////////////     PRINT MAIN MENU    /////////////////////////////////////////////////////////////////////////////

def printMainMenu(userName):
    if hasProfile(userName):
        print("InCollege Main Menu\n"
              "(1) Job search / internship\n"
              "(2) Find someone you know\n"
              "(3) Learn a new skill\n"
              "(4) Useful Links\n"
              "(5) Important Links\n"
              "(6) My Network\n"
              "(7) Edit Personal Profile\n"
              "(8) View Personal Profile\n"
              "(9) View/Send Messages\n"
              "(10) In College Learning\n"
              "(0) Logout\n")
    else:
        print("InCollege Main Menu\n"
              "(1) Job search / internship\n"
              "(2) Find someone you know\n"
              "(3) Learn a new skill\n"
              "(4) Useful Links\n"
              "(5) Important Links\n"
              "(6) Show My Network\n"
              "(7) Create Personal Profile\n"
              "(9) View/Send Messages\n"
              "(10) In College Learning\n"
              "(0) Logout\n")
    return 0

#/////////////////////////////////////////////////////////////////////////     PRINT SKILL LIST     ///////////////////////////////////////////////////////////////////////////

def printSkillList():

    print("Skill list: ")  # tentative skill list

    print("(1) Python Programming\n"
          "(2) Java Programming\n"
          "(3) C++ Programming\n"
          "(4) Time Management\n"
          "(5) Effective communication\n"
          "(0) Return to Previous Menu\n")
    return 0

#/////////////////////////////////////////////////////////////////////////     PRINT JOB MENU     /////////////////////////////////////////////////////////////////////////////

def printJobMenu():

    print("(1) Post a job\n"
          "(2) View all job titles\n"
          "(3) View all jobs you have posted\n"
          "(4) Delete a job you have posted\n"
          "(5) View all saved jobs\n"
          "(6) View all jobs you have applied for\n"
          "(0) Return to Previous Menu.\n")
    return 0

#/////////////////////////////////////////////////////////////////////////     PRINT IMPORTANT LINKS MENU     ///////////////////////////////////////////////////////////////////

def printImpLinksMenu():

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
          "(10) Languages\n"
          "(0) Return to Previous Menu\n")
    return

#/////////////////////////////////////////////////////////////////////////     PRINT USEFUL LINKS MENU     ///////////////////////////////////////////////////////////////////

def printUsefulLinksMenu():

    print("Useful Links Menu\n"
          "(1) General\n"
          "(2) Browse InCollege\n"
          "(3) Business Solutions\n"
          "(4) Directories\n"
          "(0) Return to Previous Menu\n")

    return

#/////////////////////////////////////////////////////////////////////////     PRINT USEFUL GENERAL MENU     ///////////////////////////////////////////////////////////////////

def printUsefulGeneralGroup():

    print("Useful Links Menu\n"
          "(1) Sign Up\n"
          "(2) Help Center\n"
          "(3) About\n"
          "(4) Press\n"
          "(5) Blog\n"
          "(6) Careers\n"
          "(7) Developers\n"
          "(0) Return to Previous Menu\n")
    return

#/////////////////////////////////////////////////////////////////////////     PRINT GUEST CONTROL MENU     //////////////////////////////////////////////////////////////////////

def printGuestControlMenu():

    print("Guest Control Menu\n"
          "(1) Turn ON/OFF Email\n"
          "(2) Turn ON/OFF SMS\n"
          "(3) Turn ON/OFF Ads\n"
          "(4) Change Language\n"
          "(0) Return to Previous Menu\n")
    return

#/////////////////////////////////////////////////////////////////////////     PRINT LANGUAGE MENU     //////////////////////////////////////////////////////////////////////////

def printLanguageMenu():

    print("Language Menu\n"
          "(1) Change Language to English\n"
          "(2) Change Language to Spanish\n"
          "(0) Return to Previous Menu\n")
    return

#/////////////////////////////////////////////////////////////////////////     PRINT PRIVACY POLICY MENU     ////////////////////////////////////////////////////////////////////


def printPrivacyPolicyMenu():

    print("Privacy Policy Menu\n"
          "(1) View Privacy Policy\n"
          "(2) Guest Controls\n"
          "(0) Return to Previous Menu\n")
    return
#//////////////////////////////////////////////////////////////////////////     HAS REQUEST     /////////////////////////////////////////////////////////////////

def printHasRequest():
    print("You have a new friend request!\n")
    return

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def printFriendsMenu():
    print("Friends Menu \n"
          "(1) View friends list\n"
          "(2) View pending friend requests\n"
          "(3) Add a friend\n"
          "(4) Remove a friend\n"
          "(5) View a friend's profile\n"
          "(0) Return to previous menu\n")
    return

def printJobOptionsMenu():
    print("What would you like to do?\n"
          "\t(1) Apply for job\n"
          "\t(2) Save job for later\n"
          "\t(0) Cancel\n")

def printSavedJobOptionsMenu():
    print("What would you like to do?\n"
          "\t(1) Apply for job\n"
          "\t(2) Remove job from list\n"
          "\t(0) Cancel\n")

#/////////////////////////////////////////////////////////////////////////     PRINT MESSAGES MENU    /////////////////////////////////////////////////////////////////////////////

def printMessagesMenu():

    print("\nMessages Menu\n"
          "(1) View Messages\n"
          "(2) Send Message\n"
          "(0) Return to Previous Menu\n")
    return

#/////////////////////////////////////////////////////////////////////////     PRINT TRAINING MENU    /////////////////////////////////////////////////////////////////////////////

def printTrainingMenu():
    print("\nTraining Menu\n"
          "(1) Training and Education\n"
          "(2) IT Help Desk\n"
          "(3) Business Analysis and Strategy\n"
          "(4) Security\n"
          "(0) Exit\n")
    return 0

#/////////////////////////////////////////////////////////////////////////     PRINT TRAINING AND EDUCATION MENU    ///////////////////////////////////////////////////////////////

def printTrainAndEduMenu():
    print("\nTraining and Education Menu\n"
          "(1) Coding\n"
          "(2) Resume Building\n"
          "(3) Public Speaking\n"
          "(4) Making A Presentation\n"
          "(0) Exit\n")
    return 0

#/////////////////////////////////////////////////////////////////////////     PRINT BUSINESS ANALYSIS AND STRATEGY MENU    /////////////////////////////////////////////////////////////////////////////

def printBusinessAnalysisMenu():
    
    print("\nBusiness Analysis and Strategy Menu\n"
        "(1) How to use InCollege learning\n"
        "(2) Train the trainer\n"
        "(3) Gamification of learning\n"
        "(0) Exit\n")

    return 0    

#/////////////////////////////////////////////////////////////////////////     PRINT IN COLLEGE LEARNING MENU    /////////////////////////////////////////////////////////////////////////////

def printInCollegeLearningMenu(username):
    print("InCollege Learning Menu\n")

    training = checkTraining(username)

    for i in range(0, len(training)):
        print("(" + str(i + 1) + ") " + training[i][0] + " - " + training[i][1])
    print("(0) Exit")

    return 0


def printAlreadyTakenTraining():
    print("You have already taken this training\n"
        "Would you like to take it again?\n"
        "1 = yes, 0 = no\n")

def printCompletedTraining():
    print("You have now completed this training\n")

def printCourseCancelled():
    print("Course Cancelled\n")