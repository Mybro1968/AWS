### Ex4.7 - exam grades

def exam_grade(level, mark):
    if level <1 or level >4:
        print("invalid level")
    elif mark <0 or mark >100:
        print("invalid mark")
    elif level == 1 or level ==2:
        if mark>=85:
            print("distinction")
        elif mark>=75:
            print("merit")
        elif mark>=65:
            print("pass")
        else:
            print("fail")
    elif level == 3:
        if mark>=80:
            print("distinction")
        elif mark>=70:
            print("merit")
        elif mark>=60:
            print("pass")
        else:
            print("fail")
    elif level == 4:
        if mark>=70:
            print("distinction")
        elif mark>=60:
            print("merit")
        elif mark>=50:
            print("pass")
        else:
            print("fail")

####main program

level = int(input("please enter the exam level:  "))
mark = int(input("please enter the exam mark:  "))

##print("at level ", level, "and mark ", mark, "the exam grade is")

exam_grade(level, mark)
