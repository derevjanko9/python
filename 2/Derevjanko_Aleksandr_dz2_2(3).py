list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_2 = []
for item in list_1:
    if item.count('1'):
        list_2.append(list_1.index(item))
    elif item.count('2'):
        list_2.append(list_1.index(item))
    elif item.count('3'):
        list_2.append(list_1.index(item))
    elif item.count('4'):
        list_2.append(list_1.index(item))
    elif item.count('5'):
        list_2.append(list_1.index(item))
    elif item.count('6'):
        list_2.append(list_1.index(item))
    elif item.count('7'):
        list_2.append(list_1.index(item))
    elif item.count('8'):
        list_2.append(list_1.index(item))
    elif item.count('9'):
        list_2.append(list_1.index(item))
list_2.reverse()
print(list_2)
list_3 = []
for item in list_1:
    if item.count('+'):
        list_3.append(list_1.index(item))
print(list_3)
for number in range(len(list_1)):
    if list_2.count(number):
        list_1[number] = '{:02d}'.format(int(list_1[number]))
for number in range(len(list_1)):
    if list_3.count(number):
        list_1[number] = '+' + list_1[number]

for item in list_2:
    list_1.insert(item + 1, '"')
    list_1.insert(item, '"')
print(list_1)

string_1 = ' '.join(list_1)
print(string_1)
string_1 = string_1.replace('" 0', '"0')
string_1 = string_1.replace('" 1', '"1')
string_1 = string_1.replace('" 2', '"2')
string_1 = string_1.replace('" 3', '"3')
string_1 = string_1.replace('" 4', '"4')
string_1 = string_1.replace('" 5', '"5')
string_1 = string_1.replace('" 6', '"6')
string_1 = string_1.replace('" 7', '"7')
string_1 = string_1.replace('" 8', '"8')
string_1 = string_1.replace('" 9', '"9')
string_1 = string_1.replace('" +', '"+')
string_1 = string_1.replace('0 "', '0"')
string_1 = string_1.replace('1 "', '1"')
string_1 = string_1.replace('2 "', '2"')
string_1 = string_1.replace('3 "', '3"')
string_1 = string_1.replace('4 "', '4"')
string_1 = string_1.replace('5 "', '5"')
string_1 = string_1.replace('6 "', '6"')
string_1 = string_1.replace('7 "', '7"')
string_1 = string_1.replace('8 "', '8"')
string_1 = string_1.replace('9 "', '9"')
print(string_1)
