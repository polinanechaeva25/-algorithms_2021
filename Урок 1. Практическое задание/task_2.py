"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать где какая сложность.

Примечание:
Построить список можно через списковое включение.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""


# O(n**2)

def find_min_2(my_list):
    min = my_list[0]                            #O(1)
    for el in range(len(my_list)):              #O(n)
        for idx in range(len(my_list) - 1):     #O(n)
            if my_list[el] < my_list[idx]:      #O(1)
                if my_list[el] < min:           #O(1)
                    min = my_list[el]           #O(1)
            elif my_list[idx] < min:            #O(1)
                min = my_list[idx]              #O(1)
    return min                                  #O(1)


# O(n)
def find_min_1(my_list):
    min = my_list[0]    #O(1)
    for el in my_list:  #O(n)
        if el <= min:   #O(1)
            min = el    #O(1)

    return min          #O(1)


#################################################################################################################

list_test = [x**2+3*x-6 for x in range(-10, 20)]
print(find_min_1(list_test))
print(find_min_2(list_test))
