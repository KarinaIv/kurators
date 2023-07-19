from itertools import product #импортируем product

nums = 0  #счетчик для номеров

for x in product('9876543210', repeat=5):
    kod = ''.join(x) #перебираем цифры из набора и склеиваем в строку
    nums += 1        #увеличиваем счетчик
    if nums % 2 != 0: #проверяем, что номер нечетный
        if int(kod) % 3 == 0 and int(kod) % 7 == 0 and int(kod) % 5 == 0: #проверка на делимость на 3,5,7
            #заменяем все цифры на 0 и 1, чтобы проверить последнее условие
            kod = kod.replace('2', '0').replace('4', '0').replace('6', '0').replace('8', '0')
            kod = kod.replace('3', '1').replace('5', '1').replace('7', '1').replace('9', '1')
            if ('01' not in kod) and ('10' not in kod):
                print(nums) #выводим номер первого кода, подходящего под условие
                break
