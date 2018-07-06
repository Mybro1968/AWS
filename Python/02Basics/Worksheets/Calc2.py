###
# odd or even
###

number1 = float(input("Please enter a number:  "))

mod = number1 % 2

if mod > 0:
    print("You picked an odd number.")
else:
    print("You picked an even number.")

print(mod)

