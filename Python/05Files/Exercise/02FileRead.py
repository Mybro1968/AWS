# Purpose : Creates a program that reads the first 2 names in a file then the rest

file = open("teams.txt","r")

print("First line:")
print(file.readline())
print("Second line:")
print(file.readline())
print("Rest of file:")
print(file.read())
#print("Blank line:")
#print(file.readline())

file.close()
