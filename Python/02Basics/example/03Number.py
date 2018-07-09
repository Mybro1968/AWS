from decimal import *
number1 = int(input("What is the number to be divided?  "))
number2 = int(input("What is the number to divided by?  "))

print(number1, " / ", number2, " = ", int(number1 / number2))
print(number1, " / ", number2, " = ", float(number1 / number2))
print(number1, " / ", number2, " = ", Decimal(number1 / number2))
