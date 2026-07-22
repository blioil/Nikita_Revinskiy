def number_to_english(n):
    # Словарь способ сопоставления
    number_dict = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five"
    }

    return number_dict.get(n)

try:
    n = int(input("Введите число от 1 до 5: "))
except ValueError:
    print("Ошибка: нужно ввести целое число.")
else:
    word = number_to_english(n)
    if word is not None:
        print(word)
    else:
        print("Число должно содержать от 1 до 5")