colours = ["red", "green", "blue"]
prime_numbers = [2, 3, 5, 7, 9, 11, 19]

print(colours[1])#access by index
for x in colours:#iterate over the list or enumerate over the list (iteration)
    print(x)

#every student has 2 grades available- midterm and final
#these grades must be grouped together
grades = [70,72,80,81,66,67]

grades_better =[[70,72],[80,81], [66,67]]
#above is two dimensional list
for s in grades_better:
    print(s)

#what if you want to see the avg for each student

for s in grades_better:
    grade_midterm = s[0]
    grade_final = s[1]
    average= ((grade_midterm+grade_final)/2)
    print(average)
#add names?
student_grades = [["Lisa", 70, 75], ["John", 83, 92], ["Amy", 82, 66]]
for sg in student_grades:
    print(sg)

for ss in student_grades:
    grade_midterm2 = ss[1]
    grade_final2 =ss[2]
    average2 = ((grade_midterm2+grade_final2)/2)
    print(ss[0]+ " has a grade of "+ str(average2))

my_grade_list = []

my_grade_list.append(77)
my_grade_list.append(89)
my_grade_list.append(88)

for x in my_grade_list:
    print(my_grade_list)
#why does it print 3 times?

item_list = []
item_count =0
while item_count != -1:
    item_count = int(input("Enter item count >"))
    if item_count >0:
        item_list.append(item_count)
print("The total items added are ", end="")
print(sum(item_list))