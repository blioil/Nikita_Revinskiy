# Функция для вычисления среднего арифметического оценок
def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)


# Функция для вывода информации об одном студенте
def print_student_info(student):
    name = student["name"]
    avg = calculate_average(student["grades"])
    status = "успешен" if avg >= 75 else "отстающий"
    print(f"Студент: {name}\n Средний балл: {avg:.2f}\n Статус: {status}\n")


# Функция для вычисления общего среднего балла по всем студентам
def compute_overall_average(students):
    if not students:
        return 0
    total = sum(calculate_average(student["grades"]) for student in students)
    return total / len(students)


# Функция для добавления нового студента в список
def add_student(students, name, grades):
    avg = calculate_average(grades)
    new_student = {"name": name, "grades": grades, "average": avg}
    students.append(new_student)
    return new_student


# Функция для удаления студента с самым низким средним баллом
# Возвращает удалённого студента или None, если:
#   - список пуст
#   - минимальный средний балл >= 75 (все студенты успешны)
def remove_lowest(students):
    if not students:
        return None
    # Находим минимальный средний балл
    min_avg = min(calculate_average(student["grades"]) for student in students)
    # Если минимальный средний >= 75, удаление невозможно
    if min_avg >= 75:
        return None
    # Ищем первого студента с этим баллом и удаляем
    for i, student in enumerate(students):
        if calculate_average(student["grades"]) == min_avg:
            removed = students.pop(i)
            return removed
    return None


# Основная функция, которая обновляет и выводит всю информацию
def update_and_display(students):
    print("\nТекущий список студентов")
    for student in students:
        print_student_info(student)
    overall = compute_overall_average(students)
    print(f"Общий средний балл по всем студентам: {overall:.2f}\n")


# Главная функция с меню
def main():
    # Начальный список студентов
    students = [
        {"name": "Harry", "grades": [80, 90, 78]},
        {"name": "Hermione", "grades": [95, 90, 97]},
        {"name": "Ron", "grades": [90, 70, 70]},
        {"name": "Draco", "grades": [70, 60, 80]},
        {"name": "Aston", "grades": [40, 30, 58]},
        {"name": "Zena", "grades": []}
    ]


    while True:
        print("\n===== Меню управления студентами =====")
        print("1. Показать всех студентов")
        print("2. Добавить нового студента")
        print("3. Удалить студента с наименьшим средним баллом")
        print("4. Показать только общий средний балл")
        print("5. Выйти")
        choice = input("Выберите действие (1-5): ").strip()

        if choice == '1':
            update_and_display(students)

        elif choice == '2':
            name = input("Введите имя студента: ").strip()
            if not name:
                print("Имя не может быть пустым.")
                continue
            grades_input = input("Введите оценки через пробел (или оставьте пустым): ").strip()
            if grades_input == "":
                grades = []
            else:
                try:
                    grades = [int(x) for x in grades_input.split()]
                except ValueError:
                    print("Ошибка: введите только целые числа через пробел.")
                    continue
            added = add_student(students, name, grades)
            print(f"Студент {added['name']} добавлен, средний балл: {added['average']:.2f}")

        elif choice == '3':
            if not students:
                print("Список студентов пуст, удаление невозможно.")
            else:
                removed = remove_lowest(students)
                if removed is None:
                    # Список не пуст, но минимальный средний >= 75
                    print("Все студенты имеют средний балл >= 75, удаление невозможно.")
                else:
                    avg = calculate_average(removed['grades'])
                    print(f"\nУдалён студент {removed['name']} (средний балл {avg:.2f})")

        elif choice == '4':
            overall = compute_overall_average(students)
            print(f"Общий средний балл по всем студентам: {overall:.2f}")

        elif choice == '5':
            print("Выход из программы.")
            break

        else:
            print("Неверный ввод. Пожалуйста, выберите число от 1 до 5.")


if __name__ == "__main__":
    main()