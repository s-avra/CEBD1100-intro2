my_name = input("What is your name?")
my_number = input ("What is your number?")
print("The name is {}, and the number is {} ".format(my_name, my_number))

my_name2= "Sara"
my_number2 = 17

print("The name is \"{}\" and the number is \"{}\"".format(my_name2, my_number2))

print( "Gas prices is {1:2.4f}, and the cost per liter is :{0:8.2f}".format(123.55,123.546))

try_it = input("How can I make something shorter? ").upper().strip()
if try_it[0] == "Q":
    print("it worked")
else:
    print("it didn't")