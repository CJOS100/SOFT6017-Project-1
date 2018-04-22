from random import randint # random module needed to generate random account number
dbInit = 0 # This is here so we only initialise the database on first run

def mainMenu(): # Begin the main menu
    global dbInit # Let the module know that dbInit is a global module
    if dbInit == 0: # Have we initialised the database on first run? If not, do it, otherwise, skip it.
        initDatabase()
        dbInit = dbInit + 1
    finished = 0
    while finished !=1: # Have we finished with the main menu? No, then continue to show it.
        #try:
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
        #except Exception:
            #print("")
            #print("Error! Invalid input detected! Please try again!")
            #print("")

def openAcc(): # Begin function to open an account
    print("") # Blank line for formatting
    global accountNumbers # Declare that this is a global variable
    global accountNames # Declare that this is a global variable
    global accountBalances # Declare that this is a global variable
    finished = 0
    while finished !=1:
        try:
            nameDone = 0 # Are we done with the user entering their name? No, continue to ask them till they enter a valid name.
            while nameDone != 1:
                firstAndLastName = input("Please enter the first and last name: ")
                if len(firstAndLastName) == 0:
                    print("Error! Your input is invalid, please try again.")
                else:
                    nameDone = 1 # User entered a valid name? Yes, exit the loop.
        except Exception:
            print("")
            print("Error! Invalid input detected! Please try again!")
            print("")
        generateSuccess = 0 # Have we successfully generated an account number? No, continue to try generate one.
        while generateSuccess !=1:
            newAccountNumber = randint(000000, 999999) # sample code had 5 digit account numbers, but pdf said to use 6
            if newAccountNumber in accountNumbers: # Is the number we generated alreay in use? If yes, generate a new one, otherwise continue with it
                generateSuccess = 0
            elif len(accountNumbers) == 999999: # Are we out of random numbers? If yes, ask the user to remove one, otherwise continue
                print("Sorry, the database cannot hold anymore accounts.")
                print("Please remove one before attempting to continue again.")
                exitProgram()
            else:
                generateSuccess = 1
        balanceDone = 0
        while balanceDone !=1:
            try:
                initialBalance = float(input("How much would you like to deposit into the account?: €")) # Ask the user to enter a balance, validate to make sure it is a valid non negative number.
                if initialBalance < 0:
                    print("Error, invalid amount, please try again.") # If its invalid, ask them to try again
                else:
                    accountNumbers.append(newAccountNumber)
                    accountNames.append(firstAndLastName)
                    accountBalances.append(initialBalance)
                    print("") # For formatting and to allow the output to be easily read
                    print("Success, account number is:", newAccountNumber) # Tell the user their new account number
                    print("")
                    balanceDone = 1
            except:
                print("Error! Please enter a correct balance. (You can have a balance of €0)")
        finished = 1
    mainMenu()

def closeAcc(): # Begin close account module
    print("") # Formatting
    global accountNumbers # Declare that this is a global variable
    global accountNames # Declare that this is a global variable
    global accountBalances # Declare that this is a global variable
    finished = 0
    while finished !=1:
        try:
            closingNumber = int(input("Please enter the number of the account you would like to close: ")) # Keep asking the user for the account number to close until they enter a valid number.
            closingIndex = accountNumbers.index(closingNumber) # Find the index of the account to be closed
            del accountNumbers[closingIndex] # Remove the account number from the database
            del accountBalances[closingIndex] # Remove the account balance from the database
            del accountNames[closingIndex] # Remove the account name from the database
            finished = 1
        except Exception:
            print("")
            print("Error! Invalid input detected! Please try again.")
            print("")
    mainMenu()

def withdraw(): # Begin the withdraw module
    global accountNumbers # Declare that this is a global variable
    global accountNames # Declare that this is a global variable
    global accountBalances # Declare that this is a global variable
    finished = 0
    while finished !=1:
        try:
            numberGood = 0
            while numberGood == 0:
                withdrawNumber = int(input("Please enter the number of the account you would withdraw from: ")) # Keep asking the user for the account number to withdraw from until they enter a valid number.
                if withdrawNumber not in accountNumbers:
                    print("")
                    print("Error! You have entered an invalid account number! Please try again.")
                    print("")
                    numberGood = 0
                else:
                    numberGood = 1
            withdrawIndex = accountNumbers.index(withdrawNumber) # Find the index of the account they would like to withdraw from
            balanceGood = 0
            while balanceGood != 1:
                withdrawAmount = float(input("Please enter the amount you would like to withdraw: €")) # Ask them for a valid amount to withdraw and validate it
                currentBalance = accountBalances[withdrawIndex] # Find the current balance
                newBalance = currentBalance - withdrawAmount # Update the current balance with the entered amount
                if newBalance < 0: # If they enter a negative error, repeat the loop
                    print("")
                    print("Error! You cannot withdraw more than what is currently in the account! Please try again.")
                    print("")
                    balanceGood = 0
                else:
                    balanceGood = 1 # If they enter a valid number, break the loop and update their balance
                    accountBalances[withdrawIndex] = newBalance
                    print("") # Formatting
                    print("Success! New balance:", accountBalances[withdrawIndex]) # Tell the user the new balance
                    print("") # Formatting
                    finished = 1
        except Exception:
            print("")
            print("Error! Invalid input detected! Please try again!")
            print("")
    mainMenu()

