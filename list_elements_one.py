def element(elements_list):
    if len(elements_list) >= 2:
        elements_list[0], elements_list[-1] = elements_list[-1], elements_list[0]
        return elements_list

my_list = ['one', 'two', 'three', 'four', 'five']

print("Созданный список: ", my_list)

result = element(my_list)

print("Измененный список: ", result)
