def number_to_english(n):
    if n == 1:
        return "one"
    elif n == 2:
        return "two"
    elif n == 3:
        return "three"
    elif n == 4:
        return "four"
    elif n == 5:
        return "five"
    else:
        return None

n = int(input())
word = number_to_english(n)
print(word if word else "Ошибка")