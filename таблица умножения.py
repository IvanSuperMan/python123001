number =int(input("Ваберите число от 1-10 "))
while number > 10:
    print("Введите положительное число от 1 до 10")
    number =int(input("Ваберите число от 1-10 "))
for i in range(11):
    print(number, "*", i, "=", number*i)
print('END')
