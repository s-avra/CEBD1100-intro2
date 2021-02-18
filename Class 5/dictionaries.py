#dictionary
#get province name from province code
#Get Quebec from "QC"
#dictionary composed of {key, value}
provinces={"QC": "Quebec", "ON":"Ontario"}
print(provinces["QC"])
print(provinces.get("QC"))#doesn't error if key doesn't exist, prints"None"
provincename = provinces.get("XX")
if provincename!= None:
    print(provincename)
else:
    print("This province doesn't exist")
#or
provincename2=provinces.get("OX","Not found")
print(provincename2)
#add to the dictionary
provinces["BC"]="British Colombia"
print(provinces)
del(provinces["BC"])
print(provinces)
#how to iterate each item?
for x in provinces:
    print(x)
    #nope, incorrect
for x in provinces.items():
    print(x)#see how it prints the tupples, it knows they are grouped
    print(x[0] +" is "+ x[1])
    #items returns tupple
#or
for x, y in provinces.items():
    print(x + " is " +y)
#print just values
for z in provinces.values():
    print(z)

#if you print it straight?get a list
print(provinces.values())