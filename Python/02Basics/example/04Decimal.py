###
#Name : 04Decimal.py
#Author : Gary Christie
#Date : 03 Jul 2018
#Purpose : Example of decimal
###

from decimal import *
number1 = 1
number2 = 7
print(type(number1))
print(number1 / number2)

number1 = Decimal(1)
number2 = Decimal(7)
print(type(number1))
print(number1 / number2)
