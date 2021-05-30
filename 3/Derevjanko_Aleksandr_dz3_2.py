dict_1 = {'one': 'один',
          'two': 'два',
          'three': 'три',
          'four': 'четыре',
          'five': 'пять',
          'six': 'шесть',
          'seven': 'семь',
          'eight': 'восемь',
          'nine': 'девять'}


def num_translate_adv(digit):
    if digit[0].isupper():
        return (dict_1[digit.lower()]).title()
    else:
        return dict_1[digit]


print(num_translate_adv('one'))
