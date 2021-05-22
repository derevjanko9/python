duration = 400153
minutes = duration//60
hours = minutes//60
day = hours//24

if day > 0:
    hours = hours % 24
    minutes = minutes % 60
    seconds = duration % 60
    print('{} дн {} час {} мин {} сек'.format(day, hours, minutes, seconds))
elif hours > 0:
    minutes = minutes % 60
    seconds = duration % 60
    print('{} час {} мин {} сек'.format(hours, minutes, seconds))
elif minutes > 0:
    seconds = duration % 60
    print('{} мин {} сек'.format(minutes, seconds))
else:
    seconds = duration
    print('{} сек'.format(seconds))