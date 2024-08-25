print("Калькулятор\n")
print("Выберете число\n")
first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
print("Выберете знак\n")
print ("Буквы, знаки кроме нижних ставить нельзя!")
print("+ - * :\n")
ask = input ("Писать сюда: ")
match ask:
    case "+" :
        print("Cумма чисел:", first_number + second_number)
    case "-" :
        print("Разность чисел:", first_number - second_number)
    case "*" :
        print("Произведение чисел:", first_number * second_number)
    case "/" :
        print("Деление чисел:", first_number / second_number)
input (".")
