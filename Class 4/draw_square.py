#ask user how big square should be, then draw square using "#"
#use 2 methods
#method 1 --> using nested loops
#method 2 --> using multiplication

question = input("What is the size of your square?")
a=0
while a <= int(question)-1:
    print("#"* int(question))#doing the int conv takes many times, convert earlier
    a = a+1

##prof response

size = int(input("what is the size of your square?"))
#Method 1
for x in range(0,size):
    for y in range (0, size):
        print("#", end = "")
    print ()

#Method 2
for x in range (0, size):
    print("%"* size)