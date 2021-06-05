src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def generator_1(list_2):
    for index_1 in range(1, len(list_2)):
        if src[index_1] > list_2[index_1 - 1]:
            yield list_2[index_1]


print(list(generator_1(src)))
