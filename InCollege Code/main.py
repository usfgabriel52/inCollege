from menus import *
from OutputApis import *
from input_APIs import *

while True:
    # Creates a database for the profiles if one doesnt exist
    create_tables()

    # run input API
    readTrainingFile()
    readJobsFile()
    readAccountsFile()

    # run output API
    RunallOutputAPIS()

    # run Home Menu
    homeMenu()