import pygame, random # Импортируем модуль pygame / Импортируем модуль random
WINDOW = (900, 700) # Ширина и высота окна
fps = 60 # Число кадров в секунду
CENTER = WINDOW[0]/2, WINDOW[1]/2 # Рассчитываем центр экрана (необходимо для будущего шарика)
pygame.init() # Инициализируем pygame
clock = pygame.time.Clock() # 01 Создаём часы
window = pygame.display.set_mode((WINDOW[0], WINDOW[1])) # Создаём окно
pygame.display.set_caption('Арканоид') # Заголовок окна
background = pygame.image.load("background.png").convert() # Фоновое изображение (метод convert() оптимизирует формат изображения и ускоряет рисование)
background = pygame.transform.scale(background, (WINDOW[0], WINDOW[1])) # Изменение размеров фона под размер окна
class Slab: # Общий класс для платформы и блоков
    def __init__(self, x, y, width, height, speed=0): # Инициализируем основные параметры (координаты XY, ширина, высота, скорость (по умолчанию равна 0)
        self.x = x # Координата по оси X
        self.y = y # Координата по оси Y
        self.slab_w = width # Ширина
        self.slab_h = height # Высота
        self.slab_speed = speed # Скорость
        self.slab = pygame.Rect(self.x, self.y, self.slab_w, self.slab_h) # Создаём объект Rect (четырёхугольник)
    def move(self, keys): # Метод движения платформы (получает на вход зажатую клавишу)
        if keys[pygame.K_LEFT] and self.slab.left > 0: # Если зажата левая клавиша и левый край платформы не вышел за края экрана, ТО...
            self.slab.left -= self.slab_speed # ...перемещаем платформу влево
        elif keys[pygame.K_RIGHT] and self.slab.right < WINDOW[0]: # Если зажата правая клавиша и правый край платформы не вышел за края экрана, ТО...
            self.slab.right += self.slab_speed # ...перемещаем платформу вправо
class Ball: # Класс шарика
    def __init__(self): #Инициализация шарика
        self.ball_radius = 20 # Радиус шарика
        self.ball_speed = 6 # Скорость шарика
        self.ball = pygame.Rect(CENTER[0], CENTER[1], self.ball_radius * 2, self.ball_radius * 2) # Объект Rect для вписывания в него шарика
        self.bx = random.choice([-1, 1]) # Коэффициент направления движения шарика по оси X (случайное направление влево или вправо)
        self.by = -1 # 03 Коэффициент направления движения шарика по оси Y
    def move(self): # Метод движение шарика
        self.ball.x += self.ball_speed * self.bx # По координате x
        self.ball.y += self.ball_speed * self.by # По координате y
        # Если расстояние от центра шарика по координате X до левого или правого края экрана будет меньше его радиуса, ТО...
        if self.ball.centerx < self.ball_radius or self.ball.centerx > WINDOW[0] - self.ball_radius:
            self.bx = -self.bx # ...меняем направление на противоположное
        if self.ball.centery < self.ball_radius: # Если расстояние от центра шарика по координате Y до верхней границы экрана будет меньше его радиуса, ТО...
            self.by = -self.by # ...меняем направление на противоположное
def detect_collision(bx, by, ball, rect): # Вычисляем коллизии. Если шарик столкнулся с блоком ТО изменить его траекторию
    if bx > 0: #    Если шарик движется вправо, ТО...6
        delta_x = ball.right - rect.left #    ...рассчитать дельту X
    else: #    Если шарик движется влево, ТО...
        delta_x = rect.right - ball.left #    ...рассчитать дельту X
    if by > 0: #    Если шарик движется вниз, ТО...
        delta_y = ball.bottom - rect.top #    ...рассчитать дельту Y
    else: #    Если шарик движется вверх, ТО...
        delta_y = rect.bottom - ball.top #    ...рассчитать дельту Y
    if delta_x > delta_y: #    Если delta_x > delta_y, ТО...
        by = -by #    ...меняем направление шарика по оси Y
    elif delta_y > delta_x: #    Если delta_y > delta_x, ТО...
        bx = -bx #    ...меняем направление шарика по оси X
    return bx, by #    Функция возвращает новое направление движения шарика по осям XY
platform = Slab(WINDOW[0] // 2 - 150, WINDOW[1] - 60, 300, 30, 15) # 02 Создаём объект платформы (координаты XY, ширина, высота, скорость)
ball = Ball() # 03 Создаём объект шарик
block_box = [Slab(x, y, 100, 30).slab for y in range(20, 161, 40) for x in range(15, 786, 110)] #    Создаём список с блоками 4 ряда по 8 штук
while True: #    Основной игровой цикл (обработка событий, обновление позиций объектов на основе событий, рисование объектов в новых позициях)
    for event in pygame.event.get(): #    Проверка очереди событий на нажатие клавиш
        if event.type == pygame.QUIT: #    Если был нажат крестик справа вверху, ТО...
            exit() #    ...выход из игры
        elif event.type == pygame.KEYDOWN: #    Проверка события, нажата ли клавиша
            if event.key == pygame.K_ESCAPE: # Если была нажата клавиша Esc, ТО...
                exit() #    ...выход из игры
    platform.move(pygame.key.get_pressed()) #    Вызываем метод движения платформы и передаём ему полученный список зажатых клавиш в виде словаря
    ball.move() #    Вызываем метод описывающий движение шарика
    if ball.ball.colliderect(platform.slab): #    Метод colliderect возвращает значение True или False в зависимости от того столкнулись прямоугольники или нет
        #ball.by = -ball.by #    ...меняем направление движения шарика
        ball.bx, ball.by = detect_collision(ball.bx, ball.by, ball.ball, platform.slab) #    ...меняем направление движения шарика с помощью функции
    hit_index = ball.ball.collidelist(block_box) #    Метод collidelist вернёт нам индекс блока с которым есть столкновение или -1 если столкновения не было
    if hit_index != -1: #    Если было столкновение (равно -1, если столкновения не было)
        ball.bx, ball.by = detect_collision(ball.bx, ball.by, ball.ball, block_box[hit_index]) #    Меняем направление движения шарика
        block_box.pop(hit_index) #    Убираем блок из списка (удаляем координаты блока из списка)
        fps += 2 #    При каждом убранном блоке количество кадров увеличивается на 2 (т.е. растёт скорость игры)
    window.blit(background, (0, 0)) #    Добавляем фон на экран в координаты (0, 0) - верхний левый угол
    pygame.draw.rect(window, pygame.Color("red"), platform.slab) #    Рисуем платформу (поверхность, цвет, объект)
    pygame.draw.circle(window, pygame.Color("blue"), ball.ball.center, ball.ball_radius) #    Рисуем шарик (поверхность, цвет, центр, радиус)
    [pygame.draw.rect(window, pygame.Color('orange'), block) for block in block_box] #    Рисуем блоки на экране
    pygame.display.update() #    Обновляем экран
    clock.tick(fps) #    Частота выполнения цикла за одну секунду
pygame.quit() #    Закрыть Pygame
