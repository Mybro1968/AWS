# Name : 01If
# Author : Gary Christie
# Date : 03 July 18
# Purpose : Example of if and elif

mark = int(input("enter mark:  "))

if mark>85:
    print("Distinction")
elif mark>75:
    print("Merit")
elif mark>65:
    print("Pass")
else:
    print("Fail")
