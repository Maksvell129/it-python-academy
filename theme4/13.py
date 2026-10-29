banned_users = ["alex33", "shadow_king", "bot_tester"]
current_user = "top_donater"

vip_users = ("vip_user1", "vip_user2", "top_donater")

if current_user in banned_users:
    print("Доступ заблокирован! Пользователь находится в черном списке.")
elif current_user in vip_users:
    print("Добро пожаловать в ВИП категорию!")
else:
    print("Добро пожаловать!")
