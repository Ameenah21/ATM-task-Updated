from datetime import datetime
import random
database = {}
def init():
    print ("Welcome to BankStarrr")
    print ("Do you have an account with us?")
    Reply = input("Enter 1 for Yes and 2 for No\n")
    
    try:

        if int(Reply) == 1:
            login()
        elif int(Reply) == 2:
            register()
        else:
            print("You have entered an invalid option")

    except ValueError:
        print("You have selected a wrong option")


def login():
    print("Please enter your account details to continue")
    account_number_from_user = int(input("Enter your account number\n"))
    password = input ("Enter your password\n")
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    for account_number, userDetails in database.items():
            if account_number == int(account_number_from_user):
                if (userDetails[3] == password):
                    print("You have logged in at %s" %current_time)
                    BankOperations(userDetails)

def register():

    print("*****Enter your details below to create an account\n")
    email = input("Enter your email address\n")
    first_name = input("Enter your first name\n")
    last_name = input("Enter your last name\n")
    password =input ("Please create a password\n")

    try:

        account_number = generate_account_number()

    except:
        print("Account Number cannot be generated at this time, please try again")
        init()

    database[account_number] = [ first_name, last_name, email, password, 0 ]

    print("Your account has been successfully created")
    print("*** **** **** ****")
    print("Your account number is: %d" %account_number)
    print("Keep your Account Number Secure")
    print("**** ***** **** ****")
    login()

def generate_account_number():
    return(random.randrange(1111111111,9999999999))

def BankOperations(user):
    print("Welcome %s %s " % (user[0], user[1]))
    selectedOption = input("What would you like to do? (1) Deposit (2) Withdrawal (3) Logout (4) Exit\n")
    try:
        if int(selectedOption == 1) :
            depositOperation()
        elif int(selectedOption == 2) :
            withdrawalOperation()
        elif int(selectedOption == 3) :
            login()
        elif int(selectedOption == 4) :
            exit()
        else:
            print("You have selected an invalid option")
            BankOperations(user)
    except ValueError:
        print("You have selected a wrong option")

def withdrawalOperation():
    print("Withdrawal")

def depositOperation():
    print("Deposit Operations")


init() 