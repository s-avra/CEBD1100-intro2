first = "Jane"
last = "Doe"
salary = 20080.45
symbol = "#"
repeat = 15

#print "Welcome "Jane Doe".  -> Welcome "Jane Doe".
print("Welcome, \"" + first +" "+ last + "\".")
print("Welcome, \"{0} {1}\".".format(first,last))

import decimal

#print "The salary is $20080.45".
print("The salary is " + "${:.2f}".format(salary))

#print "The symbol # repeated 15 times is : ###############"
print("The symbol # repeated 15 times is : "+symbol*repeat)

ultra_long = "supercalifragalistic"
print(len(ultra_long))
print(ultra_long.upper())
print(ultra_long.replace("sup","new"))
print(ultra_long[0:10])
print(ultra_long[-3])
print(ultra_long[-3:])
print(ultra_long[:-3])
