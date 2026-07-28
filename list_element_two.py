def elem_list(list_one, list_two):
    # Определяем более длинный и более короткий список
    if len(list_one) <= len(list_two):
        longer_list = list_two
        short_list = list_one
    else:
        longer_list = list_one
        short_list = list_two

    sum_list = []
    # Суммируем элементы, пока есть пары
    for i in range(len(short_list)):
        sum_list.append(short_list[i] + longer_list[i])
    # Добавляем оставшиеся элементы из длинного списка
    for i in range(len(short_list), len(longer_list)):
        sum_list.append(longer_list[i])
    return sum_list


list_one = [3, 5, 7, 9, 11, 13]
list_two = [1, 4, 6, 8]
result = elem_list(list_one, list_two)
print("Новый список: ", result)