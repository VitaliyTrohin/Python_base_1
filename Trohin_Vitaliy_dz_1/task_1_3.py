def transform_string(number: int):
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    if number != 11 and number % 10 == 1:
        return f'{number} процент'
    elif (number % 10 == 2 or number % 10 == 3 or number % 10 == 4) and number != 12 and number != 13 and number != 14:
        return f'{number} процента'
    else:
        return f'{number} процентов'


for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))
