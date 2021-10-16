import sqlite3
import pytest
import io
import personalProfile
import menus
import verify_acc

#This function tests if a profile database is created and if a Student can create a profile and add it to the database
def test_create_profile():

    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    #create the database if it doesnt already exist
    verify_acc.create_tables()
    #creates a new profile and stores it in the database
    personalProfile.create_profile("coolDude123")

    # display contents of db before signing up
    for r in c.execute("SELECT * FROM personalProfile"):
        print(r)

    #creates a new profile and stores it in the database
    personalProfile.create_profile("zchenoweth")
    print("\n")
    # display contents of db after signing up
    for r in c.execute("SELECT * FROM personalProfile"):
        print(r)
    return



#This function tests if the format for major and university name meets the specified requirements 
def test_formatCaps():
    assert personalProfile.formatCaps("hEllO WoRLD!!!") == "Hello World!!!"
    assert personalProfile.formatCaps("hEllO") == "Hello"
    assert personalProfile.formatCaps("This is A test") == "This Is A Test"
    return



#this function tests if you can create up to and no more than 10 accounts
def test_maximum_num_accounts(monkeypatch):
    
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    #Creates a database for the profiles if one doesnt exisit
    verify_acc.create_tables()
    
    input = 'zchenoweth\nChenoweth0@\nZachary\nChenoweth\n0\n0\n0'
    monkeypatch.setattr('sys.stdin', io.StringIO(input))
    assert menus.createAccountMenu() == 0

    input = 'CoolDude123\nCoolDude1@\nJohn\nSmith\n0\n0\n0'
    monkeypatch.setattr('sys.stdin', io.StringIO(input))
    assert menus.createAccountMenu() == 0
    
    input = 'tester123\nTester123@\nAnna\nCollins\n0\n0\n0'
    monkeypatch.setattr('sys.stdin', io.StringIO(input))
    assert menus.createAccountMenu() == 0

    input = 'Coder321\nCoder321@\nHenry\nPotter\n0\n0\n0'
    monkeypatch.setattr('sys.stdin', io.StringIO(input))
    assert menus.createAccountMenu() == 0

    input = 'princess123\nPrincess1@\nLucy\nJohnson\n0\n0\n0'
    monkeypatch.setattr('sys.stdin', io.StringIO(input))
    assert menus.createAccountMenu() == 0

    input = 'kingofpop1\nHehe1234@\nMichael\nJackson\n0\n0\n0'
    monkeypatch.setattr('sys.stdin', io.StringIO(input))
    assert menus.createAccountMenu() == 0

    input = 'metalhead123\nMetallica1@\nJames\nHetfield\n0\n0\n0'
    monkeypatch.setattr('sys.stdin', io.StringIO(input))
    assert menus.createAccountMenu() == 0

    input = 'Sweetypie\nSweetpie1@\nMary\nNoname\n0\n0\n0'
    monkeypatch.setattr('sys.stdin', io.StringIO(input))
    assert menus.createAccountMenu() == 0

    input = 'fakeperson\nFake1234@\nFake\nPerson\n0\n0\n0'
    monkeypatch.setattr('sys.stdin', io.StringIO(input))
    assert menus.createAccountMenu() == 0

    input = 'Noideas123\nNoideas1@\nLarry\nMason\n0\n0\n0'
    monkeypatch.setattr('sys.stdin', io.StringIO(input))
    assert menus.createAccountMenu() == 0

    print("Test to add 11th account(should print all accounts are full):")
    #should print that accounts are all full
    assert menus.createAccountMenu() == 0

    return

#test_maximum_num_accounts()    
#test_create_profile()
#test_formatCaps()