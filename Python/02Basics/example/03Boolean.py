
number1 = float(input("please enter the first number   "))
number2 = float(input("Please enter the second number:   "))

if number1 > number2:
    number1bigger = True

else:
    number1bigger = False

print("Number1 bigger: ", number1bigger)

if number1bigger:
    print("Number 1 is bigger")
else:
    print("Number 1 not bigger")
