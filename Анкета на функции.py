while True:
    FIO1 = input ('Введите свое ФИО ')
    if len(FIO1) >=2:
        break

while True:
    FIO2 = input ('Введите Ваш возраст ')
    if len(FIO2) <=100:
        break

while True:
    FIO6 = input ('Введите город проживания ')
    if len(FIO6) >=1:
        break

while True:
    FIO3 = input ('Введите ваш класс ')
    if len(FIO3) >=2:
        if int(FIO3) < 12:
            break

while True:
    FIO4 = input ('Введите Ваш любимый предмет в школе ')
    if len(FIO4) >=2:
        break

while True:
    FIO5 = input ('Чем нравится вам предмет ')
    if len(FIO5) >=3:
        break

while True:
    FIO7 = input ('Введите ваше хобби ')
    if len(FIO7) >=3:
        break

while True:
    FIO8 = input ('Введите чего не хватает школе ')
    if len(FIO8) >=3:
        break

while True:
    FIO9 = input ('Введите какой технологии не хвататет миру ')
    if len(FIO9) >=3:
        break

while True:
    FIO10 = input ('Введите кем бы Вы хотели стать через 10 лет? ')
    if len(FIO10) >=3:
        break

while True:
    FIO11_1 = input ('Введите Вашу глобальную или близкую цель ')
    if len(FIO11_1) >=3:
        break

if FIO11_1 == 'да' or FIO11_1 == 'Да':
   while True:
    FIO13_2 = input ('Введите что это за цель и как её можно назвать ')
    if len(FIO13_2) >=3:
        break
    
   while True:
    FIO13_3 = input ('Введите что Вам сейчас может пригодиться или помочь в том, чтобы приблизиться к Вашей цели? ')
    if len(FIO13_3) >=3:
        break

def say ():
    print (f'ФИО человека {FIO1}')
    print (f'Этому человеку {FIO2} лет')
    print (f'Город проживания{FIO6}')
    print (f'Учится в {FIO3} классе')
    print (f'Любимый предмет {FIO4}')
    print (f'Этому человеку нравится предмет {FIO4}, потому-что {FIO3}')
    print (f'Хобби человека {FIO7}')
    print (f'Этому человеку в школе нехватает {FIO8}')
    print (f'По мнению человека миру нехватает технологии {FIO9}')
    print (f'Этот человек через 10 лет хотел-бы стать {FIO10}')
    print (f'Глобальная или близкая цель человека {FIO11_1}')
    if FIO11_1 == 'да' or FIO11_1 == 'Да':
        print (f'Цель человека и как её можно назвать: {FIO13_2} ')
        print (f'Что может помочь человеку для выполнения цели: {FIO13_3} ')
say()

    
