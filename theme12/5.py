from dataclasses import dataclass


@dataclass
class User:

    name: str
    age: int
    email: str


user = User(name="Alex", age=25, email="alex@example.com")
user2 = User("Alex2", 35, "alex@example.com")

print(type(user))
print(user2)
