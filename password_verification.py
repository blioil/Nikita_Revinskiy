# Задаём правильный пароль
correct_password = "12345"

# Цикл для запроса пароля
while True:
    user_input = input("Введите пароль: ")
    if user_input == correct_password:
        print("Пароль верный! Доступ разрешён.")
        break
    else:
        print("Неверный пароль. Попробуйте снова.")