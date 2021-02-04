#ask the user for repeated integers, keep track of sum
#when user enters -1, print sum
sum_of_number = 0
result= 0
while result!= -1:
    result= int(input("what is your number?"))
    sum_of_number = sum_of_number+result
print(str(sum_of_number+1))

sum_of_ints = 0
entered_val = ""

while entered_val !=-1:
    entered_val = int(input("put in a number"))
    if entered_val != -1:
            sum_of_ints += entered_val
print(f"The sum of values is {sum_of_ints}")

multiple= ""
mod_ten = 0
while True:
    multiple = int(input ("give me a number").upper())
    if multiple != "Q":
        elif int(multiple)%10 ==0:
            print( "Your number is a multiple of 10")
        else:
            print("your number is not a multiple of 10")
