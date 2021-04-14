"""This is a banking app with capacity to do authorisation for users.

METHODS:
Init: Initializes the application
Register: Enables new users open an account
Login: Enables account holders access an account
Bank Operation: Enables account holders carry out operation on account
Deposit Operation: Enables account holders make deposits
Withdrawal Operation: Enables account holders withdraw account
Termination Operation: Enables users continue using, or terminate use of app
Account Number Generator: Generates account number for new users
"""

import random
import datetime

now = datetime.datetime.now()
accountHolders = {}


def init():
    print ("Current date and time : ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
    print('Welcome to Tetuk Bank')

    isChoiceValid = False

    while isChoiceValid == False:
        print('Do you have an account with us? \n 1. Yes \n 2. No')
        choice = int(input('Please choose an option: '))
        if(choice == 1):
            isChoiceValid = True
            login()

        elif(choice == 2):
            isChoiceValuid = True
            register()

        else:
            print('Invalid option selected \n')

def login():
    print('*****Login to your account*****\n')

    isLoginSuccessful = False

    while isLoginSuccessful == False:
        userAccountNumber = int(input('Enter your account number: '))
        userPassword = input('Enter your password: ')

        for accountNumber, userDetails in accountHolders.items():
            if (userAccountNumber == accountNumber and userPassword == userDetails[3]):
                isLoginSuccessful = True
            else:
                print('Invalid account number or password\n')

    bankOperation(userDetails)

def register():
    print('******** Register an account ********\n')
    first_name = input('Please enter your first name: ')
    last_name = input('Please enter your last name: ')
    email = input('Please enter your email address: ')

    isPasswordMatch = False

    while isPasswordMatch == False:
        password = input('Please create a password: ')
        repeatPassword = input('Please re-enter your password: ')

        if(password == repeatPassword):
            isPasswordMatch = True
            accountNumber = accountNumberGenerator()
            accountHolders[accountNumber] = [first_name, last_name, email, password]

        else:
            print('\nYour passwords do not match, please try again')
    
    print(f'Congratulations! Your account number is {accountNumber}')
    print('Ensure that you keep it safe')

    login()

def bankOperation(userDetails):
    print(f'Welcome {userDetails[0]} {userDetails[1]}')
    print('\nWhat would you like to do?')
    print('1. Withdraw')
    print('2. Deposit')
    print('3. Logout')
    print('4. Exit')

    selectedOption = int(input('\nPlease select an option \n'))

    if (selectedOption == 1):
        withdrawalOperation()

    elif (selectedOption == 2):
        depositOperation()

    elif (selectedOption == 3):
        login()

    elif (selectedOption == 4):
        exit()

    else:
        print('Invalid option selected, please try again')
        bankOperation()

def accountNumberGenerator():
    print('Please wait, your account number is being generated \n')
    return random.randrange(111111111, 999999999)

def depositOperation():
    amount = input('Please enter amount to deposit \n')
    print(f'Your balance has been credited with {amount}, thank you')
    terminationOperation()

def withdrawalOperation():
    amount = input('Please enter amount to withdraw \n')
    print(f'Your balance has been debited by {amount}, thank you \n')
    terminationOperation()

def terminationOperation():
    print('Would you like to perform another transaction? \n(1) Yes (2) No')
    selectedOption = int(input('Please select an option: '))

    isSelectedOptionValid = False
    while isSelectedOptionValid == False:
        if (selectedOption == 1):
            isSelectedOptionValid = True
            login()

        elif (selectedOption == 2):
            isSelectedOptionValid = True
            exit()

        else:
            print('Invalid option, please try again')
            terminationOperation()

#Beginning of application
init()