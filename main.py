from random import randint
dbInit = 0

def mainMenu():
    global dbInit
    if dbInit == 0:
        initDatabase()
        dbInit = dbInit + 1
    finished = 0
    while finished !=1:
        try:
            print("*** Main Menu ***")
            print("")
            print("1) Open an account")
            print("2) Close an account")
            print("3) Withdraw money")
            print("4) Deposit money")
            print("5) Generate a report for management")
            print("6) Quit")
            print("")
            selection = int(input("Please choose an option from 1-6: "))
            if selection < 0 or selection > 6:
                print("")
                print("########################################")
                print("Error! Please choose and option from 1-6")
                print("########################################")
                print("")
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
        except Exception:
            print("")
            print("Error! Invalid input detected! Please try again!")
            print("")

def openAcc():
    print("")
    global accountNumbers
    global accountNames
    global accountBalances
    finished = 0
    while finished !=1:
        try:
            nameDone = 0
            while nameDone != 1:
                firstAndLastName = input("Please enter the first and last name: ")
                if len(firstAndLastName) == 0:
                    print("Error! Your input is invalid, please try again.")
                else:
                    nameDone = 1
            generateSuccess = 0
        except Exception:
            print("")
            print("Error! Invalid input detected! Please try again!")
            print("")
        while generateSuccess !=1:
            # sample code had 5 digit account numbers, but pdf said to use 6
            newAccountNumber = randint(000000, 999999)
            if newAccountNumber in accountNumbers:
                generateSuccess = 0
            else:
                generateSuccess = 1
        balanceDone = 0
        while balanceDone !=1:
            try:
                initialBalance = float(input("How much would you like to deposit into the account?: €"))
                if initialBalance < 0:
                    print("Error, invalid amount, please try again.")
                else:
                    accountNumbers.append(newAccountNumber)
                    accountNames.append(firstAndLastName)
                    accountBalances.append(initialBalance)

                    balanceDone = 1
            except:
                print("Error! Please enter a correct balance. (You can have a balance of €0)")
        finished = 1
    mainMenu()

def closeAcc():
    print("")
    global accountNumbers
    global accountNames
    global accountBalances
    finished = 0
    while finished !=1:
        try:
            closingNumber = int(input("Please enter the number of the account you would like to close: "))
            closingIndex = accountNumbers.index(closingNumber)
            print("Closing index:", closingIndex)
            del accountNumbers[closingIndex]
            del accountBalances[closingIndex]
            del accountNames[closingIndex]
            finished = 1
        except Exception:
            print("")
            print("Error! Invalid input detected! Please try again.")
            print("")
    mainMenu()

def withdraw():
    global accountNumbers
    global accountNames
    global accountBalances
    finished = 0
    while finished !=1:
        try:
            numberGood = 0
            while numberGood == 0:
                withdrawNumber = int(input("Please enter the number of the account you would withdraw from: "))
                if withdrawNumber not in accountNumbers:
                    print("")
                    print("Error! You have entered an invalid account number! Please try again.")
                    print("")
                    numberGood = 0
                else:
                    numberGood = 1
            withdrawIndex = accountNumbers.index(withdrawNumber)
            withdrawAmount = float(input("Please enter the amount you would like to withdraw: €"))
            currentBalance = accountBalances[withdrawIndex]
            newBalance = currentBalance - withdrawAmount
            balanceGood = 0
            while balanceGood != 1:
                if newBalance < 0:
                    print("")
                    print("Error! You cannot withdraw more than what is currently in the account! Please try again.")
                    print("")
                    balanceGood = 0
                    break
                else:
                    balanceGood = 1
                    accountBalances[withdrawIndex] = newBalance
                    print("New balance:", accountBalances[withdrawIndex])
                    finished = 1
        except Exception:
            print("")
            print("Error! Invalid input detected! Please try again!")
            print("")
    mainMenu()

def deposit():
    global accountNumbers
    global accountNames
    global accountBalances
    finished = 0
    while finished !=1:
        numberGood = 0
        while numberGood == 0:
            depositNumber = int(input("Please enter the number of the account you would deposit to: "))
            if depositNumber not in accountNumbers:
                print("")
                print("Error! You have entered an invalid account number! Please try again.")
                print("")
                numberGood = 0
            else:
                numberGood = 1
        depositIndex = 0
        depositIndex = accountNumbers.index(depositNumber)
        print(depositIndex)
        amountGood = 0
        while amountGood == 0:
            depositAmount = float(input("Please enter the amount you would like to desposit: €"))
            if depositAmount < 0:
                print("Error! You cannot deposit a negative amount of money! Please try again.")
                amountGood = 0
            else:
                amountGood = 1
        currentBalance = accountBalances[depositIndex]
        newBalance = currentBalance + depositAmount
        accountBalances[depositIndex] = newBalance
        print("")
        print("Success! New balance:", accountBalances[depositIndex])
        print("")
        finished = 1
        #except Exception:
            #print("")
            #print("Error! Invalid input detected! Please try again!")
            #print("")
    mainMenu()

def genReport():
    print("")
    print("Generating report.txt in current directory...")
    global accountNumbers
    global accountBalances
    global accountNames

    filename = "report.txt"
    output_file = open(filename, "w", encoding='utf-8')
    output_file.write("Total Accounts Open:" + " " + str(len(accountNumbers)) + "\n")
    output_file.write("Total Money in Accounts:" + " €" + str(sum(accountBalances)) + "\n")
    largestAmount = max(accountBalances)
    largestIndex = accountBalances.index(largestAmount)
    output_file.write("Largest amount on deposit: €" + str(accountBalances[largestIndex]) + ", in account number:" + str(accountNumbers[largestIndex]) + " owned by: " + str(accountNames[largestIndex]) + "\n")
    output_file.write("\n" + "Account Number  | Customer Name       | Account Balance" + "\n")
    output_file

    linesWritten = 0
    while linesWritten < len(accountNumbers):
        max_width = 20
        column_width = max_width - len(accountNames[linesWritten])
        output_file.write(str(accountNumbers[linesWritten]) + "          | " + str(accountNames[linesWritten]) + column_width*" " + "| €" + str(accountBalances[linesWritten]) + "\n")
        linesWritten = linesWritten + 1
    output_file.close()
    mainMenu()

def exitProgram():
    print("")

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

mainMenu()
