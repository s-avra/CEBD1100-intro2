# x = 5/0
#ZeroDivisionError occurs

#raise Exception("The credit card requires 16 digits")

def divide_numbers(n1,n2):
    result = 0
    try:
        result = n1/n2
        return  result
    except:
        return False
print(divide_numbers(7,0))

#how to check if something is a float
def is_a_float(n):
    try:
        n=float(n)
        return True
    except:
        return False


print(is_a_float("Hi"))
print(is_a_float(7))

#prof answer
print(isinstance(7.1, float))