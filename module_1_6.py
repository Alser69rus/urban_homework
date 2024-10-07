my_dict = {"Саша": 1981, "Юра": 1976, "Лиля": 1981}
print("Словарь:", my_dict)
print("Существующее значение (Саша):", my_dict["Саша"])
print("Отсутствующее значение (Маша):", my_dict.get("Маша", "не найдено"))
my_dict["Оля"] = 1983
my_dict["Ася"] = 2010
value = my_dict.pop("Саша")
print("Измененный словарь:", my_dict)
print("Удаленное значение (Саша):", value)

my_set = {0, 1, 2, 3, True, False, "string"}
print("Множество:", my_set)
my_set.update({3.14, 2.71})
my_set.remove(0)
print("Измененное множество:", my_set)
