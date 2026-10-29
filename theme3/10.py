car = {
    "brand": "Toyota",
    "model": "Camry",
    "price": 20000.0,
    "colors": ["black", "white"],
    "peredachi": {1,2,3,4,5,6},
    "owner": {
        "name": "Alex",
        "phone_number": "+375292929299",
        'cities': ["Minsk", "Grodno"]
    },
    111: 222,
    22.11: 223
}

car["model"] = "RAV4"
car["year"] = 2024
#
# print(car["owner"]["cities"][1])
# car["owner"]["cities"][1] = "Brest"
# print(car.get("key", "Unknown"))
# print(list(car.keys()))
# print(list(car.values()))
# print(list(car.items()))

print("model" in car)
print("model" in car.keys())
print("key" in car)