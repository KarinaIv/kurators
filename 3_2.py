nums = 0 #счетчик для номеров

alf = '9876543210' #все цифры

for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    kod = x1 + x2 + x3 + x4 + x5 #перебираем цифры из набора и склеиваем в строку
                    nums += 1 #увеличиваем счетчик
                    if int(kod) % 105 == 0 and nums % 2 != 0: #так как 3,5,7 взаимно простые, то код должен делиться на 3*5*7=105
                        #заменяем все цифры на 0 и 1, чтобы проверить последнее условие
                        kod = kod.replace('2', '0').replace('4', '0').replace('6', '0').replace('8', '0')
                        kod = kod.replace('3', '1').replace('5', '1').replace('7', '1').replace('9', '1')
                        if ('01' not in kod) and ('10' not in kod):
                            print(nums) #выводим номер первого кода, подходящего под условие
                            exit()
