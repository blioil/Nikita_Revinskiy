def elem_list(list1, list2):
    max_len = max(len(list1), len(list2))
    sum_list = []
    for i in range(max_len):
        a = list1[i] if i < len(list1) else 0
        b = list2[i] if i < len(list2) else 0
        sum_list.append(a + b)
    return sum_list


list1 = [3, 5, 7, 9, 11, 13]
list2 = [1, 4, 6, 8]

print(elem_list(list1, list2))