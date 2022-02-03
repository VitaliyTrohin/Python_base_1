def thesaurus(*args) -> dict:
    name_list = [*args]
    dict_out = {}
    for name in name_list:
        name.capitalize()
        capital = name[0]
        if capital in dict_out.keys():
            dict_out[capital].append(name)
        else:
            dict_1 = [name]
            dict_out[capital] = dict_1
    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
