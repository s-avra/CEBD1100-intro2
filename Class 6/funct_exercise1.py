#my attempt
def get_max(n1,n2,n3):
    return max(n1,n2,n3)
print("The max of the three numbers is " + str(get_max(3,6,7)))

#other student answers s
def get_max1(val1, val2, val3):#would call it get max, print might not be wanted
    if val1>val2:
        maxi =val1
    elif val2>val3:
        maxi = val2
    else:
        maxi = val3
    return maxi
print(get_max1(8,3,2))

def get_max2(n1, n2, n3):
    max_num =0
    num_list = [n1,n2,n3]
    for i in num_list:
        if i< max_num:
            max_num= i
    return max_num
print(get_max2(3,5,9))
#this doesn't make sense

#prof answer
def get_max3(n1, n2, n3):
    if n1> n2 and n1>n3:
        return n1
    if n2>n3:
        return n2
    return n3
print(get_max3(2,6,9))
