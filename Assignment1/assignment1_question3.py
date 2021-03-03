#variables
num_range = 25
fizz_multiplier = 3
buzz_multiplier = 5
# FizzBuzz execution
for x in range(0,num_range+1):
    print("{0:2}: ".format(x), end="")
    if x % fizz_multiplier ==0 and x!= 0:
        print("Fizz", end="")
    if x % buzz_multiplier ==0 and x!= 0:
        print("Buzz", end="")
    print()

