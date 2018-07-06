##4.8 exam average

def average(number1,number2, number3):
    if number1 <0 or number1 >100:
        print(number1, " Invalid Mark entered for first exam")
    elif number2 <0 or number2 >100:
        print(number2, " Invalid Mark entered for second exam")
    elif number3 <0 or number3 >100:
        print(number2, " Invalid Mark entered for third exam")
    else:
        average_mark=(number1 + number2 + number3)/3
        if average_mark>=65:
            print(average_mark, "PASS")
        else:
            print(average_mark, "FAIL YOU THICK FUCK!!!!!")

maths_mark = int(input("enter mathhs exam 1 result "))
english_mark = int(input("enter english exam 2 result "))
ICT_mark = int(input("enter ICT exam 3 result "))

average(maths_mark, english_mark, ICT_mark)
