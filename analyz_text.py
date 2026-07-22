# Ввод текста и приведение к нижнему регистру
text = input("Введите текст:\n").lower()

# Удаляем знаки препинания, заменяя их на пробелы
punctuation = ".,!?;:()\"'—«»…"
for p in punctuation:
    text = text.replace(p, " ")

# Подсчёт гласных
vowels = "аеёиоуыэюя"
vowel_total = 0
for ch in text:
    if ch in vowels:
        vowel_total += 1

# Разбиваем текст на слова
words = text.split()

# Количество слов
word_count = len(words)
print(f"Количество слов в тексте: {word_count}")

# Самое длинное слово
longest = ""
for w in words:
    if len(w) > len(longest):
        longest = w
if longest:
    print(f"Самое длинное слово: {longest} (длина: {len(longest)})")
else:
    print("Самое длинное слово: нет слов")

print(f"Количество гласных букв в тексте: {vowel_total}")

# Вывод частоты
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

print("Частота слов:")
if words:
    for w, count in freq.items():
        print(f"  {w}: {count}")
else:
    print("Текст не содержит слов")