import re
RE_EMAIL = re.compile(r'([a-z]+(?:\d+)*)[@]([a-z]+\.[a-z]+)')


def email_parse(name):
    dict_1 = {}
    for items in RE_EMAIL.findall(name):
        dict_1['username'] = items[0]
        dict_1['domain'] = items[1]
    if len(dict_1) == 0:
        raise ValueError(f'wrong emai {name}')
    return dict_1


print(email_parse('derevanko@yandex.ru'))
print(email_parse('derevjanko9@gmail.com'))
print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))
