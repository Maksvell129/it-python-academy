from copy import deepcopy

inventory = [
    "меч",
    "щит"
]

hero = {
    "name": "Воин",
    "level": 1,
    "inventory": inventory,
    "skills": {
        "attack": 10,
        "defense": 5
    }
}

hero2 = deepcopy(hero)

print(hero)
print(hero2)
print(hero2 is hero)

hero["name"] = "Сильнейший воин"

print(hero)
print(hero2)


hero2["inventory"].append("макбук")

print("+" * 20)
print(hero)
print(hero2)


hero3 = deepcopy(hero)

hero3["skills"]["attack"] += 2

print("+" * 20)
print(hero)
print(hero2)
print(hero3)
