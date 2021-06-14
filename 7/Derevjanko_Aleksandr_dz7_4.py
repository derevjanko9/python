import os
f = r'c:\Users\proaa\Desktop'
dict_1 = {}

for tuple_1 in os.walk(f):
    for item in tuple_1[2]:
        if os.stat(tuple_1[0] + '\\' + item).st_size <= 100:
            dict_1.setdefault(100, 0)
            dict_1[100] += 1
        elif 100 < os.stat(tuple_1[0] + '\\' + item).st_size <= 1000:
            dict_1.setdefault(1000, 0)
            dict_1[1000] += 1
        elif 1000 < os.stat(tuple_1[0] + '\\' + item).st_size <= 10000:
            dict_1.setdefault(10000, 0)
            dict_1[10000] += 1
        else:
            dict_1.setdefault(100000, 0)
            dict_1[100000] += 1

print(dict_1)
