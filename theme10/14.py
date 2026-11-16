import json

user = {
    "name": "Alex",
    "age": 25,
    "items": ["phone", "keys"]
}

data = json.dumps(user)

# print(data)
# print(type(data))
# print(user)

data = '{"name": "Alex", "age": 25}'


user = json.loads(data)

print(user)
