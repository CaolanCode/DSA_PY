# integers are emutable
num1 = 11
num2 = num1

print("Before num2 is updated")
print("num1 = ", num1)
print("num2 = ", num2)

print("\nnum1 points to: ", id(num1))
print("\nnum2 points to: ", id(num2))

num2 = 22

print("After num2 is updated")
print("num1 = ", num1)
print("num2 = ", num2)

print("\nnum1 points to: ", id(num1))
print("\nnum2 points to: ", id(num2))

# dictionaries can be changed where they point to
# the unlinked memory will be taken care of with garbage collection
dict1 =  {'value' : 11}

dict2 = dict1

print("Before dict2 is updated")
print("dict1 = ", dict1)
print("dict2 = ", dict2)

print("\ndict1 points to: ", id(dict1))
print("\ndict2 points to: ", id(dict2))

dict2['value'] = 22

print("After dict2 is updated")
print("dict1 = ", dict1)
print("dict2 = ", dict2)

print("\ndict1 points to: ", id(dict1))
print("\ndict2 points to: ", id(dict2))