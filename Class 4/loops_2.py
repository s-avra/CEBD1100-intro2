for a in range(10):
    print (a, end="")

for b in ("apple", "pear", "orange"):
    print(b)

for a in range(2,9):
    if a < 5:
        print (str(a) + " less than 5")
    else:
        print("more than 5")
# for a in range(10):
#     if a <= 5:
#         print("X")
# how to do the above with continue
for a in range(10):
    if a>5:
        continue
    print(a)

name = "hello"
print(name[0])
for l in name:
    print(l.upper(), end = "") #"l" just stores current letter in loop
print() #this print is to start next print on new line
print(range(5,10))
print(list(range(5,10)))#casting to a list

list_start =1
list_end= 100
for n in range(list_start, list_end +1):
    if n% 2==0:
        print(str(n) + "; ", end = "")
print()

for y in range(1,100,10):
    print(y, end = ", ")


