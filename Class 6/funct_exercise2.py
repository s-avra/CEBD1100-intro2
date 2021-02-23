def div_by_three(n1):
    if n1 % 3 ==0:
        return "Divisible by three"
    return "not divisible by"
print(div_by_three(18))

#now make it flexible
def is_div_by(num,divisor):
    return num % divisor ==0
if is_div_by(9,3):
    print("the num is divisible by the divisor")
#avoid proactively a div zero error
