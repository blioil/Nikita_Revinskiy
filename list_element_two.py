def elem_list(list_one, list_two):
    # Определяем более длинный и более короткий список
    if len(list_one) <= len(list_two):
        longer_list = list_two
        short_list = list_one
    else:
        longer_list = list_one
        short_list = list_two


    # Суммируем попарно элементы короткого и длинного списков
    sum_list = [short_list[i] + longer_list[i] for i in range(len(short_list))]
    # Добавляем оставшиеся элементы из длинного списка (если есть)
    sum_list.extend(longer_list[len(short_list):])
    return sum_list

# Проверка
list_one = [3, 5, 7, 9, 11, 13]
list_two = [1, 4, 6, 8]
result = elem_list(list_one, list_two)
print("Новый список: ", result)