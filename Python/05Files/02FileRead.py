# Purpose : Creates a program that reads the first 2 names in a file then the rest

file = open("teams.txt","w")

count = int(input("how many teams would you like to enter?  "))

#team_name = input("Please enter a team name:  ")

for n in range(count):
    if count !=0:
        team_name = input("Please enter a team name:  ") + "\n"
        file.write(team_name)
        count = count - 1

file.close()
