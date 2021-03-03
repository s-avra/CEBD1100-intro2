def is_an_int(num):
    try:
        num = int(num)
        return True
    except:
        return False

# exception capturing
while True:
    table_size = input("What size multiplication table would you like printed? ")
    if is_an_int(table_size) == False:
        print("Please enter an integer.")
    if is_an_int(table_size) == True:
        table_int=int(table_size)
        if table_int <= 0:
            print("Please enter a positive, non-zero integer.")
            continue
        elif len(str(table_int*table_int))>5:
            print("Sorry, that exceeds the size of the table. Please enter a smaller number.")
            continue
        # table output
        else:
            # title
            print((int(((table_int*6)+6)/2)-10)*" " + "Multiplication Table"+(int(((table_int*6)+6)/2)-9)*" ")
            #"multiplication table" has 19 letters
            # top row
            print((6)*" ",end= "")
            for a in range(1,table_int+1):
                print("{0:6}".format(str(a)), end="")
            # separating line
            print("\n"+"_"*6 +"_"*(table_int*6), end="")
            #remaining rows
            for b in range(1, table_int+1):
                print("\n")
                print("{0:3}".format(str(b)) + "|  ", end="")
                for c in range(1,table_int+1):
                    print("{0:6}".format(str(b*c)), end="")
            break
#can you make the size flexible?