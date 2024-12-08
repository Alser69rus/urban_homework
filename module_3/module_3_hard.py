def calculate_structure_sum(value) -> int:
    if isinstance(value, str):
        return len(value)
    elif isinstance(value, int):
        return value
    elif isinstance(value, list) or isinstance(value, set) or isinstance(value, tuple):
        return sum([calculate_structure_sum(v) for v in value])
    elif isinstance(value, dict):
        return calculate_structure_sum(list(value.values()) + list(value.keys()))
    else:
        print(f"Неизвестный {type(value)}, значение {value}")
        return 0


if __name__ == "__main__":
    data_structure = [
        [1, 2, 3],
        {"a": 4, "b": 5},
        (6, {"cube": 7, "drum": 8}),
        "Hello",
        ((), [{(2, "Urban", ("Urban2", 35))}]),
    ]
    result = calculate_structure_sum(data_structure)
    print(result)
