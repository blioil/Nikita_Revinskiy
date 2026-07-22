def can_vote(user_age, user_citizen, user_disqualified):
    if user_age < 0:
        return False, "Возраст не может быть отрицательным."
    if user_age < 18:
        return False, "Вам должно быть 18 лет или старше."
    if not user_citizen:
        return False, "Вы должны быть гражданином страны"
    if user_disqualified:
        return False, "Вы дисквалифицированы для голосования"
    return True, "Вы можете голосовать!"

# Ввод данных
while True:
    user_int = (input("Введите ваш возраст: "))
    try:
        user_age = int(user_int)
        if user_age < 0:
            print("Возраст не может быть отрицательным.")
            continue
        break
    except ValueError:
        print("Ошибка:\"Введите целое данные\"")

# Ввод гражданство
citizen_input = input("Вы гражданин? (да/нет): ").strip().lower()
user_citizen = citizen_input in ("да", "yes", "no", "нет")

# Ввод дисквалификации
disqual_input = input("Вы дисквалифицированы? (да/нет): ").strip().lower()
user_disqualified = disqual_input in ("да", "yes", "no", "нет")

message = can_vote(user_age, user_citizen, user_disqualified)
print(message)