def describe_pet(pet_name= "spot", animal_type= "dog"):
    print("Pet name is "+ pet_name)
    print("Animal type is "+ animal_type)
describe_pet()
describe_pet("Jack")
describe_pet("Jack", "Cat")
#how to specify animal type
describe_pet(animal_type="fish")
#named parameter

def generate_namr(first:str, last: str ="Unknown"):#forced typing, makes it cleaner
    return first+last
print(generate_namr("sara","avramovic"))

def add_nums(num1=0, num2=0):
    return num1+num2
#equivalating number to default, the type of default is expected
#maybe you don't want an empty value, either one is fine

#how to make parameters flexible
def add_numbers (n1, n2, n3=0):
    return n1+n2+n3
def add_numbers2 (numbers: list):
    return sum(numbers)
print("Sum of numbers"+ str(add_numbers2([4, 7, 8, 12, 23])))
#need brackets because it's a list
