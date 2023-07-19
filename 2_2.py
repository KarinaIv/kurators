unic_otv = []  #список для уникальных слов, подходящих под условие

alf = 'АЗАРТ'  #алфавит

for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    s = x1 + x2 + x3 + x4 + x5  #создаем строку
                    #проверяем условие, что все буквы встречаются столько раз, сколько в алфавите(перестановки)
                    if s.count('А') == 2  and s.count('З') == 1 and s.count('Р') == 1 and s.count('Т') == 1:
                        if ('АА' not in s) and (s[0] != 'A' and s[-1] != 'А') and ('ЗР' not in s): #проверка условия
                            if s not in unic_otv:  #проверяем, что подходящего слова еще нет в списке
                                unic_otv.append(s) #заносим в список слово
print(len(unic_otv))  #выводим ответ-длину списка