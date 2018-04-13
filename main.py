def mainMenu():
    initDatabase()
    finished = 0
    while finished !=1:
        print("Main Menu")
        print("1) Open an account")
        print("2) Close an account")
        print("3) Withdraw money")
        print("4) Deposit money")
        print("5) Generate a report for management")
        print("6) Quit")
        selection = int(input("Please choose an option from 1-6: "))
        if selection < 0 or selection > 6:
            print()
            print("########################################")
            print("Error! Please choose and option from 1-6")
            print("########################################")
            print()
        elif selection == 1:
            finished = 1
            openAcc()
        elif selection == 2:
            finished = 1
            closeAcc()
        elif selection == 3:
            finished = 1
            withdraw()
        elif selection == 4:
            finished = 1
            deposit()
        elif selection == 5:
            finished = 1
            genReport()
        elif selection == 6:
            finished = 1
            exitProgram()

def openAcc():
    print("Works")
    mainMenu()

def closeAcc():
    print("Works")
    mainMenu()

def withdraw():
    print("Works")
    mainMenu()

def deposit():
    print("Works")
    mainMenu()

def genReport():
    print("Works")
    mainMenu()

def exitProgram():
    print("########################################")
    print("Exiting")
    print("########################################")
    exit()

def initDatabase():
    f = open('bank.txt', 'r')
    database = f.readlines()
    f.close()
    databaseClean = []
    for i in range(len(database)):
        databaseClean.append(database[i].strip('\n'))
    accountNumbers = databaseClean[0::3]
    accountBalances = databaseClean[1::3]
    accountNames = databaseClean[2::3]
    print(accountNumbers) # For testing only, remove in final version
    print(accountBalances) # For testing only, remove in final version
    print(accountNames) # For testing only, remove in final version

mainMenu()
