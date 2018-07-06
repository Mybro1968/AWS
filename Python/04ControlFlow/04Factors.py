# Name : 4.4factorial
# Author : Gary Christie
# Date : 03 July 18
# Purpose : Exercise to calculate factorial.
# example: 5! = 5x4x3x2x1 = 120

#input request for number
number1 = int(input("This application will provide the sum of the factors \nof a given number and output its sum. \n\nPlease enter a number:  "))

#set the factorial to 1
factorial = 1

# for i in the range of (number1(inputvalue),stop at 0, increment by -1(by default will add 1)
for i in range(number1,0,-1):
#itterate the factorial by i
    factorial=factorial * i
    
print("Factorial of ", number1, "=", factorial)
