src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# set_1 = set(src)
# print(set_1)
list_1 = []
for item in src:
    if item not in list_1:
        list_1.append(item)
print(list_1)
