def multiply(a, b):
    if type(a) not in (int, float) or type(b) not in (int, float):
        return ("Ошибка введенных данных")
    return a * b

result = multiply(2, 3)     # Вызов функции и сохранение ее
print(result)