def deposit(): # Begin the deposit module
    global accountNumbers
    global accountNames
    global accountBalances
    finished = 0
    while finished !=1:
        try:
            numberGood = 0
            while numberGood == 0:
                depositNumber = int(input("Please enter the number of the account you would deposit to: ")) # Keep asking the user for an accunt number to deposit to until they enter a valid one
                if depositNumber not in accountNumbers:
                    print("")
                    print("Error! You have entered an invalid account number! Please try again.")
                    print("")
                    numberGood = 0
                else:
                    numberGood = 1
            depositIndex = 0 # Init the variable
            depositIndex = accountNumbers.index(depositNumber) # Update the variable with the account number's index
            amountGood = 0
            while amountGood == 0:
                depositAmount = float(input("Please enter the amount you would like to desposit: €")) # Validate the amount being deposited
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
        except Exception:
            print("")
            print("Error! Invalid input detected! Please try again!")
            print("")
    mainMenu()

def genReport(): # Begin the module to generate a report
    print("")
    print("Generating report.txt in current directory...") # Let the user know we are beining to generate the report
    global accountNumbers # Global variables once again
    global accountBalances # Global variables once again
    global accountNames # Global variables once again

    filename = "report.txt" # The name of the file we will be generating the report to
    output_file = open(filename, "w", encoding='utf-8') # Open the file in writing mode and set the enocding to utf-8
    output_file.write("Total Accounts Open:" + " " + str(len(accountNumbers)) + "\n")
    output_file.write("Total Money in Accounts:" + " €" + str(format(sum(accountBalances), ".2f")) + "\n" + "\n")
    maxVal = max(accountBalances) # Find the max amount of money in the database
    largestIndex = accountBalances.index(maxVal) # Find the index of the largest balance
    largest_name = "" # Init the variable
    count = 0 # Init the count variable
    largestIndexes = [] # Init the largestIndexes list
    if accountBalances.count(maxVal) > 1: # If the largest amount of money occurs more than once, do the following
        output_file.write("Largest amount on deposit: €" + str(accountBalances[largestIndex]) + "\n") # Write the largest amount
        for i in range(len(accountBalances)): # Iterate through the list, adding the indexes to a new list
            if accountBalances[i] == maxVal:
                largestIndexes.append(i)
        i = 0
        output_file.write("Owned by:" + "\n" + "Account Number | Customer Name" + "\n") # Formatting
        while i < len(largestIndexes): # While current number is less than the length of the new list with max indexes on it, do the following
                output_file.write(str(accountNumbers[i]) + "         | " + str(accountNames[i]) + "\n") # Formatting & account number and its associated name
                i = i + 1
    elif accountBalances.count(maxVal) == 1:
        output_file.write("Largest amount on deposit: €" + str(accountBalances[largestIndex]) + ", in account number:" + str(accountNumbers[largestIndex]) + ", owned by: " + str(accountNames[largestIndex]) + "\n")
    output_file.write("\n" + "Account Number  | Customer Name       | Account Balance" + "\n")
    linesWritten = 0
    while linesWritten < len(accountNumbers): # Formatting
        max_width = 20 # Max width of a column (can be adjusted)
        column_width = max_width - len(accountNames[linesWritten])
        output_file.write(str(accountNumbers[linesWritten]) + "          | " + str(accountNames[linesWritten]) + column_width*" " + "| €" + str(accountBalances[linesWritten]) + "\n")
        linesWritten = linesWritten + 1
    output_file.close()
    mainMenu()

def exitProgram(): # Begin the function to exit the program, and write to file all changes
    print("") # Formatting
    global accountNumbers # Global variables once again
    global accountNames # Global variables once again
    global accountBalances # Global variables once again
    filename = "bank.txt" # The file we will be writing to
    output_file = open(filename, "w") # Open in writing mode
    output_file.write(str("")) # Wipe the file
    output_file.close() # Close the file

    linesWritten = 0
    while linesWritten < len(accountNumbers): # Start wrting the database back
        filename = "bank.txt" # File we are writing to
        output_file = open(filename, "a") # Open the file in append mode
        output_file.write(str(accountNumbers[linesWritten])+ "\n") # Write an account number
        output_file.write(str(accountBalances[linesWritten])+ "\n") # Write an account balance
        output_file.write(str(accountNames[linesWritten])+ "\n") # Write an account name
        linesWritten = linesWritten + 1
    output_file.close()
    print("########################################")
    print("############### Exiting ################") # Tell the user we are exiting
    print("########################################")
    exit()

def initDatabase(): # Function to initialise the database
    f = open('bank.txt', 'r') # Open bank.txt in read only mode
    database = f.readlines() # Read all data from the bank.txt file
    f.close() # Close bank.txt
    databaseClean = [] # Init a new blank database that we will add the cleaned up database to
    for i in range(len(database)):
        databaseClean.append(database[i].strip('\n')) # Remove new line characters from the original database and add them to the clean database
    global accountNumbers # Global variables once again
    global accountBalances # Global variables once again
    global accountNames # Global variables once again
    accountNumbers = databaseClean[0::3] # Start from line 0, read to the end, every 3 lines
    for i in range(len(accountNumbers)):
        accountNumbers[i] = int(accountNumbers[i])
    accountBalances = databaseClean[1::3] # Start from line 1, read to the end, every 3 lines
    for i in range(len(accountBalances)):
        accountBalances[i] = float(accountBalances[i])
    accountNames = databaseClean[2::3] # Start from line 2, read to the end, every 3 lines

mainMenu()
