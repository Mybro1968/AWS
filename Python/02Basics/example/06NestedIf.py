# Name : 06NestedIf
# Author : Gary Christie
# Date : 03 July 18
# Purpose : Example of if menu

print("Menu:")
print("3 - Level 3")
print("4 - Level 4")

examlevel = int(input("Enter exam level: "))
if examlevel == 3:
    mark = int(input("Enter level 3 mark: "))
    if mark > 65:
        print("Pass")
    else:
        print("Fail")
elif examlevel == 4:
    mark = int(input("Enter level 4 mark: "))
    if mark > 50:
        print("Pass")
    else:
        print("Fail")
else:
    print("Invalid Level")
