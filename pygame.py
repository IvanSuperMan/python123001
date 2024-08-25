# pip install pygame
import pygame  # Импортируем модуль pygame

pygame.init()  # Инициализация pygame
width = 640  # Ширина окна
height = 480  # Высота окна
window = pygame.display.set_mode((width, height))  # Создаём окно

FPS = 30  # Частота кадров
clock = pygame.time.Clock()  # Создаём часы

ufo = pygame.image.load('ufo.png')  # Подгружаем спрайт с НЛО
ufo_rect = ufo.get_rect()  # Получаем четырёхугольник вокруг спрайта
speed = 10  # Скорость движения НЛО

frame = pygame.Rect(400, 200, 80, 80)  # Создаём рамку (x, y, ширина, высота)
box = pygame.Rect(200, 200, 80, 80)  # Создаём квадрат (x, y, ширина, высота)
ball = pygame.Rect(width//2, height-100, 20, 20)  # Создаём квадрат для шарика (x, y, ширина, высота)
ball_x = 1  # Направление движения шарика

def ball_move():  # Функция движения шарика
    global ball_x  # Делаем переменную глобальной
    ball.x += speed * 2 * ball_x  # Движение шарика

    if ball.right >= width or ball.left <= 0:  # Если шарик столкнулся с краями окна, ТО...
        ball_x = -ball_x  # ...меняем направление движения

font = pygame.font.SysFont('Arial', 20, bold=True)  # Создаём шрифт


while True:  # Основной игровой цикл
    for event in pygame.event.get():  # Проверка очереди событий на нажатие клавиш
        if event.type == pygame.QUIT:  # Если был нажат крестик справа вверху, ТО...
            exit()  # ...закрыть программу

    key = pygame.key.get_pressed()  # Получаем состояние клавиш
    if key[pygame.K_UP]:  # Если зажата стрелочка вверх, ТО...
        ufo_rect.y -= speed  # ...перемещаем спрайт НЛО вверх
    elif key[pygame.K_DOWN] and ufo_rect.bottom < height:  # Если зажата стрелочка вниз и спрайт не вышел за нижний край окна, ТО...
        ufo_rect.y += speed  # ...перемещаем спрайт НЛО вниз
    elif key[pygame.K_LEFT]:  # Если зажата стрелочка влево, ТО...
        ufo_rect.x -= speed  # ...перемещаем спрайт НЛО влево
    elif key[pygame.K_RIGHT]:  # Если зажата стрелочка вправо, ТО...
        ufo_rect.x += speed  # ...перемещаем спрайт НЛО вправо

    ball_move()  # Запускаем функцию движения шарика


    window.fill((95,143,132))  # Фон окна
    pygame.draw.rect(window, (0, 0, 255), box)  # Отображаем синий квадрат в окне
    window.blit(ufo, ufo_rect)  # Отображаем спрайт в окне

    if ufo_rect.colliderect(frame) or ufo_rect.colliderect(box):  # Если спрайт пересёк квадрат или рамку, ТО...
        pygame.draw.rect(window, (255, 0, 0), ufo_rect, 8)  # ...отображаем красную рамку вокруг спрайта

    pygame.draw.rect(window, (0, 255, 0), frame, 10)  # Отображаем рамку в окне
    pygame.draw.circle(window, (237, 118, 14), ball.center, 20)  # Отображаем шарик в окне


    coordinates_text = font.render(f"Координаты: X {ufo_rect.x}, Y {ufo_rect.y}", 1, pygame.Color('yellow'))  # Задаём параметры отображения текста
    window.blit(coordinates_text, (5, 5))  # Отображаем текст


    pygame.display.update()  # Обновляем экран
    clock.tick(FPS)  # Частота выполнения цикла за одну секунду

pygame.quit()  # Закрыть Pygame
