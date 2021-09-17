import pandas as pd

global logged_in

# This function displays the Login Menu
def display_LoginMenu():
    print("\nLog In to InCollege\n")

    found = False

    while not found:  # continue looping as long as user inputs invalid login info
        # get input from the user
        username = input("Enter username: ")
        password = input("Enter password: ")
        found = find_account(username, password)
        if not found:
            print("Incorrect username/password, please try again\n")
    print("\nYou have successfully logged in\n")
    logged_in = True
    display_MainMenu()

# This function displays the screen that allows a user to create an account
def display_RegisterMenu():
    print("\nCreate a New Account\n")
    accounts = pd.read_csv('accounts.csv', index_col=0, squeeze=True).to_dict()
    # TODO: looping while user inputs invalid values
    if len(accounts.keys()) < 6:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if not username in accounts or password_check(password):
            accounts[username] = password
            print("Successfully created an account\n")
    else:
        print("All permitted accounts have been created, please come back later\n")

    df = pd.DataFrame(accounts.items())
    df.to_csv('accounts.csv', index=False)

# This function displays the Main Menu after the user has logged in
def display_MainMenu():
    print("InCollege Main Menu\n"
          "(1) Search for a job\n"
          "(2) Find someone you know\n"
          "(3) Learn a new skill\n"
          "(0) Logout\n")
    opt = input("Enter command: ")

    if int(opt) == 1 or int(opt) == 2:
        print("Under construction\n")
        display_MainMenu()
    elif int(opt) == 3:
        print("Skill list: ")
        print("(1) Python Programming\n"
              "(2) Java Programming\n"
              "(3) C++ Programming\n"
              "(4) Time Management\n"
              "(5) Effective communication\n"
              "(0) Return to Main Menu")
        skill = input("Select a skill: ")
        if skill != 0:
            print("Under construction\n")
        display_MainMenu()
    else:
        logged_in = False
        main()

# This function looks for the given username and password in the CSV file
def find_account(findUsername, findPassword):
    # get all the accounts from the csv file
    accounts = pd.read_csv('accounts.csv', index_col=0, squeeze=True).to_dict()

    # initialize temp values to False
    un = False
    pw = False

    for u in accounts.keys():
        if u == findUsername:
            un = True  # change value of un to True if found

    for p in accounts.values():
        if p == findPassword:
            pw = True  # change value of pw to True if found

    return pw and un

# Function to validate the password
def password_check(passwd):
    # declaring the special characters to be used to enter by user

    SpecialSym = ['$', '@', '#', '%']

    # variable used to determine the valid characters within the loop
    val = True

    # beginning of the loop

    # checks the minimum length validation
    if len(passwd) < 8:
        print('length should be at least 8')
        val = False

    # checks the max length validation
    if len(passwd) > 12:
        print('length should be not be greater than 12')
        val = False

    # checks for 1 digit input
    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one digit')
        val = False

    # checks for Upper case input
    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False

    # checks for special synbol inout
    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False

    # checks if inputs are valid
    if val:
        return val


# Main method
def main():
    opt = -1  # tentative value

    while opt != 0:
        print("Welcome to InCollege!")

        print("(1) Login\n"
              "(2) Register\n"
              "(0) Exit\n")
        opt = int(input("Enter command: "))

        if opt == 1:
            display_LoginMenu()
        elif opt == 2:
            display_RegisterMenu()

    print("Thank you for using InCollege!")


# Driver Code
if __name__ == '__main__':
    main()

