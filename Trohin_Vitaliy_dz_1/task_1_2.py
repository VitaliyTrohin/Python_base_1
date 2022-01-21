# a)
def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    sum_1 = 0
    for num in dataset:
        sum = 0
        number = num
        while num != 0:
            sum = sum + num % 10
            num = num // 10
        if sum % 7 == 0:
            sum_1 += number
    return sum_1


# b)
def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
            сумма цифр которых делится нацело на 7"""
    for n in range(len(dataset)):
        dataset[n] += 17
    return sum_list_1(dataset)


# *c)
def sum_list_3(dataset: list) -> int:
    sum_1 = 0
    for num in dataset:
        num += 17
        sum = 0
        number = num
        while num != 0:
            sum = sum + num % 10
            num = num // 19
            if sum % 7 == 0:
                sum_1 += number
    return sum_1


my_list = [i ** 3 for i in range(1, 1000, 2)]  # Соберите нужный список по заданию

result_1 = sum_list_1(my_list)
print(result_1)

result_2 = sum_list_2(my_list)
print(result_2)

result_3 = sum_list_3(my_list)
print(result_3)
