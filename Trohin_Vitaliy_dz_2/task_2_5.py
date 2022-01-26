from random import uniform


def transfer_list_in_str(list_in: list) -> str:
    list_2 = []
    for el in list_in:
        rub = int(el)
        cop = int((el * 100) % 100)
        list_2.append(f'{rub:02} руб {cop:02} коп')
    str_out = ', '.join(list_2)
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    list_in.sort()
    return list_in


result_2 = sort_prices(my_list)
print(result_2)
id_sorted_my_list = id(result_2)


def sort_price_adv(list_in: list) -> list:
    list_out = sorted(list_in)
    list_out.reverse()
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3)


def check_five_max_elements(list_in: list) -> list:
    list_out = []
    sort_list = sort_price_adv(list_in)
    for i in range(5):
        list_out.append(sort_list[i])
    return list_out


result_4 = check_five_max_elements(my_list)
print(result_4)
