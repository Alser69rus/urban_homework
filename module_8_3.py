class Car:
    def __init__(self, model: str, vin: int, numbers: str):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_vin(self, vin_number: int) -> bool:
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип vin номер")
        if 1_000_000 <= vin_number <= 9_999_999:
            return True
        raise IncorrectVinNumber("Неверный диапазон для vin номера")

    def __is_valid_numbers(self, numbers: str) -> bool:
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        if len(numbers) == 6:
            return True
        raise IncorrectCarNumbers("Неверная длина номера")


class IncorrectVinNumber(Exception):
    def __init__(self, message: str):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message: str):
        self.message = message


if __name__=='__main__':
    try:
        first = Car('Model1', 1000000, 'f123dj')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')