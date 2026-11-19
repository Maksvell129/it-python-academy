

class User:

    def __init__(self, code, number): # +375 +7
        self.code = code
        self.number = number

    @property
    def phone_number(self) -> str:
        return self.code + str(self.number)

user = User(code="+375", number=332222222)
print(user.phone_number)
