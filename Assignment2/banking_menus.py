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
    if int(checking_acct_creation) < 10:
        print("Minimum deposit of $10.00 required.")
        continue
    else:
        checkingaccount1= CheckingAccount(int(checking_acct_creation),0)
        print("Your checking account has been successfully created.")
        #service charge setup
        flat_fee = 5
        checkingaccount1.service_charges(flat_fee)
        withdraw_fee = int(str(checkingaccount1.withdraw_count))*0.1
        checkingaccount1.service_charges(withdraw_fee)
        break
print("\nPlease create a savings account.\nMinimum deposit is $25.00, annual interest rate is 3%.")
while True:
    savings_acct_creation = input("How much would you like to deposit? ")
    if is_an_int(savings_acct_creation) == False:
        print("Please enter an integer.")
        continue
    if int(savings_acct_creation) < 25:
        print("Minimum deposit of $25.00 required.")
        continue
    else:
        savingsacct1 = SavingsAccount(int(savings_acct_creation),0.03)
        #service charge setup
        svg_withdraw_num=int(savingsacct1.withdraw_count)
        if svg_withdraw_num > 4:
            savings_fee = (svg_withdraw_num-4)*1
        else:
            savings_fee= 0
        savingsacct1.service_charges(savings_fee)
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
            # Savings Deposit
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
                    break
                print("Thank you for banking with us today.\n")
                break
            # Savings Withdraw
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
                    break
                print("Thank you for banking with us today.\n")
                break
            #Savings Report
            if savings_choice[0] == "C":
                print()
                savingsacct1.doMonthlyReport()
                print("Thank you for banking with us today.\n")
                break
            #Back to Main
            if savings_choice[0] == "D":
                print()
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
            #Checking Deposit
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
                        checkingaccount1.deposit(deposit_size)
                    break
                print("Thank you for banking with us today.\n")
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
                        checkingaccount1.withdraw(withdraw_size)
                    break
                print("Thank you for banking with us today.\n")
                break
            #Checking Report
            if checking_choice[0] == "C":
                print()
                checkingaccount1.doMonthlyReport()
                print("Thank you for banking with us today.\n")
                break
            #Back to main
            if checking_choice[0] == "D":
                print()
                break
            else:
                print("Please enter one of the listed options.")
        continue

    if bank_choice[0] == "C":
        print("Goodbye!")
        break
    else:
        print("Please enter one of the listed options.\n")