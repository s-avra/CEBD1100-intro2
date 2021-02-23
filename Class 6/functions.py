def add_numbers(val1, val2):
    return val1+val2
num1=float(input("enter the 1st number"))
num2=float(input("enter the 2nd number"))
print("The sum of the numbers is " + str(add_numbers(num1, num2)))
print("The sum of the numbers is " + str(add_numbers("9","5")))

#can have multiple returns inside a function
def code_type(code):
    if len(code) == 7:
        return "Legacy code"

    if code[0:1] == "9":
        return "Current code"
    return"Invalid"
print(code_type("78765435"))
