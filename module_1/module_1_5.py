immutable_var = 1, 2, "a", "b"
print("Immutable tuple:", immutable_var)
mutable_list = [1, 2, "a", "b", True]
mutable_list[4] = "Modified"
print("Mutable list:", mutable_list)

try:
    immutable_var[0] = True
    print("Кортеж можно изменить")
except Exception as e:
    print("Кортеж менять нельзя!")
    print("Будет ошибка выполнения:", e)
