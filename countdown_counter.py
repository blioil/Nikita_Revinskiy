while True:
    user_input = input("Введите целое положительное число: ")
    try:
        n = int(user_input)
    except ValueError:
        print("Ошибка: нужно ввести целое число.")
        continue
    if n > 0:
        break
    else:
        print("Число должно быть положительным (больше нуля).")

result = []
while n >= 0:
    result.append(n)
    n -= 1

print(result)