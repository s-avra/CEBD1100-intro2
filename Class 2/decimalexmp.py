import decimal

a = decimal.Decimal("10.67")

b= decimal.Decimal(10.67)

#always feed deciml a string
#issue --> how can it verify that it is fed a correct amount?

print (a - 5)
print(b - 5)
