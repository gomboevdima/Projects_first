from datetime import datetime
try:
    year = 2022
    month = int(input('Input month'))
    day = int(input('Input day'))
    data = datetime(year, month, day)
    if data >=datetime(year, 1, 20) and data <= datetime(year, 2, 18):
        print('Водолей')
    elif data >= datetime(year, 2, 19) and data <= datetime(year, 3, 20):
        print('Рыбы')
    elif data >= datetime(year, 3, 21) and data <= datetime(year, 4, 19):
        print('Овен')
    elif data >= datetime(year, 4, 20) and data <= datetime(year, 5, 20):
        print('Телец')
    elif data >= datetime(year, 5, 21) and data <= datetime(year, 6, 20):
        print('Близнецы')
    elif data >= datetime(year, 6, 21) and data <= datetime(year, 7, 22):
        print('Рак')
    elif data >= datetime(year, 7, 23) and data <= datetime(year, 8, 22):
        print('Лев')
    elif data >= datetime(year, 8, 23) and data <= datetime(year, 9, 22):
        print('Дева')
    elif data >= datetime(year, 8, 23) and data <= datetime(year, 9, 22):
        print('Весы')
    elif data >= datetime(year, 8, 23) and data <= datetime(year, 9, 21):
        print('Скорпион')
    elif data >= datetime(year, 8, 22) and data <= datetime(year, 9, 21):
        print('Телец')
    else:
        print('Козерог')
except ValueError:
    print('Error')