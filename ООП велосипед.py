class Bicycle:
    def __init__(self, wheel, color, motor):
        self.wheel = wheel
        self.color = color
        self.motor = motor

    def brake(self):
        print(f'Велосипед остановился')
        
class Kids(Bicycle):
    def __init__(self, wheel, color, motor, proprietor):
        super().__init__(wheel, color, motor)
        self.proprietor = proprietor

    def owner(self):
        print(f'Владелец велосипеда {self.proprietor}')

bicycle_kids = Kids(2, 'красный', None, 'Дима')
print(bicycle_kids.wheel)
print(bicycle_kids.color)
print(bicycle_kids.motor)
print(bicycle_kids.proprietor)
bicycle_kids.brake()
bicycle_kids.owner()
