names = ["Алексей", "Мария", "Дмитрий"]
salaries = [150000, 180000, 120000]
companies = ["Google", "Amazon", "Apple"]

# for name, salary  in enumerate(names):
#     print(f"{name}: {salaries[i]}")


for name, salary, company in zip(names, salaries, companies):
    print(f"Сотрудник {name} получает {salary} руб. Работает в {company}")
