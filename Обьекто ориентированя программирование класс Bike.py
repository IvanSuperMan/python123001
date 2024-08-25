class Bike:
    def __init__(self, model, color, top_speed):
        self.model = model
        self.color = color
        self.top_speed = top_speed

    def beep(self):
        print(f'Звук модели{self.model} - "бип"')
    #def __str__(self):
        #return(f'Этот обьект является зкземляром класс мотоциклов')
    
"""bike1 = Bike()
print(bike1.model)
bike1.beep()

bike2= Bike()
print(bike1.model)
bike1.beep()

bike3= Bike()
bike3.model = 'BMW'
bike3.top_speed = 350
print(f'Модель {bike3.model}, цвет {bike3.color}, максимальная скорость {bike3.top_speed} км/ч.')
bike3.beep()"""

bike1 = Bike('Yamaha','синий', 300)
bike2 = Bike('Урал','зеленый', 120)
print(f'Модель {bike1.model}, цвет {bike1.color}, максимальная скорость {bike1.top_speed} км/ч.')
bike1.beep()
print(f'Модель {bike2.model}, цвет {bike2.color}, максимальная скорость {bike2.top_speed} км/ч.')
bike2.beep()
print(bike1.__doc__)
print(bike2.__doc__)


