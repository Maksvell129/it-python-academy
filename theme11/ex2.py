class Curs:
    def __init__(self, name: str, mark: int | None = None):
        self.__name = name
        self.__mark = mark


    @property
    def name(self):
        return self.__name

    @property
    def mark(self):
        return self.__mark


class Student:
    def __init__(self, name: str):
        self.name = name
        # 1
        self.courses: dict[str, int | None] = {}

        # 2
        # self.courses: list[tuple] = []

        # 3
        # self.courses: list[Curs] = []

    def add_course(self, course_name: str, mark: int | None = None):
        self.courses[course_name] = mark

    # def add_course2(self, curs: Curs):
    #     self.courses.append(curs)

    def get_average_mark(self):
        total = 0
        count = 0
        for mark in self.courses.values():
            if mark is not None:
                total += mark
                count += 1

        if count == 0:
            return 0

        return round(total / count, 2)


    # def get_average_mark2(self):
    #     total = 0
    #     count = 0
    #     for curs in self.courses():
    #         if curs.mark is not None:
    #             total += curs.mark
    #             count += 1
    #
    #     if count == 0:
    #         return 0
    #
    #     return round(total / count, 2)


    def show_unfinished_courses(self):
        print(f"Незавершенные курсы студента {self.name}:")
        has_unfinished = False

        for course, mark in self.courses.items():
            if mark is None:
                print(f"- {course}")
                has_unfinished = True

        if not has_unfinished:
            print("- Все курсы завершены")


def get_best_student(students: list[Student]) -> Student | None:
    if not students:
        return None

    return max(students, key=lambda s: s.get_average_mark())

student1 = Student("Alex")
student1.add_course("Математика", 5)
student1.add_course("Физика", 4)
student1.add_course("История", 5)

student2 = Student("Anna")
student2.add_course("Математика", 3)
student2.add_course("Физика", 4)
student2.add_course("Программирование")

student3 = Student("Елена")
student3.add_course("Химия", 5)
student3.add_course("Биология", 5)
student3.add_course("Английский язык")

student4 = Student("Дмитрий")
student4.add_course("Философия")

all_students = [student1, student2, student3, student4]

print("--- Средние баллы ---")
for s in all_students:
    print(f"{s.name}: {s.get_average_mark()}")

print("\n--- Проверка долгов и текущих курсов ---")
student1.show_unfinished_courses()
print()
student2.show_unfinished_courses()

print("\n--- Лучший студент ---")
best_student = get_best_student(all_students)
print(best_student.name, best_student.get_average_mark())


# [
#     ("Химия", 5),
#     ("Биология", 5),
#     ("Английский язык", None)
# ]