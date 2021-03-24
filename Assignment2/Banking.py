print("Welcome.")
def is_an_int(n):
    try:
        n= int(n)
        return True
    except:
        return False
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
                        print("X was deposited successfully.")
                    break
                print("Thank you for banking with us today. ")
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
                        print("X successfully withdrawn")
                    break
                print("Thank you for banking with us today. ")
                break
            if savings_choice[0] == "C":
                print("Report")
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
            print(savings_menu)
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
            if savings_choice[0] == "B":
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
            if savings_choice[0] == "C":
                print("Report")
                break
            if savings_choice[0] == "D":
                break
            else:
                print("Please enter one of the listed options.")
        continue

    if bank_choice[0] == "C":
        print("Goodbye!")
        break
    else:
        print("Please enter one of the listed options.\n")