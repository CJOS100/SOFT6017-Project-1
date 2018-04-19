from random import randint
dbInit = 0

def mainMenu():
    global dbInit
    if dbInit == 0:
        initDatabase()
        dbInit = dbInit + 1
    finished = 0
    while finished !=1:
        print("*** Main Menu ***")
        print()
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
    print()
    global accountNumbers
    global accountNames
    global accountBalances
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

                    balanceDone = 1
            except:
                print("Error! Please enter a balance again. (You can have a balance of €0)")
        finished = 1
    mainMenu()

def closeAcc():
    print()
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
        finished = 1
    mainMenu()

def withdraw():
    global accountNumbers
    global accountNames
    global accountBalances
    finished = 0
    while finished !=1:
        withdrawNumber = int(input("Please enter the number of the account you would withdraw from: "))
        withdrawIndex = accountNumbers.index(withdrawNumber)
        withdrawAmount = float(input("Please enter the amount you would like to withdraw: €"))
        currentBalance = accountBalances[withdrawIndex]
        newBalance = currentBalance - withdrawAmount
        accountBalances[withdrawIndex] = newBalance
        print("New balance:", accountBalances[withdrawIndex])
        finished = 1
    mainMenu()

def deposit():
    global accountNumbers
    global accountNames
    global accountBalances
    finished = 0
    while finished !=1:
        depositNumber = int(input("Please enter the number of the account you would deposit to: "))
        depositIndex = accountNumbers.index(depositNumber)
        depositAmount = float(input("Please enter the amount you would like to desposit: €"))
        currentBalance = accountBalances[depositIndex]
        newBalance = currentBalance + depositAmount
        accountBalances[depositIndex] = newBalance
        print("New balance:", accountBalances[depositIndex])
        finished = 1
    mainMenu()

def genReport():
    print()
    print("Generating report.txt in current directory...")
    global accountNumbers
    global accountBalances
    global accountNames

    filename = "report.txt"
    output_file = open(filename, "w")
    output_file.write("Total Accounts Open:" + " " + str(len(accountNumbers)) + "\n")
    output_file.write("Total Money in Accounts:" + " €" + str(sum(accountBalances)) + "\n")
    output_file.close()

    mainMenu()

def exitProgram():
    print()
    print("########################################")
    print("############### Exiting ################")
    print("########################################")

    global accountNumbers
    global accountNames
    global accountBalances
    filename = "bank.txt"
    output_file = open(filename, "w")
    output_file.write(str(""))
    output_file.close()

    linesWritten = 0
    while linesWritten < len(accountNumbers):
        filename = "bank.txt"
        output_file = open(filename, "a")
        output_file.write(str(accountNumbers[linesWritten])+ "\n")
        output_file.write(str(accountBalances[linesWritten])+ "\n")
        output_file.write(str(accountNames[linesWritten])+ "\n")
        linesWritten = linesWritten + 1
    output_file.close()
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
