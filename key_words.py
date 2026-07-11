def max_number(a, b):
    if a > b:       # Проверка условие 'a'>'b'
        return a    # Если "да" выводим и выходим из функции
    else:           # Если "нет" то переходим в else
        return b    # Выводи 'b' и выыходим из функции

print ("1: ",max_number(100,6))


def empty_function():
    pass


def even_number(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
result = list(even_number(13))
print("3: ",result)


def max_number(a, b):
    if a > b:
        return a
    else:
        return b

def test_max_number():
    assert max_number(10, 5) == 10, "Ошибка: max_number(10, 5) должна быть равна 10"
    assert max_number(3, 8) == 8, "Ошибка: max_number(3, 8) должна быть равна 8"
    assert max_number(7, 7) == 7, "Ошибка: max_number(7, 7) должна быть равна 7"
    assert max_number(-5, -5) == -5, "Ошибка: max_number(-5, -5) должна быть равна -5"
    assert max_number(0, 0) == 0, "Ошибка: max_number(0, 0) должна быть равна 0"
    assert max_number(3.5, 3.5) == 3.5, "Ошибка: max_number(3.5, 3.5) должна быть равна 3.5"
    assert max_number(-3, -7) == -3, "Ошибка: max_number(-3, -7) должна быть равна -3"
    assert max_number(-10, -2) == -2, "Ошибка: max_number(-10, -2) должна быть равна -2"
    assert max_number(0, 15) == 15, "Ошибка: max_number(0, 15) должна быть равна 15"
    assert max_number(0, -5) == 0, "Ошибка: max_number(0, -5) должна быть равна 0"
    assert max_number(3.14, 2.71) == 3.14, "Ошибка: max_number(3.14, 2.71) должна быть равна 3.14"
    assert max_number(5, 5.0) == 5, "Ошибка: max_number(5, 5.0) должна быть равна 5"

test_max_number()
print("4 : Все тесты пройдены!")