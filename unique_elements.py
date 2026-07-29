def create_list():
    my_list = []
    while True:
        user_input = input("Введите элемент по одному :  , а для завершения списка введите (\"пустую строку\" или \"стоп\"): ").strip().lower()
        if user_input == "" or user_input == "стоп":
            print("Завершение ввода")
            break
        my_list.append(user_input)
    return my_list


def count_unique_elements(lst):
    try:
        return len(set(lst))
    except TypeError:
        print("Ошибка: переданный объект не является списком.")
        return 0


def main():
    my_list = create_list()
    if my_list:
        unique_count = count_unique_elements(my_list)
        print(f"Список: {my_list}  \nКоличество уникальных элементов: {unique_count}")
    else:
        print("Список пуст, уникальных элементов нет.")

if __name__ == "__main__":
    main()
