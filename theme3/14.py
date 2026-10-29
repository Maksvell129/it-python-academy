

scores = [5, 2, 9, 1]

# scores.sort(reverse=True)

# print(scores)
#
# print(sorted(scores, reverse=True))

# print(scores)


# cities = ["Minsk", "Mansk"]
#
# print(sorted(cities))


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
}

keys = list(car.keys())
keys.sort()

print(sorted(car))
print(keys)