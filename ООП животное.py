class Animal:
    def __init__(self, speed, jump_height, weight):
        self.speed = speed
        self.jump_height = jump_height
        self.weight = weight
    def info(self):
        print("Скорость:", self.speed, "км/час")
        print("Высота прыжка:", self.jump_height, "м")
        print("Вес",self.weight, "кг") 
    def run(self):
        print("Животное бежит!")
    def jump(self):
        print("Животное прыгает!")
rabbit = Animal(50, 4.5, 5)
print("Свойства гепарда:")
rabbit.info()
rabbit.run()
rabbit.jump()

