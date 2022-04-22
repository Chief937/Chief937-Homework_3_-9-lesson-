import random

# известные люди нашего ЖЭКа -----------------------------------------------------------------------
persona = {
    0: {'name': 'Иванов',    'birth_short': '01.01.1971', 'birth_long': 'первое января 1971 года'},
    1: {'name': 'Петров',    'birth_short': '02.02.1972', 'birth_long': 'второе февраля 1972 года'},
    2: {'name': 'Сидоров',   'birth_short': '03.03.1973', 'birth_long': 'третье марта 1973 года'},
    3: {'name': 'Васильев',  'birth_short': '04.04.1974', 'birth_long': 'четвертое апреля 1974 года'},
    4: {'name': 'Викторов',  'birth_short': '05.05.1975', 'birth_long': 'пятое мая 1975 года'},
    5: {'name': 'Кузнецов',  'birth_short': '06.06.1976', 'birth_long': 'шестое июня 1976 года'},
    6: {'name': 'Волков',    'birth_short': '07.07.1977', 'birth_long': 'седьмое июля 1977 года'},
    7: {'name': 'Попов',     'birth_short': '08.08.1978', 'birth_long': 'восьмое августа 1978 года'},
    8: {'name': 'Андреев',   'birth_short': '09.09.1979', 'birth_long': 'девятое сентября 1979 года'},
    9: {'name': 'Рабинович', 'birth_short': '10.10.1980', 'birth_long': 'десятое октября 1980 года'},
}

# вопросы и ответы ----------------------------------------------------------------------------------
all_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
game_over = False

while not game_over:
    print('\nОтветьте на пять вопросов')
    random_num = random.sample(all_num, 5)

    quest_num = 0
    correct = 0

    for num in random_num:
        quest_num += 1
        print(quest_num, 'Напишите дату рождения сотрудника с фамилией', persona[num]['name'])
        answer = input('dd.mm.yyyy: ')
        if answer == persona[num]['birth_short']:
            correct += 1
            print('OK')
        else:
            print('Правильный ответ', persona[num]['birth_long'])

    print('\nВы ответили правильно на ', correct, 'вопросов')
    answer = input('Желаете попробовать снова? введите y/n ')
    if answer != 'y':
        game_over = True

print('GAME OVER!!!')
