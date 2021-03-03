#from ... import, or import..as
from functiondemo.basicmath import *
# star means all (wildcard)
print("Adding Demo")
n1=int(input("Please enter number one. "))
n2=int(input("Please enter number two. "))
print("the sum is " + str(add(n1, n2)))
#with from you're importing things directly
#with import functiondemo.basicmath as my_func its putting it in this file
# second preferable because it minimizes chances of two functions colliding
# makes it okay to have duplicate names

