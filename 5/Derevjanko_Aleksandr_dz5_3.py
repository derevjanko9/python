from itertools import zip_longest
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
# generator_1 = (item for item in zip_longest(tutors, klasses))


def generator_1(list_1, list_2):
    if len(list_1) <= len(list_2):
        for tuple_1 in zip(list_1, list_2):
            yield tuple_1
    else:
        for tuple_1 in zip_longest(list_1, list_2):
            yield tuple_1


print(*generator_1(tutors, klasses))
