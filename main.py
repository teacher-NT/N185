import os
os.system("cls")

car = {
    "brand": "BYD",
    "model": "Song Plus",
    "narxi": 21000,
    "rang": "qora",
    "yil": 2024
}

# print(car['bran'])
# print(car.get("bran", "Bunday kalit yo'q"))

# k = list(car.keys())
# print(k[0])

# v = list(car.values())
# print(v)

# car.pop('yil')
# print(car)

# items = list(car.items())
# print(items)
# for  k, v in car.items():
#     print(k, v)

# t = car.popitem()
# print(car)
# print(t)


# car["brand"] = "BMW"
# car['model'] = "M5"
# car["rang"] = "Moviy"
# car["yil"] = 2023
car.update({"brand":"BMW", "model":"M5", "rang":"Moviy", "yil":2023, 'probeg':5000})
print(car)














# print(car)

# car["probeg"] = 1500
# car['rang'] = "Ko'k"
# print(car["model"], car["narxi"], car['probeg'], car['rang'])

# if "rang" in car:
#     print("Yes!")
# else:
#     print("No!")

# for i in car:
#     print(i, car[i])

