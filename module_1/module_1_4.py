my_string = input("Введите что-нибудь: ")
print("Введено символов:", len(my_string))
print("Верхний регистр", my_string.upper())
print("Нижний регистр", my_string.lower())
my_string = my_string.replace(" ", "")
print("Измененная строка без пробелов:", my_string)
print("Первый символ:", my_string[0])
print("Последний символ:", my_string[-1])