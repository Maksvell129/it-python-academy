import json

# with open("user.json", "r", encoding="utf-8") as file:
#     user = json.load(file)
#
# print(user)
# print(user["name"])


import json

user = {
    "name": "Alex",
    "age": 25,
    "skills": ["Python", "SQL"],
    "is_active": True,
    "is_banned": False,
    "example": None,
}

user2 = {
    "name": "Vlad",
    "age": 25,
    "skills": ["Python", "GO"],
    "is_active": True,
    "is_banned": False,
    "example": None,
}

with open("users.json", "w", encoding="utf-8") as file:
    json.dump([user, user2], file, ensure_ascii=False, indent=4)
