#ask a user to enter their name
#tell the user if their name is more than 5 letters
x= 5
if x==5:
    print("the number is 5")
else:
    print("not a 5")

user_name = input("what is your name>>>")
if len(user_name)<=5:
    print("Your name has five letters or less")
else:
    print("your name is longer than 5 letters")

name = input("What is another name?").strip()
if len(name)>6:
    print("Name is longer than 6 characters")
    if len(name)<10:
        print("But it's less than 10 characters")
    elif len(name)>=10:
        print("And it's 10 or greater")
elif len(name)== 6:
    print("Name is  exactly 6 characters long")
else:
    print("Name is not longer then 6 characters, please try again")
    print("please try again")