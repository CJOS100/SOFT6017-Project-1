from random import randint

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
    global accountNumbers
    global accountNames
    global accountBalances
    initDatabase()
    finished = 0
    while finished !=1:
        nameDone = 0
        while nameDone != 1:
            firstAndLastName = input("Please enter the first and last name: ")
            if len(firstAndLastName) == 0:
                print("Error! Your input is invalid, please try again.")
            else:
                nameDone = 1
        generateSuccess = 0
        while generateSuccess !=1:
            newAccountNumber = randint(00000, 99999)
            if newAccountNumber in accountNumbers:
                generateSuccess = 0
            else:
                generateSuccess = 1
        balanceDone = 0
        while balanceDone !=1:
            try:
                initialBalance = float(input("How much would you like to deposit into the account?: "))
                if initialBalance < 0:
                    print("Error, invalid amount, please try again")
                else:
                    accountNumbers.append(newAccountNumber)
                    accountNames.append(firstAndLastName)
                    accountBalances.append(initialBalance)
                    filename = "bank.txt"
                    output_file = open(filename, "a")
                    output_file.write(str(newAccountNumber)+ "\n")
                    output_file.write(str(initialBalance)+ "\n")
                    output_file.write(str(firstAndLastName)+ "\n")
                    output_file.close()
                    balanceDone = 1
            except:
                print("Error! Please enter a balance again. (You can have a balance of €0)")
        finished = 1
    mainMenu()

def closeAcc():
    global accountNumbers
    global accountNames
    global accountBalances
    finished = 0
    while finished !=1:
        closingNumber = int(input("Please enter the number of the account you would like to close: "))
        closingIndex = accountNumbers.index(closingNumber)
        print("Closing index:", closingIndex)
        del accountNumbers[closingIndex]
        del accountBalances[closingIndex]
        del accountNames[closingIndex]

        filename = "bank.txt"
        output_file = open(filename, "w")
        output_file.write(str(""))
        output_file.close()

        linesWritten = 0
        while linesWritten < len(accountNumbers):
            print(linesWritten, accountNumbers[linesWritten])
            filename = "bank.txt"
            output_file = open(filename, "a")
            output_file.write(str(accountNumbers[linesWritten])+ "\n")
            output_file.write(str(accountBalances[linesWritten])+ "\n")
            output_file.write(str(accountNames[linesWritten])+ "\n")
            linesWritten = linesWritten + 1
        output_file.close()
        finished = 1
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
    print("############### Exiting ################")
    print("########################################")
    exit()

def initDatabase():
    f = open('bank.txt', 'r')
    database = f.readlines()
    f.close()
    databaseClean = []
    for i in range(len(database)):
        databaseClean.append(database[i].strip('\n'))
    global accountNumbers
    global accountBalances
    global accountNames
    accountNumbers = databaseClean[0::3]
    for i in range(len(accountNumbers)):
        accountNumbers[i] = int(accountNumbers[i])
    accountBalances = databaseClean[1::3]
    for i in range(len(accountBalances)):
        accountBalances[i] = float(accountBalances[i])
    accountNames = databaseClean[2::3]
    print(accountNumbers) # For testing only, remove in final version
    print(accountBalances) # For testing only, remove in final version
    print(accountNames) # For testing only, remove in final version

mainMenu()
