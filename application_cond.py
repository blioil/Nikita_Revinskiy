# Функция для вычисления суммы чётных чисел от 1 до 100
def sum_even_numbers():
    applicat_condition = 0
    for i in range(2, 101, 2):
        applicat_condition += i
    print("Сумма всех четных чисел от 1 до 100: ", applicat_condition)

# Функция для создания списка квадратов нечётных чисел от 1 до 10
def squares_of_odd_numbers():
    nums = [n**2 for n in range(1, 11, 2)]
    print("Квадраты всех нечетных чисел от 1 до 10, используя генератор списка", nums)

# Функция для ввода чисел до первого отрицательного
def count_until_negative():
    count = 0
    while True:
        user_input = input("Введите число: ")
        try:
            num = int(user_input)
        except ValueError:
            print("Ошибка: нужно ввести целое число.")
            continue
        count += 1
        if num < 0:
            break
    print(f"Количество введённых чисел включая отрицательное: {count}")

# Вызов функций для демонстрации
if __name__ == "__main__":
    sum_even_numbers()
    squares_of_odd_numbers()
    count_until_negative()