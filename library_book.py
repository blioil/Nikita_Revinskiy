# Создание библиотеки
library = {
    "Герой нашего времени": {
        "автор": "Михаил Лермонтов",
        "год издания": 1840,
        "наличие": True
    },
    "Мастер и Маргарита": {
        "автор": "Михаил Булгаков",
        "год издания": 1966,
        "наличие": True
    },
    "Горе от ума": {
        "автор": "Александр Грибоедов",
        "год издания": 1833,
        "наличие": False
    },
    "Финансист": {
        "автор": "Теодор Драйзер",
        "год издания": 1912,
        "наличие": True
    }
}


def book_list_view(library):
    """Выводит только названия книг."""
    if not library:
        print("В библиотеке нет книг.")
        return
    print("\nСписок книг (только названия):")
    for i, title in enumerate(library.keys(), start=1):
        print(f"{i}. {title}")


def book_full_view(library):
    """Выводит полную информацию о книгах."""
    if not library:
        print("В библиотеке нет книг.")
        return
    print("\nПолная информация о книгах:")
    for i, (title, info) in enumerate(library.items(), start=1):
        status = "в наличии" if info["наличие"] else "отсутствует"
        print(f"{i}. {title} — {info['автор']} ({info['год издания']}) — {status}")


def add_book(title, author, year):
    """Добавляет книгу с наличием = None. Если книга уже есть, предлагает обновить."""
    if title in library:
        print(f"Книга \"{title}\" уже существует.")
        choice = input("Хотите обновить информацию о книге? (y/n): ").strip().lower()
        if choice in ('y', 'yes', 'да'):
            library[title]["автор"] = author
            library[title]["год издания"] = year
            print(f"Информация о книге \"{title}\" обновлена.")
        else:
            print("Обновление отменено.")
    else:
        library[title] = {
            "автор": author,
            "год издания": year,
            "наличие": None   # статус не определён
        }
        print(f"Книга \"{title}\" успешно добавлена в библиотеку.")


def console_add_book(library):
    """Вспомогательная функция для ввода данных при добавлении."""
    print("\n--- Добавление новой книги ---")
    title = input("Введите название книги: ").strip()
    if not title:
        print("Название не может быть пустым. Операция отменена.")
        return

    author = input("Введите автора: ").strip()
    if not author:
        print("Автор не может быть пустым. Операция отменена.")
        return

    year_str = input("Введите год издания (целое число): ").strip()
    try:
        year = int(year_str)
    except ValueError:
        print("Год должен быть числом. Операция отменена.")
        return

    if year <= 0:
        print("Год должен быть положительным числом. Операция отменена.")
        return

    add_book(title, author, year)


def remove_book(title):
    """Удаляет книгу по названию. Если книга не найдена, выводит сообщение."""
    if title in library:
        del library[title]
        print(f"Книга \"{title}\" удалена из библиотеки.")
    else:
        print(f"Книга \"{title}\" не найдена в библиотеке.")


def console_remove_book(library):
    """Вспомогательная функция для ввода названия удаляемой книги."""
    print("\n--- Удаление книги ---")
    title = input("Введите название книги, которую хотите удалить: ").strip()
    if not title:
        print("Название не может быть пустым. Операция отменена.")
        return
    remove_book(title)


def main_menu():
    while True:
        print("\n=== Библиотека ===")
        print("1. Показать только названия книг")
        print("2. Показать полную информацию о книгах")
        print("3. Добавить книгу")
        print("4. Удалить книгу")
        print("5. Выйти")
        choice = input("Выберите действие (1-5): ").strip()

        if choice == '1':
            book_list_view(library)
        elif choice == '2':
            book_full_view(library)
        elif choice == '3':
            console_add_book(library)
        elif choice == '4':
            console_remove_book(library)
        elif choice == '5':
            print("До свидания!")
            break
        else:
            print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    main_menu()