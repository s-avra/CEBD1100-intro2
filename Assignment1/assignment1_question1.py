# main menu
goodbye_menu2 = "Thanks for drawing triangles! Goodbye."
print("Welcome!")
def is_an_int(n):
    try:
        n= int(n)
        return True
    except:
        return False
while True:
    main_menu = "Select an option below:\n1 - Draw a Triangle\nQ - Quit"
    print(main_menu)
    main_choice = input("Which option would you like? ").upper()
    if main_choice == "1":
        print("\nGood choice!")
        # menu 2
        while True:
            menu2 = "\nChoose which triangle you would like to draw:\n1 - Right sided triangle\n2 - Isosceles triangle\nQ - Back to main menu"
            print(menu2)
            menu2_choice = input("Which option would you like? ").upper()
            # Right sided triangle
            if menu2_choice == "1":
                while True:
                    right_prompt = input("\nWhat size would you like your right sided triangle? ")
                    if is_an_int(right_prompt) == False:
                        print("Please enter an integer.")
                        continue
                    right_size=abs(int(right_prompt))
                    if right_size == 0:
                        print("Please enter a non-zero integer.")
                        continue
                    for x in range(1, right_size+1):
                        print("#"*x)
                    break
                try_again =input("I hope you like your triangle! Enter \"A\" if you would like to try again.\nEnter anything else to go back to the main menu. ").upper().strip()
                if try_again == "A":
                    continue
                else:
                    print()
                    break
            # Isosceles triangle
            if menu2_choice == "2":
                while True:
                    iso_prompt=input("\nWhat size would you like your isosceles triangle? ")
                    if is_an_int(iso_prompt) == False:
                        print("Please enter an odd integer.")
                        continue
                    iso_size=abs(int(iso_prompt))
                    if iso_size ==0:
                        print("Please enter a non-zero odd integer.")
                        continue
                    if iso_size%2 == 0:
                        print("Please enter an odd integer.")
                        continue
                    elif iso_size%2 ==1 and iso_size>0:
                        for z in range(1,iso_size+1,2):
                            print(int(((iso_size-z)/2))*" ", end = "")
                            print(z*"#", end = "")
                            print(int(((iso_size - z) / 2)) * " ")
                    break
                try_again = input("I hope you like your triangle! Enter \"A\" if you would like to try again.\nEnter anything else to go back to the main menu. ").upper().strip()
                if try_again == "A":
                    continue
                else:
                    print()
                    break
            if menu2_choice == "Q":
                print()
                break
            else:
                print("Please enter one of the listed options.")
        continue
    if main_choice == "Q":
        print("Goodbye!")
        break
    else:
        print("Please enter one of the listed options.\n")
