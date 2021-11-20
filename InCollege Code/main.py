from menus import *
from OutputApis import *
from input_APIs import *

while True:
    # Creates a database for the profiles if one doesnt exist
    create_tables()

    # run API
    readAccountsFile()
    readJobsFile()
    readTrainingFile()
    RunallOutputAPIS()

    # run Home Menu
    homeMenu()