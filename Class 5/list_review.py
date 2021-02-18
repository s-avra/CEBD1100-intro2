# create a list with numbers 0-9 in it
# display the list elements separated by a comma
#display all even elements of the list
#display the avg value of all elements in the list

list1= list(range(10))

for x in list1:
    print(str(x), end= ",")
print()# need this print to create new line
#exclude comma on nine?
for x in list1:
    print(str(x), end ="")
    if x< max(list1):
        print(",", end= "")
print()
del(list1[4])#only works because cast to list.
# Range on it's own doesn't know each individual component
for x in list1:
    print(str(x), end ="")
    if x< max(list1):
        print(",", end= "")
print()
#print evens
for x2 in list1:
    if x2%2==0:
        print(x2, end =",")
print()
#make an even list
even_list1 =list(range(0,10,2))
print(even_list1)
even_list2 =[]
for x2 in list1:
    if x2%2==0:
        even_list2.append(x2)
        print(even_list2, end =",")
print()
#print avg of values
print(sum(list1)/len(list1))
