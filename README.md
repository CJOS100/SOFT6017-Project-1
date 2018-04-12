# Modular Programming Project #1

Name: Cathal O'Sullivan  
No: R00161981

## Specifications

Data for a bank is kept in a file called bank.txt.  
The file stores bank records and each bank record consists of  
•	 a bank account number  
•	 a balance in the account  
•	 a name  

A snippet of the file might be:  
98768  
8077.00  
Jim McIntyre  
58697  
23233.99  
Michael Murphy  
35318  
4545.12  
Abigail Buckley  
20454  
23233.45  
Marie Delaney  
Or if you prefer the data on one line might be  
98768 8077.00 Jim McIntyre  
58697 23233.99 Michael Murphy  
35318 4545.12 Abigail Buckley  
20454 23233.45 Marie Delaney  
Develop an application that allows the user to choose from one of the following options, until they choose to quit.  
1. Open an account
2. Close an account
3. Withdraw money
4. Deposit money
5. Generate a report for management
6. Quit

## Details

1. When opening an account a new account number must be created. It is a random 6 digit
number which is not already used as a bank account number.
2. Search for a bank account by its number and delete all data associated with that bank account.
3. Search for a bank account by its number and withdraw a user-specified amount of money if
there are sufficient funds.
4. Search for a bank account by its number and deposit a user-specified amount of money.
5. Print the following details:
a. Details of all accounts
b. Total amount on deposit in the bank
c. Largest amount on deposit specifying the account holder(s)
6. Quit and write the data from the list(s) back to bank.txt


## Built With

* [Python](http://www.dropwizard.io/1.0.2/docs/) - The code framework used
* [Git](https://maven.apache.org/) - Versioning management
* [Atom](https://rometools.github.io/rome/) - IDE

## Authors

* **Cathal O'Sullivan** - *Student*
