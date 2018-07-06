# Program : 03FileReadByLine
# Author  : John Merchant
# Date    : 06May2016
# Purpose : Example to open and read file by line


file = open("filename.txt","r")

print("First line:")
print(file.readline())
file.seek(0)
print("First line again")
print(file.readline())

file.close()
