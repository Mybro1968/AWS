###function

def volume(number1,number2, number3):
    if number1<0 or number2<0 or number3<0:
        print("Invalid entry")
    else:
        volume=number1 * number2 * number3
        print("Volume = ", volume)
    
###  Main Body
            
width = float(input("enter width: "))
depth = float(input("enter depth: "))
height = float(input("enter height: "))

volume(width, depth, height)
