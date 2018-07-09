# Purpose : Creates a program that reads the first 2 names in a file then the rest

#file = open("teams.txt","r")

#file.readline()
#file.readline()
#print("The contents of the 3rd Line:")
#print(file.readline())
#print("Blank line:")
#print(file.readline())

#file.close()

#User inputs entry number to list

file = open("teams.txt","r")

linenumber = int(input("Enter the outline line number:  "))

count = 1

###line count
for n in range(1,linenumber+1):
    count=count+1
    
###while loop   
while count > 1:
    file.readline()
    count = count - 1
if count < linenumber:
    print("line number ", linenumber, "reads ------>  ", file.readline())

file.close()

