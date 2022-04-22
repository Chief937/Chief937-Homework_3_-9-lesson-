print('Вам предстоит ввести много цифр через разделитель')

# Выбор разделителя ------------------------------------------------------------
print('Выберите разделитель из предложенных:')
separator_dict = {',': 'запятую', ';': 'точку с запятой', '/': 'слэш'}
print(list(separator_dict.keys()))
while True:
    buf_str = input('Ведите разделитель: ')
    if buf_str in separator_dict.keys():
        my_separator = buf_str
        break
    else:
        print('неверный выбор, повторите')

# Ввод любых цифр без проверки на цифру ----------------------------------------
print()
buf_str = input('Введите любые цифры в одну строку через ' + separator_dict[my_separator] + ':')

# Получение цифр в список ------------------------------------------------------
all_digit = []

buf_str = buf_str.split(my_separator)
for one_str in buf_str:
    if one_str.isdigit() and len(one_str) == 1:
        all_digit.append(int(one_str))

# Создание уникального списка ---------------------------------------------------
uni_set = set()
for one_digit in all_digit:
    uni_set.add(one_digit)

# Завершение --------------------------------------------------------------------
print('Вы ввели цифры: ', all_digit)
print('Из них уникальные: ', list(uni_set))
