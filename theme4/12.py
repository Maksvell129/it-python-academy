user_role = "guest"

match user_role:
    case "admin":
        print("Полный доступ ко всем настройкам")
    case "editor" | "author":
        print("Доступ к редактированию контента")
    case "guest":
        print("Только просмотр страниц")
    case _:
        print("Неизвестная роль пользователя")
