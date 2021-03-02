# main menu
goodbye_menu2 = "Thanks for drawing triangles! Goodbye."
print("Welcome!")
while True:
    main_menu = "Please select an option below:\n1 - Draw a Triangle\nQ - Quit"
    print(main_menu)
    main_choice = input("Which option would you like? ").upper()
    if main_choice == "1":
        print("\nGood choice!")
        # menu 2
        while True:
            menu2 = "\nChoose which triangle you would like to draw:\n1 - Right sided triangle\n2 - Isosceles triangle\nQ - Back to main menu"
            print(menu2)
            menu2_choice = input("Which option would you like? ").upper()
            if menu2_choice == "1":
                right_size = int(input("\nWhat size would you like your right sided triangle? "))
                for x in range(1, right_size+1):
                    print("#"*x)
                try_again =input("I hope you like your triangle! Press \"A\" if you would like to try again.\nPress anything else to go back to the main menu. ").upper().strip()
                if try_again == "A":
                    continue
                else:
                    print()
                    break
            if menu2_choice == "2":
                iso_size=int(input("\nWhat size would you like your isosceles triangle? "))
                for z in range(1,iso_size+1,2):
                    print(int(((iso_size-z)/2))*" ", end = "")
                    print(z*"#", end = "")
                    print(int(((iso_size - z) / 2)) * " ")
                break
            if menu2_choice == "Q":
                print()
                break
            else:
                print("Sorry!\nThat option is not available, please enter one of the listed options.")
        continue
    if main_choice == "Q":
        print("Goodbye!")
        break
    else:
        print("Sorry, try again")
