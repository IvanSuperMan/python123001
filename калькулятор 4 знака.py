print("Калькулятор\n")
print("Выберете знак\n")
print("+ - * :\n")
ask = input ("Писать сюда: ")
first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
if ask == "+":
    print("\nСумма чисел:", first_number + second_number)
if ask == "-":
    print("\nРазность чисел:", first_number - second_number)
if ask == "*":
    print("\nПроизведение чисел:", first_number * second_number)
if ask == ":":
    print("\nДеление чисел:", first_number / second_number)
input("")

