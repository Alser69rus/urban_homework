def get_multiplied_digits(number: int) -> int:
    str_number = str(number)
    first = int(str_number[:1])
    if len(str_number) == 1:
        return first
    if first == 0:
        first = 1
    return first * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(40203)
print(result)
