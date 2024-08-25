game_over = 0
import time
import random
clovo = ("_"*24)
class Hero():

    
    # конструкция класса
    
    def __init__(self, name, level, experience, health, armor, attack_power, weapon, strength, agility, inteligence):
        self.name = name
        
        self.level = level

        self.experience = experience
        
        self.health = health

        self.armor = armor

        self.attack_power = attack_power 

        self.weapon = weapon

        self.strength = strength

        self.agility = agility

        self.inteligence = inteligence

        
    # печать инфо о персонаже:
    
    def print_info(self):

        print('\n', '-'*24)

        print('Герой:', self.name)

        print('Игровой Уровень:', self.level)

        print('EXP:', self.experience)

        print('Количество здоровья:', self.health)

        print('Количество брони:', self.armor)

        print('Сила удара:', self.attack_power)

        print('Оружие:', self.weapon)

        print('Сила:', self.strength)

        print('Ловкость:', self.agility)

        print('Разум:', self.inteligence)

        print('-'*24,'\n')

    # нанесение ударов
    
    def strike(self, enemy):

        print('\nУдар! ' + self.name + ' атакует ' + enemy.name 
            + ' с силой ' + str(self.attack_power) + ', используя ' + self.weapon + '\n')
        enemy.armor -= self.attack_power
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        print(enemy.name + ' покачнулся.\nКоличество брони упало до ' +
            str(enemy.armor) + ', а уровень здоровья до ' + str(enemy.health) + '\n')

        # логика начисления опыта
        
        time.sleep(random.randint(1,2))
        EXP = random.randint(1,10)
        self.experience = self.experience + EXP
        #print("EXP ", EXP)
        #print("Всего опыта", self.experience)
        print ("За удар", self.name, "герой получил", EXP, "опыта. Всего:", self.experience, "\n") 
        time.sleep(random.randint(2,3))


    # вступить в схватку
    
    def attack(self, enemy):
        if self.health and enemy.health > 0:
            self.strike(enemy)

            if enemy.health <= 0:
                print(enemy.name, "герой пал в сражении")
                game_over = 1

            if self.health <= 0:
                print(self.name, "герой пал в сражении")
                game_over = 1
        
        
class EnemyHero():
    
    # конструкция класса
    
    def __init__(self):
        self.name = random.choice(['Орк','Эльф','Гоблин','Троль'])
        
        self.level = random.randint(1,3)

        self.experience = 0
        
        self.health = 30 * self.level

        self.armor = random.randint(0,30)

         

        self.weapon = random.choice(['клинок','посох','секира'])

        self.strength = random.randint( 5 * self.level, 10 * self.level)

        self.agility = random.randint(5 * self.level, 10 * self.level)

        self.inteligence = random.randint(5 * self.level, 10 * self.level)

        self.attack_power = random.randint(1,5) * self.strength

        
    # печать инфо о персонаже:
    
    def print_info(self):

        print('\n', '-'*24)

        print('Герой:', self.name)

        print('Игровой Уровень:', self.level)

        print('EXP:', self.experience)

        print('Количество здоровья:', self.health)

        print('Количество брони:', self.armor)

        print('Сила удара:', self.attack_power)

        print('Оружие:', self.weapon)

        print('Сила:', self.strength)

        print('Ловкость:', self.agility)

        print('Разум:', self.inteligence)

        print('-'*24,'\n')

    # нанесение ударов
    
    def strike(self, enemy):

        print('\nУдар! ' + self.name + ' атакует ' + enemy.name 
            + ' с силой ' + str(self.attack_power) + ', используя ' + self.weapon + '\n')
        enemy.armor -= self.attack_power
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        print(enemy.name + ' покачнулся.\nКоличество брони упало до ' +
            str(enemy.armor) + ', а уровень здоровья до ' + str(enemy.health) + '\n')

        # логика начисления опыта
        
        time.sleep(random.randint(1,2))
        EXP = random.randint(1,10)
        self.experience = self.experience + EXP
        #print("EXP ", EXP)
        #print("Всего опыта", self.experience)
        print ("За удар", self.name, "герой получил", EXP, "опыта. Всего:", self.experience, "\n") 
        time.sleep(random.randint(2,3))

    # вступить в схватку

    def attack(self, enemy):
        if self.health and enemy.health > 0:
            self.strike(enemy)

            if enemy.health <= 0:
                print(enemy.name, "герой пал в сражении")
                game_over = 1

            if self.health <= 0:
                print(self.name, "герой пал в сражении")
                game_over = 1
              
# создание обьектов героев



player = Hero('Леонид', 1, 0, 39, 8, 7, 'миниган', 10, 10, 10)
#outlaw = Hero('Ольга', 1, 0, 40, 7, 3, 'лук', 10, 10, 10)
enemy = EnemyHero()

print(enemy)
# основной цикл игры
while game_over != 1:

    # меню выбора вступить ли в схватку

    menu = int(input(clovo + "\n1- Вступить в схватку \n2-Избежать сражения \n3-Информация о герое \n4-Информация о вражеском герое \n5-Выход \nВаш ответ: "))
    print('_'*24,'\n')
    if (menu) == 1:
        while game_over != 1:
        
            # меню сражения
            first_deictvie = int(input(clovo + "\n1-Удар \n2-Пропустить ход \n3-Информация о герое \n4-Информация о вражеском герое \n5-Сдаться \n6-Сбежать с поля боя \nВаш ответ: "))
            print('_'*24,'\n')
            if (first_deictvie) == 1:
               player.attack(enemy)

            if (first_deictvie) == 2:
                print("------------------------")
                print("\nВы пропустили ход")
                print("\n------------------------")
                      
            if (first_deictvie) == 3:
                player.print_info()
                continue # прерывание тела цикла, переход от этой команды к началу выполнения цикла

            if (first_deictvie) == 4:
                enemy.print_info()
                continue
            
            if (first_deictvie) == 5:
                # проработать
                enemy1 = enemy
                enemy = EnemyHero()
                # enemy_list = []
                # enemy.append(enemy)
                # print(enemy_list)
                break
            if (first_deictvie) == 6:
                enemy = EnemyHero()
                break 
            enemy.attack(player)

    if (menu) == 2:
        print("------------------------")
        print("\nВы избижали сражения")
        # проработать последствия
        enemy = EnemyHero()
        print("\n------------------------")
              
    if (menu) == 3:
        player.print_info()
        continue # прерывание тела цикла, переход от этой команды к началу выполнения цикла

    if (menu) == 4:
        enemy.print_info()
        continue
    
    if (menu) == 5:
        break
    
    
    
