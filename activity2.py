string = str(input("enter a random word"))
string2 = ("")
for i in string:
    string2 = i + string2
print("\nthe orignal string is ", string)
print("\nthe reversed string is ", string2)