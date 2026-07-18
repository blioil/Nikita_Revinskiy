def max_number(a, b):
    if a > b:
        return a
    return b


def even_number(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


def empty_function():
    pass


def test_max_number():
    assert max_number(10, 5) == 10, "Ошибка: первое число (10) должно быть больше"
    assert max_number(3, 8) == 8, "Ошибка: второе число (8) должно быть больше"
    assert max_number(7, 7) == 7, "Ошибка: при равенстве должно возвращать 7"
    assert max_number(-3, -7) == -3, "Ошибка: -3 больше, чем -7"

if __name__ == "__main__":
    print("1:", max_number(100, 6))

    result = list(even_number(13))
    print("3:", result)

    test_max_number()
    print("4: Все тесты пройдены!")