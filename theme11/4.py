class PublicUser:
    def __init__(self, name):
        self.name = name

user = PublicUser("Alex")
print(user.name)
user.name = "Maria"
print(user.name)


class ProtectedUser:
    def __init__(self, name):
        self._name = name


user = ProtectedUser("Alex")
print(user._name)
user._name = "Maria"
print(user._name)


class PrivateUser:
    def __init__(self, name):
        self.__name = name

user = PrivateUser("Alex")
print(user._PrivateUser__name)
user.__name = "Maria"
print(user.__name)
