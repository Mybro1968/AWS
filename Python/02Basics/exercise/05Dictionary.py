# Name : 05Dictionary
# Author : Gary Christie
# Date : 03 July 18
# Purpose : Example of dictionary

name = {}
name["Jack"]=23
name["James"]=17
name["Joe"]=19
name["John"]=20
name["Alex"]=22
print(name)
print(name["John"])

if "John" in name:
    print(name["John"])
else:
    print("not in name")
