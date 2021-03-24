from babel.numbers import format_currency
from Assignment2.account_types.savings_acct import SavingsAccount
from Assignment2.account_types.checking_acct import CheckingAccount

def is_an_int(n):
    try:
        n= int(n)
        return True
    except:
        return False
print("Welcome.\n")
print("Please create a checking account.\nMinimum deposit is $10.00")
while True:
    checking_acct_creation = input("How much would you like to deposit? ")
    if is_an_int(checking_acct_creation) == False:
        print("Please enter an integer.")
        continue
    if int(checking_acct_creation) <= 10:
        print("Minimum deposit of $10.00 required.")
        continue
    else:
        checkingaccount1= CheckingAccount(int(checking_acct_creation),0)
        print("Your checking account has been successfully created.")
        break
print("\nPlease create a savings account.\nMinimum deposit is $25.00, annual interest rate is 3%.")
while True:
    savings_acct_creation = input("How much would you like to deposit? ")
    if is_an_int(savings_acct_creation) == False:
        print("Please enter an integer.")
        continue
    if int(savings_acct_creation) <= 25:
        print("Minimum deposit of $25.00 required.")
        continue
    else:
        savingsacct1 = SavingsAccount(int(savings_acct_creation),0.03)
        print("Your savings account has been successfully created.")
        break
print()
while True:
    bank_menu = "Bank Menu:\nA: Savings\nB: Checking\nC: Exit"
    print(bank_menu)
    bank_choice = input("Which option would you like? ").upper().strip()
    if bank_choice[0] == "A":
         # Savings Menu
        while True:
            savings_menu = "Savings Menu\nA: Deposit\nB: Withrawal\nC: Report\nD: Return to Bank Menu"
            print(savings_menu)
            savings_choice = input("Which option would you like? ").upper().strip()
            # Deposit
            if savings_choice[0] == "A":
                while True:
                    deposit_prompt = input("\nHow much would you like to deposit? ")
                    if is_an_int(deposit_prompt) == False:
                        print("Please enter an integer.")
                        continue
                    deposit_size=int(deposit_prompt)
                    if deposit_size <= 0:
                        print("Please enter a postitive, non-zero integer.")
                        continue
                    else:
                        savingsacct1.deposit(deposit_size)
                        print(format_currency(deposit_size,'USD',locale = 'en_US') + " was deposited successfully.")
                    break
                print("Thank you for banking with us today.\n")
                break
            # Withdraw
            if savings_choice[0] == "B":
                while True:
                    withdraw_prompt=input("\nHow much would you like to withdraw? ")
                    if is_an_int(withdraw_prompt) == False:
                        print("Please enter an integer.")
                        continue
                    withdraw_size=int(withdraw_prompt)
                    if withdraw_size <=0:
                        print("Please enter a positive, non-zero integer.")
                        continue
                    else:
                        savingsacct1.withdraw(withdraw_size)
                        print(format_currency(withdraw_size,'USD', locale= 'en_US')+" was successfully withdrawn")
                    break
                print("Thank you for banking with us today.\n")
                break
            if savings_choice[0] == "C":
                print(savingsacct1.doMonthlyReport())
                break
            if savings_choice[0] == "D":
                break
            else:
                print("Please enter one of the listed options.")
        continue
    elif bank_choice[0] == "B":
        # Checking Menu
        while True:
            checking_menu = "Savings Menu\nA: Deposit\nB: Withrawal\nC: Report\nD: Return to Bank Menu"
            print(checking_menu)
            checking_choice = input("Which option would you like? ").upper().strip()
            # Deposit
            if checking_choice[0] == "A":
                while True:
                    deposit_prompt = input("\nHow much would you like to deposit? ")
                    if is_an_int(deposit_prompt) == False:
                        print("Please enter an integer.")
                        continue
                    deposit_size = int(deposit_prompt)
                    if deposit_size <= 0:
                        print("Please enter a postitive, non-zero integer.")
                        continue
                    else:
                        print("X was deposited successfully.")
                    break
                print("Thank you for banking with us today. ")
                break
            # Withdraw
            if checking_choice[0] == "B":
                while True:
                    withdraw_prompt = input("\nHow much would you like to withdraw? ")
                    if is_an_int(withdraw_prompt) == False:
                        print("Please enter an integer.")
                        continue
                    withdraw_size = int(withdraw_prompt)
                    if withdraw_size <= 0:
                        print("Please enter a positive, non-zero integer.")
                        continue
                    else:
                        print("X successfully withdrawn")
                    break
                print("Thank you for banking with us today. ")
                break
            if checking_choice[0] == "C":
                print("Report")
                break
            if checking_choice[0] == "D":
                break
            else:
                print("Please enter one of the listed options.")
        continue

    if bank_choice[0] == "C":
        print("Goodbye!")
        break
    else:
        print("Please enter one of the listed options.\n")