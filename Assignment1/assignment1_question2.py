def is_an_int(num):
    try:
        num = int(num)
        return True
    except:
        return False
table_size = input("What size multiplication table would you like?")

print((7+int(int(table_size)/2))*" " + "Multiplication Table"+int(int(table_size)/2)*" ")
print()
table_int=int(table_size)
print(7*" ",end= "")
for a in range(1,table_int+1):
    print("{0:3}".format(a), end = "")
    print