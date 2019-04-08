cars = ["Ford", "Chrystler", "Dodge", "Ram", "Jeep", "Chevy", "GMC"]
print(cars)

MyArrayLen = len(cars)
print(MyArrayLen)

cars.append("Buick")
print(cars[3])

cars.insert(2, "Toyota")
print(cars)

cars.pop(4)
print(cars)

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print"The length of the array is " , MyArrayLen
