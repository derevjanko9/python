list_1 = [58.44, 25.0, 33.40, 88.45, 129.99, 130, 57.28, 72.14, 27.50, 80.40, 29.14, 77.20]
print(id(list_1[0]))
for price in list_1:
    price = '{:.2f}'.format(price)
    rub, kop = price.split('.')
    print('{} руб {:02d} коп'.format(int(rub), int(kop)))

list_1 = sorted(list_1)
print(id(list_1[5]))
for price in list_1:
    price = '{:.2f}'.format(price)
    rub, kop = price.split('.')
    print('{} руб {:02d} коп'.format(int(rub), int(kop)))

list_1.reverse()
list_2 = list_1
print(list_2)

list_3 = list_2[:5]
list_3.reverse()
for price in list_3:
    price = '{:.2f}'.format(price)
    rub, kop = price.split('.')
    print('{} руб {:02d} коп'.format(int(rub), int(kop)))
