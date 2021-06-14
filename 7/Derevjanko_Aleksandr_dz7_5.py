import os
f = r'c:\Users\proaa\Desktop'
dict_1 = {}
list_100 = []
list_1000 = []
list_10000 = []
list_100000 = []
for tuple_1 in os.walk(f):
    for item in tuple_1[2]:
        if os.stat(tuple_1[0] + '\\' + item).st_size <= 100:
            if list_100.count(item.split('.')[-1]) == 0:
                list_100.append(item.split('.')[-1])
            dict_1.setdefault(100, 0)
            dict_1[100] += 1
        elif 100 < os.stat(tuple_1[0] + '\\' + item).st_size <= 1000:
            if list_1000.count(item.split('.')[-1]) == 0:
                list_1000.append(item.split('.')[-1])
            dict_1.setdefault(1000, 0)
            dict_1[1000] += 1
        elif 1000 < os.stat(tuple_1[0] + '\\' + item).st_size <= 10000:
            if list_10000.count(item.split('.')[-1]) == 0:
                list_10000.append(item.split('.')[-1])
            dict_1.setdefault(10000, 0)
            dict_1[10000] += 1
        else:
            if list_100000.count(item.split('.')[-1]) == 0:
                list_100000.append(item.split('.')[-1])
            dict_1.setdefault(100000, 0)
            dict_1[100000] += 1

for key, val in dict_1.items():
    if key == 100:
        dict_1[key] = (val, list_100)
    elif key == 1000:
        dict_1[key] = (val, list_1000)
    elif key == 10000:
        dict_1[key] = (val, list_10000)
    elif key == 100000:
        dict_1[key] = (val, list_100000)
print(dict_1)
