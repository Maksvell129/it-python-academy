hero = {
    "name": "Воин",
    "level": 1,
    "inventory": ['sword', "potion"],
    "skills": {
        "attack": 10,
        "defense": 5
    }
}


for key in hero:
    print(f"{key}: {hero[key]}")


for value in hero.values():
    print(f"{value}")


for key, value in hero.items():
    print(f"{key} - {value}")