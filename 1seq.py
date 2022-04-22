# Ввод количества элементов с проверкой на число ----------------------
while True:
    buf_str = input('Ведите количество элементов будущего списка: ')
    if buf_str.isdigit():
        num_list = int(buf_str)
        break
    else:
        print('Вы не ввели число. Повторите')

# Ввод каждого элемента с проверкой на цифру ---------------------------
print()
print('Введите по одной', num_list, 'цифр')
all_digit = []

count = 1
while count <= num_list:
    buf_str = input('Введите ' + str(count) + ' элемент :')

    if buf_str.isdigit() and len(buf_str) == 1:
        one_digit = int(buf_str)
        count += 1
        all_digit = all_digit + [one_digit]
    else:
        print('Вас просили ввести ЦИФРУ!, повторите')
        continue

# Завершение -----------------------------------------------------------
all_digit.sort()
print('Вывод:', all_digit)
