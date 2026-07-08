while True:
    try:
        # Запрашиваем числа
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        # Запрашиваем операцию
        operation = input("Выберите операцию (+, -, *, /): ")

        # Инициализируем переменные ДО условия
        result = None
        operation_name = ""  # ← ДОБАВЛЯЕМ: пустая строка по умолчанию

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
            # operation_name уже определена как ""

    except ValueError:
        print("Ошибка: Введено не число!")
        continue
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль!")
        continue
    else:
        # МЕНЯЕМ: проверяем, что результат есть И операция известна
        if result is not None and operation_name:  # ← ИЗМЕНЯЕМ условие
            print(f"Результат {operation_name}: {num1} {operation} {num2} = {result}")
    finally:
        # Спрашиваем о продолжении
        decision = input("\nПродолжить? (да/нет): ").lower()
        if decision != 'да':
            print("Программа завершена.")
            break