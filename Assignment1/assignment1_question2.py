def is_an_int(num):
    try:
        num = int(num)
        return True
    except:
        return False
table_size = input("What size multiplication table would you like?")

print((int((int(table_size)+4)/2))*" " + "Multiplication Table"+int((int(table_size)+4)/2)*" ")
table_int=int(table_size)
print((4)*" ",end= "")
for a in range(1,table_int+1):
    print("{0:2}  ".format(a), end="")
print("\n"+"_"*(4+(table_int*4)), end="")
for b in range(1, table_int+1):
    print("\n")
    print(str(b) + " |  ", end="")
    for c in range(1,table_int+1):
        print("{0:4}".format(str(b*c)), end="")