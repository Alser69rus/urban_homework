my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

i = 0
while i < len(my_list):
    value = my_list[i]
    if value < 0:
        break
    print(value)
    i += 1
