# Purpose : writes a file with input for up to 5 names

file = open("teams.txt","w")

count = int(input("how many teams would you like to enter?  "))

#team_name = input("Please enter a team name:  ")

for n in range(count):
    if count !=0:
        team_name = input("Please enter a team name:  ") + "\n"
        file.write(team_name)
        count = count - 1

file.close()
