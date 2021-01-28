my_text1 = "This is a \\quote \" symbol"
my_text2 = '\fthis is a quote \t " sym\nbol'
my_text3 = "x"
print(my_text1)
print(my_text2)

print(my_text3 * 10)


line_length = input( "How long would you like your line?")

print("_"* int(line_length))

line_length2 = input( "How many characters would you like?")
character = input(" what character should I use")
print(character * int(line_length2))