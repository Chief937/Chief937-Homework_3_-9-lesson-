# Ввод списков в виде строки ---------------------------------------------------
print('Вам предстоит ввести две последовательности цифр с разделителем запятая')
buf_str1 = input('Введите первую: ')
buf_str2 = input('Введите вторую: ')

# Получение цифр в списки ----ЦИФРЫ МОГУТ ПОВТОРЯТЬСЯ! -------------------------
all_digit1 = []
buf_str1 = buf_str1.split(',')
for one_str in buf_str1:
    if one_str.isdigit() and len(one_str) == 1:
        all_digit1.append(int(one_str))

all_digit2 = []
buf_str2 = buf_str2.split(',')
for one_str in buf_str2:
    if one_str.isdigit() and len(one_str) == 1:
        all_digit2.append(int(one_str))

# Удаляем в списке 1 цифры присутствующие в списке 2 --------------------------
set_digit1 = set(all_digit1)         # уникальные цифры в  1м
set_digit2 = set(all_digit2)         # уникальные цифры во 2м
set_delete = set_digit1 - set_digit2 # цифры, которые НЕ надо удалять
set_delete = set_digit1 - set_delete # цифры, которые НАДО удалить

for one_digit in set_delete:
    for i in range(all_digit1.count(one_digit)):  # ЦИФРЫ МОГУТ ПОВТОРЯТЬСЯ!
        all_digit1.remove(one_digit)

# Завершение ------------------------------------------------------------------
print()
print(all_digit1)

