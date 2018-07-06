###  whileValue

investment = int(input("please enter investment:  "))
year = int(input("please enter the year of investment:  "))


while investment < 1000:
    year = year + 1
    investment = investment * 1.075
    print("year ", year, "value ", investment)


#int(input("please enter investment:  ")
