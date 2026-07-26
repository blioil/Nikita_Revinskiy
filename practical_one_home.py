# Функция для вычисления среднего арифметического оценок
def calculate_average(grades):
    if not grades:          # защита от пустого списка
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
def remove_lowest(students):
    if not students:
        return None
    # Находим минимальный средний балл
    min_avg = min(calculate_average(student["grades"]) for student in students)
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

# 1. Создаём начальный список студентов
students = [
    {"name": "Harry", "grades": [80, 90, 78]},
    {"name": "Hermione", "grades": [95, 90, 97]},
    {"name": "Ron", "grades": [90, 70, 70]},
    {"name": "Draco", "grades": [70, 60, 80]},
    {"name": "Aston", "grades": [40, 30, 58]},
    {"name": "Zena", "grades": []}
]


# Первый вывод
update_and_display(students)

# Добавляем нового студента
added = add_student(students, "Eve", [80, 85, 90, 75])
print(f"После добавления нового студента {added['name']}:")
update_and_display(students)

# Удаляем студента с самым низким средним баллом
removed = remove_lowest(students)
if removed:
    print(f"После удаления студента {removed['name']} (средний балл {calculate_average(removed['grades']):.2f}):")
else:
    print("Список студентов пуст, удаление невозможно.")
update_and_display(students)