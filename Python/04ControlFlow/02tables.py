timestable = int(input("Please enter the number of the times table you want to see: "))
rangevalue = int(input("what value would you like to go up to?  "))
for i in range(rangevalue + 1):
    print(timestable, " x",i,"=",timestable * i,)

