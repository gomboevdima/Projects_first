import random


choose_1 = ""
print('Привет/Hello')
us_message = input("Вы можете пообщаться на разные темы с этим ботом (Работа\Погода\Полезные навыки): ").upper()
if us_message == "РАБОТА":
    print(f'Окей. Вы выбрали: Работу.\nНачнем с того что в мире существуют множество работ и я предлогаю вам поиграть в игру (Y/ДА ; U/НЕТ):')
    while choose_1 != "СТОП":
        game_1 = ['Ваша работа программист', 'Ваша работа продавец', 'У вас ваш бизнес', 'Ваша работа строитель']
        print(game_1[random.randint(0, 3)])
        choose_your = input("Y/U: ").upper()
        if choose_your == "Y":
            print('Угадал')
        if choose_your == "U":
            print("Не угадал значит")
        if choose_your == "СТОП":
            print("Ок, до встречи, пока!")
            break
elif us_message == 'ПОГОДА':
    е = ['Сегодня ветрено', 'Солнечно', 'Дождь']
    print(е[random.randint(0, 2)])
elif us_message == 'ПОЛЕЗНЫЕ НАВЫКИ':
    print('https://pythonworld.ru/')
else:
    print("Error")