fruit=["apple", "banana", "cranberry"]
print(fruit)
print(fruit[1])

#add to list
fruit = {"apple","cranberry"}
print(fruit)
fruit.add("date")
print(fruit)
fruit.add("banana")
fruit.add("orange")
fruit.add("kiwi")
fruit.add("cherry")
print(fruit)

#add items and quantities
fruit = {}
fruit["apple"] = 21
fruit["banana"] = 20
fruit["cranberry"] = 1

print(fruit)
#print the quantity of an item
print(fruit["apple"])

if "apple" in fruit:
    print(fruit["apple"])
else:
    print("Not specified")
