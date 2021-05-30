from random import randint
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n):
    """ Принимает колличество шуток """
    list_1 = []
    while n > 0:
        n -= 1
        list_1.append(f'{nouns[randint(0, 4)]} {adverbs[randint(0, 4)]} {adjectives[randint(0, 4)]}')
    return list_1


print(get_jokes(2))
