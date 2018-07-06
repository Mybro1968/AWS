# Name : 03Squares
# Author : Gary Christie
# Date : 03 July 18
# Purpose : times table

for i in range(1,101):
    square = i ** 2
    if square < 2000:
        print(i,"squared = ", square)
    else:
        break
