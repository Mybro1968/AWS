# Program : 02FileRead
# Author  : Gary Christie
# Date    : 05 Jul 2016
# Purpose : Example to open and read file

file = open("filename.txt","r")

print("First line:")
print(file.readline())
file.seek(0)
print("First line again:")
print(file.readline())
print("Second line:")
print(file.readline())
file.seek(25,0)
print(file.readline())
print("fifth line:")
print("Rest of file:")
print(file.read())
print("Blank line:")
print(file.readline())

file.close()
