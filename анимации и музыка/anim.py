import pygame #   Импортируем модуль pygame
pygame.init() #   Инициализируем pygame
WIN_SIZE = (600, 400) #   Задаём ширину и высоту окна
FPS = 10 #   Число кадров в секунду
steps = pygame.mixer.Sound('sounds/step.ogg') #   Загружаем звук шага для персонажа
class MySprite(): #   Класс для спрайта
    def __init__(self): #   Инициализация спрайта
        self.images = [] #   Создаём список для хранения всех изображений для анимации
        self.images.append(pygame.image.load('images/player_stand.png')) #   Загружаем изображение (персонаж стоит)
        self.images.append(pygame.image.load('images/player_walk1.png')) #   Загружаем изображение (персонаж шагает)
        self.images.append(pygame.image.load('images/player_walk2.png')) #   Загружаем изображение (персонаж шагает)
        self.move_index = 0 #   Переменная для отображения счётчика изображений анимации
        self.image = self.images[self.move_index] #   Переменная для текущего изображения из анимации
        self.rect = self.image.get_rect() #   Получаем четырёхугольник вокруг спрайта
        self.rect.y = 100 #   Задаём координату расположения спрайта по оси Y
        self.move = False #   Переменная для активации анимации
        self.speed = 7 #   Скорость передвижения спрайта
        self.left = False #   Поворот персонажа влево (изначально спрайт смотрит вправо)
    def update(self, keys): #   Метод для отображения анимации на экране /   добавляем параметр keys для получения зажатых клавиш
        if keys[pygame.K_LEFT]: #   Если зажата левая клавиша, ТО...
            self.move = True #   ...спрайт анимирован
            self.left = True #   ...персонаж смотрит влево
            self.rect.x -= self.speed #   ...перемещаем спрайт влево
        elif keys[pygame.K_RIGHT]: #   Если зажата правая клавиша, ТО...
            self.move = True #   ...спрайт анимирован
            self.left = False #   ...персонаж НЕ смотрит влево
            self.rect.x += self.speed #   ...перемещаем спрайт вправо
        else: #   ИНАЧЕ...
            self.move = False #   ...спрайт НЕ анимирован
            steps.stop() #   Останавливаем воспроизведение звука шага
        if self.move: #   Если нажата клавиша движения спрайта, ТО...
            self.move_index += 1 #   Увеличиваем счётчик на 1
            if self.move_index > 2: #   Если счётчик больше двух (так, как у нас две картинки с анимацией ходьбы), ТО...
                self.move_index = 1 #   ...переходим к первому изображению в списке
                self.image = self.images[self.move_index] #   Задаём изображение для отображения в анимации
        else: #   ИНАЧЕ...
            self.image = self.images[0] #   ...персонаж стоит
        if self.left: #   Если персонаж смотрит влево, ТО...
            self.image = pygame.transform.flip(self.image, True, False) #   ...отразить изображение по горизонтали
        if self.move_index == 2 and self.move: #   Если изображение текущего спрайта равно 2 И нажата клавиша движения, ТО...
            steps.play(-1) #   ...воспроизводим звук шага бесконечное число раз
def main(): #   Создаём основную функцию
    screen = pygame.display.set_mode(WIN_SIZE) #   Создаём окно
    clock = pygame.time.Clock() #   Создаём часы
    my_sprite = MySprite() #   Создаём объект персонажа
    pygame.mixer.music.load("sounds/music.mp3") #   Добавляем фоновую музыку
    pygame.mixer.music.play(-1) #   Бесконечное воспроизведение музыки
    pygame.mixer.music.set_volume(0.2) #   Громкость 20% от реальной
    while True: #   Основной игровой цикл
        for event in pygame.event.get(): #   Проверка очереди событий на нажатие клавиш
            if event.type == pygame.QUIT: #   Если был нажат крестик справа вверху, ТО...
                exit() #   Выход из игры
        screen.fill(pygame.Color(255, 255, 255)) #   Задаём цвет фона окна
        #   Вызываем метод отображения анимации /   Передаём в метод список зажатых клавиш в виде словаря
        my_sprite.update(pygame.key.get_pressed())
        screen.blit(my_sprite.image, my_sprite.rect) #   Отображаем спрайт игрока на экране
        pygame.display.update() #   Обновляем экран
        clock.tick(FPS) #   Частота выполнения цикла за одну секунду
if __name__ == '__main__': #   Условие запуска игры
    main() #   Запускаем основной цикл
