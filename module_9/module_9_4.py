from random import choice

first = "Мама мыла раму"
second = "Рамена мало было"
print(list(map(lambda x, y: x == y, first, second)))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, "w", encoding="utf-8") as f:
            for data in data_set:
                f.write(f"{data}\n")

    return write_everything


write = get_advanced_writer("example.txt")
write("Это строчка", ["А", "это", "уже", "число", 5, "в", "списке"])


class MysticBall:
    def __init__(self, *args):
        self.args = args

    def __call__(self, *args, **kwargs):
        return choice(self.args)


first_ball = MysticBall("Да", "Нет", "Наверное")
print(first_ball())
print(first_ball())
print(first_ball())
