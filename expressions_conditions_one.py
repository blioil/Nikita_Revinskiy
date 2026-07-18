def can_vote(user_age, user_citizen, user_disqualified):
    if user_age < 18:
        return False, "Вам должно быть 18 лет или старше"
    if not user_citizen:
        return False, "Вы должны быть гражданином страны"
    if user_disqualified:
        return False, "Вы дисквалифицированы для голосования"
    return True, "Вы можете голосовать!"

# Ввод данных
user_age = int(input("Введите ваш возраст: "))
user_citizen = input("Вы гражданин? (да/нет): ").lower() == "да"
user_disqualified = input("Вы дисквалифицированы? (да/нет): ").lower() == "да"

can_vote_result, message = can_vote(user_age, user_citizen, user_disqualified)
print(message)