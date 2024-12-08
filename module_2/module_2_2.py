first = int(input("Введите первое число:"))
second = int(input("Введите второе число:"))
third = int(input("Введите третье число:"))

if first == second and first == third:
    print("Три одинаковых числа", 3)
elif first == second or first == third or second == third:
    print("Два одинаковых числа", 2)
else:
    print("Одинаковых чисел нет", 0)
