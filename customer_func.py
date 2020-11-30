# calling the file with the customer account information

from accounts_def import account1


# Function that calls the transfer method in customer

def transfer():
    print("\nYou are about to transfer money ------")

    phonenbr = int(input("\nPhone number: "))
    amount = int(input("Amount: "))

    test_amount = account1.c_transfer(amount, 0)

    if test_amount == 0:
        print("Insufficient balance")
        exit()

    print("\nYou are transferring", amount, "RWF to", phonenbr)

    password = int(input("\nEnter the password to confirm: "))

    result = account1.c_transfer(amount, password)

    if result != "":
        print("\nYou have successfully transferred money")
        print("Your new balance is: ", result, "RWF")
    else:
        print("Invalid Password")


# Function that calls the withdraw method in customer

def withdraw():
    print("\nYou are about to withdraw money ------")

    amount = int(input("\nAmount: "))
    trans_fee = amount * 0.05

    test_amount = account1.c_withdraw(amount, 0)

    if test_amount == 0:
        print("Insufficient balance")
        exit()

    print("\nYou are withdrawing", amount, "RWF")
    print("The transaction fee is: ", trans_fee)

    password = int(input("\nEnter the password to confirm: "))

    result = account1.c_withdraw(amount, password)

    if result != "":
        print("\nYou have successfully withdrawn money")
        print("Your new balance is: ", result, "RWF")
    else:
        print("Invalid Password")


# Function that calls the payment method in customer

def payment():
    print("You are about to make a payment -----")

    payment_reason = input("\nReason for Payment: ")
    code = int(input("Code of the business: "))
    amount = int(input("Amount: "))

    test_amount = account1.c_withdraw(amount, 0)

    if test_amount == 0:
        print("\nInsufficient balance")
        exit()

    print("\nYou are paying", amount, "RWF to", code, "(Business code) for", payment_reason)

    password = int(input("\nEnter the password to confirm: "))

    result = account1.c_payment(amount, password)

    if result != "":
        print("\nYou have successfully paid for", payment_reason)
        print("Your new balance is: ", result, "RWF")
    else:
        print("Invalid Password")


