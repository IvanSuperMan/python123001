import pygame # Импортируем библиотеку Pygame

width, height = 300, 300 #Ширина экрана, # Высота экрана 
screen = pygame.display.set_mode((width, height))  # Создание экрана
pygame.display.set_caption("Tic Tac Toe") # Название экрана

pygame.init() # Инициализация модуля pygame

white, black = (255, 255, 255), (0, 0, 0) # Создаем цвета, которые нам предстоит использоват
fps_clock = pygame.time.Clock() # Создание объекта для отслеживания времени
fps = 30 # Количество кадров в секунду

running = True
while running:
    for event in pygame.event.get(): # event принимает в себя клавиши, что были нажаты пользователем
        if event.type == pygame.QUIT: # Выход из цикла при нажатии на кнопку выход
            running = False
            
    screen.fill(black) # заливка экрана
    pygame.display.flip() # переворот экрана
    fps_clock.tick(fps) # ограничение кадров в секунду

pygame.quit() # завершение работы pygame
