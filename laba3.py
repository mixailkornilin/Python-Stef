second_name = ['Корнилин', 'Клейменов', 'Млюкова']
predmet = ['Русский','Математика','География']
date = ['18.10.2013','01.01.2013','12.02.2014']
dati = ['2','3','4','5']

second_name_hash = hash(second_name[0])
predmet_hash = hash(predmet[0])
date_hash = hash(date[0])
dati_hash = hash(dati[0])
print(second_name_hash)
for s in date:
    if s == '18.10.2013':
        for i in predmet:
            if i == 'Русский':
                for g in second_name:
                     for h in dati:
                        print(s, i,g,h)


#Фильтр через хеширование
#фамилия > предмет(повторяетс) > дата(повторяетс) > пустое значение(оценка) не повторяется
#фамилия > предмет > дата > пустое значение
#фамилия > предмет > дата > пустое значение
#фамилия > предмет > дата > пустое значение
