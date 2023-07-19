from itertools import product  #импортируем product

k = 0   #счетчик для результата

for x in product('ДРУЗЬЯ', repeat=6):
    s = ''.join(x)  #перебираем буквы из набора и склеиваем в строку
    if s[0] != 'Ь' and s.count('У') <= 2:
        if 'УЬ' not in s and 'ЬУ' not in s:  #проверяем нужное условие
            k += 1   #если условие выполняется, то увеличиваем счетчик
print(k)  #выводим результат на экран
