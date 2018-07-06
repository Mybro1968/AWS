# Program : 05FileEdit
# Author  : John Merchant
# Date    : 06May2016
# Purpose : Example to open and edit file


file = open("filename.txt","r")

outfile = ""
for line in range (10):
    if line % 2 == 0:
        outfile = outfile + file.readline()

    else:
        file.readline()

file = open("filename.txt", "w")
file.write(outfile)
file.close()
