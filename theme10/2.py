import os

print(os.getcwd())

print(os.listdir("data"))

print(os.path.exists("1.py"))

print(os.path.isfile("data.txt"))

print(os.path.isdir("data.txt"))

path = os.path.join("data", "users.txt")

print(path)