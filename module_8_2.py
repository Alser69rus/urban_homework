def personal_sum(numbers) -> tuple[float, int]:
    result: float = 0
    incorrect_data: int = 0
    for v in numbers:
        try:
            result += v
        except TypeError:
            print(f"Некорректный тип данных для подсчёта суммы - {v}, type: {type(v)}")
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers) -> float | None:
    result = None
    try:
        sum_num, incorrect = personal_sum(numbers)
        result = sum_num / (len(numbers) - incorrect)
    except ZeroDivisionError:
        result = 0
    except TypeError:
        print("В numbers записан некорректный тип данных")
    finally:
        return result


if __name__ == "__main__":
    # Строка перебирается, но каждый символ - строковый тип
    print(f'Результат 1: {calculate_average("1, 2, 3")}')
    # Учитываются только 1 и 3
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
    # Передана не коллекция
    print(f"Результат 3: {calculate_average(567)}")
    # Всё должно работать
    print(f"Результат 4: {calculate_average([42, 15, 36, 13])}")
