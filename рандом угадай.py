print ("Программа угадай число")
secret_number = 7
while True:
    number = int(input ("Введите число "))
    if number == secret_number:
        print("Вы угадали число")
        break
    if number != secret_number:
        print("Неверно")
                
        
        
