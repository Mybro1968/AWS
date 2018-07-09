number1 = float(input("Please enter the first number:  "))
number2 = float(input("please enter the second number:  "))                

print("Menu: ")
print("1 - Add")
print("2 - subtract")
print("3 - Multiply")
print("4 - Divide")
print("5 - Square")
print("6 - Power")

menu_option = int(input("Select Option:  "))

if menu_option == 1:
    print(number1," + ",number2," = ", number1 + number2)
elif menu_option == 2:
    print(number1, "-", number2, "=", number1 - number2)
elif menu_option == 3:
    print(number1,"*",number2,"=",number1 * number2)
elif menu_option == 4:
    print(number1,"/",number2,";=",number1 / number2)
elif menu_option == 5:
    print(number1,"squared =",number1 * number1)
    print(number2,"squared =",number2 * number2)
elif menu_option == 6:
    print(number1,";to power of",number2,"=",number1 ** number2)
else:
    print("invalid selection")
    
