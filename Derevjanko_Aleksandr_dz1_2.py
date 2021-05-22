list_1 = []
for number in range(1, 1001):
    list_1.append(number**3)
print(list_1)
sum_2 = 0
for number in list_1:
    number = str(number)
    sum_1 = 0
    for i in number:
        i = int(i)
        sum_1 += i
    if sum_1 % 7 == 0:
        sum_2 += sum_1
print(sum_2)
list_3 = []
for number in list_1:
    number = number + 17
    list_3.append(number)
print(list_3)
sum_2 = 0
for number in list_3:
    number = str(number)
    sum_1 = 0
    for i in number:
        i = int(i)
        sum_1 += i
    if sum_1 % 7 == 0:
        sum_2 += sum_1
print(sum_2)

for number in range(1000):
    list_1[number] += 17
print(list_1)
sum_2 = 0
for number in list_1:
    number = str(number)
    sum_1 = 0
    for i in number:
        i = int(i)
        sum_1 += i
    if sum_1 % 7 == 0:
        sum_2 += sum_1
print(sum_2)