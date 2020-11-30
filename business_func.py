# calling the file with the business account information

from accounts_def import account2


# Function that calls the transfer method in business

def transfer():
    print("\nYou are about to transfer money ------")

    phonenbr = int(input("\nPhone number: "))
    amount = int(input("Amount: "))

    test_amount = account2.b_transfer(amount, 0)

    if test_amount == 0:
        print("Insufficient balance")
        exit()

    print("\nYou are transferring", amount, "RWF to", phonenbr)

    password = int(input("\nEnter the password to confirm: "))

    result = account2.b_transfer(amount, password)

    if result != "":
        print("\nYou have successfully transferred money")
        print("Your new balance is: ", result, "RWF")
    else:
        print("Invalid Password")


# Function that calls the withdraw method in business

def withdraw():
    print("\nYou are about to withdraw money ------")

    amount = int(input("\nAmount: "))

    test_amount = account2.b_withdraw(amount, 0)

    if test_amount == 0:
        print("Insufficient balance")
        exit()

    print("\nYou are withdrawing", amount, "RWF")

    password = int(input("\nEnter the password to confirm: "))

    result = account2.b_withdraw(amount, password)

    if result != "":
        print("\nYou have successfully withdrawn money")
        print("Your new balance is: ", result, "RWF")
    else:
        print("Invalid Password")



