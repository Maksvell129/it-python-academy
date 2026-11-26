import json


class User:
    def __init__(self, name, age, marks: [str] | None = None):

        if marks is None:
            marks = []

        self.age = age
        self.name = name
        self.marks = marks

    @classmethod
    def from_string(cls, data: str):
        name, age = data.split(",")
        return cls(name, int(age))

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["name"], data["age"])

    @classmethod
    def from_list(cls, data: list):
        return cls(data[0], data[1])

    @classmethod
    def from_json(cls, data: str):
        data = json.loads(data)
        return cls(data["name"], data["age"])


class Admin(User):
    pass


# user1 = User("Alex", 25)
#
# user2 = User.from_string("Maria,27")
#
# print(user1.age, user1.name)
# print(user2.age, user2.name)

admin = Admin.from_string("Alex,30")

print(admin.name)
print(admin.age)
print(admin)