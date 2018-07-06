# Name : 01WorksheetNameAge
# Author : Gary Christie
# Date : 05 July 18
# Purpose : Exercise to calculate when a person will turn 100.

name = input("Please enter your name: ")
age = int(input("Please enter your current age: "))
year = 2018

century = 100 - age

century_year = year + century

loop = int(input("Please enter a number: "))

for i in range(0, loop):
    print("Greetings, ", name, "You will be 100 years old in ", century_year)


          
