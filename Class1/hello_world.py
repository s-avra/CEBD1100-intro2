my_name = "Sara"
a_number = 42



print("Hello " + my_name)
print(2+3)
print(1.01+1.02)

#print("My name is " + my_name + "and the number is " + a_number)
## cannot mix strings and numbers, can't concatenate integer
#need to do conversion

#Conversion 1=> number to string (add quotes) or  str()
#Conversion 2=> a string to number  int()

print("my name is " + my_name + "and the number is " + str(a_number))

# single equals sign is assignment
#double equal is comparison can even compare strings
print(5==5)
print("B"> "A")