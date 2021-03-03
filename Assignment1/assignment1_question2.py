def is_an_int(num):
    try:
        num = int(num)
        return True
    except:
        return False
table_size = input("What size multiplication table would you like? ")
table_int=int(table_size)
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
#add "sorry that integer exceeds the table size, please try again with a smaller integer
# add in exception protection
#add in number shift for number row title?