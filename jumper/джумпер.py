import pygame #    Импортируем модуль pygame
pygame.init() #    Инициализируем pygame
SC_W = 900 #    Ширина окна
SC_H = 700 #    Высота окна
screen = pygame.display.set_mode((SC_W, SC_H)) #    Создаём окно
pygame.display.set_caption('Джампер') #    Заголовок окна
BG = pygame.image.load('bg.png').convert() #    Загружаем фоновое изображение
earth = SC_H - 55 #    Задаём уровень земли (высота экрана минус 55)
fps = 60 #    Число кадров в секунду
clock = pygame.time.Clock() #    Создаём часы
font = pygame.font.SysFont('Arial', 50, bold=True) #    Создаём шрифт для отображения набранных очков
score = 0 #    Переменная для сохранения очков
running = True #    Переменная отвечает за запуск игры и её завершение
game_over = False #    Переменная отвечающая за конец игры (False - игра не завершена, True - игрок проиграл)
class Characters: #    Класс для спрайтов (персонажа и гриба)
    def __init__(self, img, scale, lef, bot, x, y): #    Инициализация спрайта
    #    Загружаем и масштабируем спрайт (изображение, 0 - угол поворота в градусах, scale - масштаб)
        self.sprite = pygame.transform.rotozoom(pygame.image.load(img), 0, scale)
        self.rect = self.sprite.get_rect() #    Получаем четырёхугольник вокруг спрайта
        self.rect.left = lef #    Устанавливаем левую границу для отображения спрайта
        self.rect.bottom = bot #    Устанавливаем начальное значение нижней границы четырёхугольника
        self.speed = [x, y] #    Скорость персонажа по оси X и оси Y
        self.jamp_is = True #    Определяем возможность прыжка
        self.jamp_speed = 20 #    Скорость прыжка
        self.jamp_count = 0 #    Счётчик высоты (необходим, чтобы персонаж не улетел за пределы экрана)
    def move(self): #    Метод движения персонажа
        global score, fps #    Используем глобальные переменные внутри функции с возможностью их изменения
        self.rect = self.rect.move(self.speed) #    Перемещаем спрайт в заданных направлениях
        #    Данное условие будет распространяться только на мухомор, так как спрайт игрока не может двигаться по оси X
        if self.rect.left < 0: #    Если спрайт вышел за пределы экрана слева, ТО...
            self.rect.right = SC_W #    ...отобразить его снова справа
            score += 1 #    ...увеличиваем очки
            fps += 2 #    ...увеличиваем скорость игры
    def gravity(self): #    Гравитация
        if self.rect.bottom > earth: #    Если нижний край спрайта больше чем высота экрана минус расстояние до земли, ТО...
            self.rect.bottom = earth #    ...возвращаем персонажа на землю (псевдогравитация)

#    Создаём объект игрока (изображение, масштаб, левая граница для отображения спрайта, уровень земли, скорость X, скорость Y)
player = Characters('bunny.png', 0.7, 50, earth, 0, 9)
#    Создаём объект мухомора (изображение, масштаб, левая граница для отображения спрайта, уровень земли, скорость X, скорость Y)
mushroom = Characters('mushroom.png', 0.7, SC_W, earth, -10, 0)

while running: #    Основной игровой цикл (обработка событий, обновление позиций объектов на основе событий, рисование объектов в новых позициях)
    for event in pygame.event.get(): #    Проверка очереди событий на нажатие клавиш
        if event.type == pygame.QUIT: #    Если был нажат крестик справа вверху, ТО...
            running = False #    ...завершить игру
        elif event.type == pygame.KEYDOWN: #    Проверка события, нажата ли клавиша (pygame.KEYDOWN - это тип события (нажатие на кнопку))
            if event.key == pygame.K_ESCAPE: #    Если была нажата клавиша Esc, ТО...
                running = False #    ...завершить игру
                #    Если нажат пробел И персонаж находится на земле И прыжок запрещён, ТО...
            if event.key == pygame.K_SPACE and player.rect.bottom == earth and not(player.jamp_is):
                player.jamp_is = True #    ...разрешаем прыжок
                player.jamp_count = player.jamp_speed #    ...счётчик высоты равен высоте прыжка
    if player.jamp_is and player.jamp_count > 0: #    Если прыжок разрешён И счётчик высоты больше нуля, ТО...
        player.rect.y -= player.jamp_speed #    ...перемещаем спрайт персонажа по оси Y
        player.jamp_count -= 1 #    ...уменьшаем счётчик высоты на 1
    else: #    Если условие не выполнено, ТО...
        player.jamp_is = False #    ...запрещаем прыжок и персонаж падает вниз
    if player.rect.colliderect(mushroom.rect): #    Если игрок столкнулся с мухомором, ТО...
        game_over = True #    ...игрок проиграл и игра останавливается
    if not(game_over): #    Если игрок НЕ проиграл, ТО...
        player.move() #    Вызываем метод движения для персонажа
        player.gravity() #    Вызываем метод гравитации
        mushroom.move() #    Вызываем метод движения для мухомора
    else: #    Если игрок проиграл, ТО всё движение останавливается...
        key = pygame.key.get_pressed() #    ...получаем список зажатых клавиш в виде словаря
        if key[pygame.K_SPACE]: #    Если игрок нажимает на клавишу пробел, ТО...
            score = 0 #    ...счёт обнуляется
            fps = 60 #    ...скорость игры возвращается к первоначальной
            mushroom.rect.left = SC_W #    ...мухомор возвращается на начальную позицию
            game_over = False #    ...возобновляем игру
    screen.blit(BG, (0, 0)) #    Добавляем фон на экран в координатах (0, 0) - верхний левый угол
    screen.blit(player.sprite, player.rect) #    Отображаем спрайт игрока на экране
    screen.blit(mushroom.sprite, mushroom.rect) #    Отображаем спрайт мухомора на экране
    score_text = font.render(f"СЧЁТ: {score}", 1, pygame.Color('blue')) #    Задаём параметры отображения счёта
    screen.blit(score_text, (5, 5)) #    Отображаем счёт на экране
    if game_over: #    Если игрок проиграл, ТО...
        game_over_text = font.render('КОНЕЦ ИГРЫ', True, (180, 0, 0)) #    Задаём параметры надписи 'КОНЕЦ ИГРЫ'
        screen.blit(game_over_text, (SC_W // 2, SC_H // 2)) #    Отображаем текст на экране
    pygame.display.update() #    Обновляем экран
    clock.tick(fps) #    Частота выполнения цикла за одну секунду
pygame.quit() #    Закрыть Pygame
