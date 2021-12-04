def thesaurus(*args):
    dict_1 = {}
    for item in args:
        if dict_1.get(item[0], None) is None:
            dict_1[item[0]] = [item]  # dict_1.setdefault(item[0], item)
        else:
            list_1 = dict_1[item[0]]
            list_1.append(item)
            dict_1[item[0]] = list_1
    print(dict_1)


thesaurus('Иван', 'Мария', 'Петр', 'Илья')
