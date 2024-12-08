def custom_write(file_name: str, strings: list[str]):
    with open(file_name, "w", encoding="utf-8") as f:
        file_info = {}
        for i, s in enumerate(strings):
            pos = f.tell()
            file_info[(i + 1, pos)] = s
            f.write(f"{s}\n")
    return file_info


if __name__ == "__main__":
    info = [
        "Text for tell.",
        "Используйте кодировку utf-8.",
        "Because there are 2 languages!",
        "Спасибо!",
    ]

    result = custom_write("test.txt", info)
    for elem in result.items():
        print(elem)
