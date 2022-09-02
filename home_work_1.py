day = int(input('Введите день едели и нажмите enter: '))
if day<=7 and day >=1:
    if day==6 or day==7:
        print(str(day) + ' -> да') #print(f"{day} -> да")
    else:
        print(str(day) + ' -> нет')#print(f"{day} -> да")
else:
    print('Введён несуществующий день')
