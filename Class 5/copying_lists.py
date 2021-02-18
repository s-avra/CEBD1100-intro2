list1 = [2,3,4]
list2 = [value for value in list1]#wordy, not needed
print(list1)
print(list2)
list2[1]=6
print(list1)
print(list2)

#or
list3=list1.copy()#simpler
list3[2]=8
print(list3)