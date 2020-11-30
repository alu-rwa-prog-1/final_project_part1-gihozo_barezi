# Authors: Julien Barezi and Gihozo Landelin

# importing the accounts from accounts_def file

from accounts_def import account1
from accounts_def import account2

# importing the customer and business functions

import customer_func
import business_func


cont = "y"

# Welcoming message

print("\nWelcome to the Mobile Money service ---- Enjoy!!")

# starting a loop so that the user can be allowed to do more than one operation

while cont != "n":

    # Asking the user which account they have because there are two different types and each has its functions
    Username = input("\nYour name: ").lower()

    # If they choose one we call methods from customer
    if Username == account1.name:
        print("\nWelcome Christian ---- customer account")
        print("\nSelect the operation you want to make:")
        print("\n1: Deposit Money")
        print("2: Withdraw Money")
        print("3: Check Balance")
        print("4: Transfer Money")
        print("5: Buy Electricity or Airtime")
        print("6: Pay a Business")
        query = int(input("\nYour choice: "))

        if query == 1:
            account1.deposit()
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")
        elif query == 2:
            customer_func.withdraw()
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")

        elif query == 3:
            account1.enquiry()
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")

        elif query == 4:
            customer_func.transfer()
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")

        elif query == 5:
            account1.buy()
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")

        elif query == 6:
            customer_func.payment()
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")

        elif query == 7:
            account1.create_account()
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")

    # If they choose 2 we use methods from the business class

    elif Username == account2.name:
        print("\nWelcome Kenny ---- Business account")
        print("\nSelect the operation you want to make:")
        print("\n1: Deposit Money")
        print("2: Withdraw Money")
        print("3: Check Balance")
        print("4: Transfer Money")
        print("5: Buy Electricity or Airtime")
        query = int(input("\nYour choice: "))

        if query == 1:
            account2.deposit()
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")
        elif query == 2:
            business_func.withdraw()
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")

        elif query == 3:
            account2.enquiry()
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")

        elif query == 4:
            business_func.transfer()
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")
        elif query == 5:
            account2.buy()
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")

else:
    print("Sorry that account doesn't exist!")
    exit()
