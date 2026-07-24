def count_words(text):
    return len(text.lower().strip(',.!?;:()"\''))

def longest_word(text):
    return max(text.lower().strip(',.!?;:()"\''), key=len)

def count_vowels(text):
    vowels = "аеёиоуыэюя"
    return sum(1 for ch in text.lower() if ch in vowels)

def word_frequency(text):
    freq = {}
    for word in text.split():
        word = word.lower().strip(',.!?;:()"\'')
        if word:
            freq[word] = freq.get(word, 0) + 1
    return freq


# Основная часть
text = input("Введите текст: ")

print("Количество слов:", count_words(text))
print("Самое длинное слово:", longest_word(text))
print("Количество гласных букв:", count_vowels(text))

print("\nЧастота слов:")
for w, cnt in sorted(word_frequency(text).items()):
    print(f"{w}: {cnt}")
