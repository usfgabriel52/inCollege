from jobs import *
from verify_acc import *
from training import *


# reads "studentAccounts.txt" and updates the database accordingly
def readAccountsFile():

    try:
        accountsFile = open('input files\\studentAccounts.txt').read()
    except FileNotFoundError:
        print("studentAccounts.txt does not exist.\n")
    else:
        entries = []

        for a in accountsFile.split('====='):
            entries.append(a)

        for entry in entries:

            line = 0

            for i in entry.split('\n'):
                if line == 0 and i != '':
                    temp = i.split(',')
                    username = temp[0]
                    first = temp[1]
                    last = temp[2]
                    line += 1
                elif line > 0 and i != '':
                    password = i

            if number_rows() < 10 and not unique_user(username):
                data_entry(username, password, first, last, 1, 1, 1, 'English', 'Standard')   # add the account into the database with default information

# reads "newJobs.txt" and updates the database accordingly
def readJobsFile():
    try:
        jobsFile = open('input files\\newJobs.txt').read()
    except FileNotFoundError:
        print("newJobs.txt does not exist.\n")
    else:
        entries = []

        for e in jobsFile.split('====='):  # split the file by the ===== delimiter
            entries.append(e)

        for entry in entries:

            if entry != '':
                information = []
                line = 0
                description = ''
                desc_index = 1

                # title, description (marked by a line that just contains &&&), poster name, employer name, location, salary
                for j in entry.split('\n'):

                    if j != '&&&&':
                        if j != '':
                            information.append(j)
                            line += 1
                    else:  # store the index of the last line related to the description
                        desc_index = line - 1

                title = information[0]
                for d in range(1, desc_index + 1):
                    description += information[d] + '\n'
                poster_first = information[desc_index + 1]
                poster_last = information[desc_index + 2]
                employer = information[desc_index + 3]
                location = information[desc_index + 4]
                salary = information[desc_index + 5]

                # check the database if there is less than 10 job entries and if the current title is unique
                if len(getAllJobTitles()) < 10 and len(getJobDetailsByTitle(title)) == 0:
                    job_data_entry(title, description, employer, location, salary, poster_first, poster_last)  # add the job entry to the database


# reads "newtraining.txt" and updates the database accordingly
def readTrainingFile():
    try:
        trainingFile = open('input files\\newtraining.txt').read()
    except FileNotFoundError:
        print("newtraining.txt does not exist.\n")
        if not findCourse("How to use In College learning"):
            addCourse("How to use In College learning")
        if not findCourse("Train the trainer"):
            addCourse("Train the trainer")
        if not findCourse("Gamification of Learning"):
            addCourse("Gamification of Learning")
        if not findCourse("Understanding the Architectural Design Process"):
            addCourse("Understanding the Architectural Design Process")
        if not findCourse("Project Management Simplified"):
            addCourse("Project Management Simplified")
    else:
        for entry in trainingFile.split("\n"):
            if not findCourse(entry):
                addCourse(entry)
