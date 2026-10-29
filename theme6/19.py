def outer():

    x = 10

    def inner():
        print(x)

    inner()

outer()


# def write_users_in_docs(users):
#
#     def _format(user):
#         #
#         return f"{user['first_name']} {user['last_name']}"
#
#     #   открыть файл
#     #   проверка файла
#     #   закрыть файл
#     for user in users:
#         print(_format(user))
#
# write_users_in_docs(users=[
#     {"first_name": "John", "last_name": "Doe"},
#     {"first_name": "Max", "last_name": "Doe"},
# ])
