# main menu
print("Welcome!")
while True:
    main_menu = "Please select an option below:\n1 - Draw a Triangle\nQ - Quit"
    print(main_menu)
    main_choice = input("Which option would you like? ").strip().upper()
    if main_choice != "1" and "Q":
        print("Sorry!\nThat option is not available, please enter one of the listed options.")
    if main_choice == "1":
        print("Good choice!")
        # menu 2
        while True:
            menu2 = "What kind of triangle would you like to draw?\n1 - Right sided triangle\n2 - Isosceles triangle\nQ - Back to main menu"
            print(menu2)
            menu2_choice = input("Which option would you like? ").upper()
            if menu2_choice == "Q":
                break
            if menu2_choice == "1":
                print("What size would you like your right sided triangle?")
                break
            if menu2_choice == "2":
                print("What size would you like your isosceles triangle?")
                break
            else:
                print("Sorry!\nThat option is not available, please enter one of the listed options.")
    if main_choice == "Q":
        print("Goodbye!")
        break
