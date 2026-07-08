while True:
    try:
        # Запрашиваем числа
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        # Запрашиваем операцию
        operation = input("Выберите операцию (+, -, *, /): ")

        # Выполняем операцию
        if operation == '+':
            result = num1 + num2
            operation_name = "сложения"
        elif operation == '-':
            result = num1 - num2
            operation_name = "вычитания"
        elif operation == '*':
            result = num1 * num2
            operation_name = "умножения"
        elif operation == '/':
            result = num1 / num2
            operation_name = "деления"
        else:
            print("Ошибка: Неизвестная операция!")
            result = None

    except ValueError:
        print("Ошибка: Введено не число!")
        continue  # перезапускаем цикл
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль!")
        continue  # перезапускаем цикл
    else:
        if result is not None:
            print(f"РЕЗУЛЬТАТ {operation_name.upper()}:")
            print(f"{num1} {operation} {num2} = {result}")
    finally:
        # Спрашиваем о продолжении
        decision = input("\nПродолжить? (да/нет): ").lower()
        if decision != 'да':
            print("Программа завершена.")
