import math

import requests
import pandas
import matplotlib.pyplot as plt
import numpy
from PIL import Image, ImageOps


def request_example():
    print("Пример для requests")
    print("Выводим текст программы из GitHub")
    print("*" * 80)
    print("Попытка соединения с сервером")
    r = requests.get(
        url="https://raw.githubusercontent.com/Alser69rus/urban_homework/refs/heads/master/module_10/module_10_1.py"
    )
    if r.status_code == 200:
        print("Данные получены")
        print(f'Текст программы: \n"""\n{r.text}\n"""')
    else:
        print(f"Что-то пошло не так. Код ошибки {r.status_code}")
    print("*" * 80)
    print()


def pandas_example():
    print("Пример для pandas")
    print("Анализ данных из файла")
    print("*" * 80)

    ser = pandas.Series(
        {
            "0": -1,
            "1": 0,
            "2": 3,
            "3": 8,
            "4": 15,
            "5": 24,
            "-1": 0,
            "-2": 3,
            "-3": 8,
            "-4": 15,
            "-5": 24,
        }
    )
    ser.to_excel("parabola.xlsx")

    fr = pandas.read_excel(
        "parabola.xlsx",
        "Sheet1",
        index_col=0,
    )
    fr = fr.sort_index()
    print("Количество данных для каждого значения")
    print(fr.value_counts().sort_index())

    print("Построение графика. (Для продолжения необходимо его закрыть)")
    fr.plot()
    plt.show()


def numpy_example():
    print("Решение системы линейных уравнений при помощи numpy")
    print("*" * 80)
    print("Дано:")
    print(
        "Бита и мяч стоят 1000 руб. Бита на 800 руб. дороже мяча. Найти цену биты и мяча"
    )
    print("Решение:")
    print("x1 + x2 = 1000")
    print("x1 - x2 = 800")
    print("Ответ:")
    a = numpy.array([[1, 1], [1, -1]])
    b = numpy.array([1000, 800])
    x = numpy.linalg.solve(a, b)
    res = zip(["Бита", "Мяч"], x.tolist())
    print(f'{"Предмет": ^20}{"Цена, руб.": ^20}')
    for it, pr in res:
        print(f"{it: <20}{pr: ^20.2f}")
    print("*" * 80)
    print()


def matplotlib_example():
    print("График синусоиды matplotlib")
    print("*" * 80)
    fig, ax = plt.subplots()
    x = [x * math.pi / 180 for x in range(360)]
    y = [math.sin(x * math.pi / 180) for x in range(360)]
    print("Построение графика. (Для продолжения необходимо его закрыть)")
    ax.plot(x, y)
    plt.show()
    print("*" * 80)
    print()


def pillow_example():
    im = Image.open("in_image.jpg")
    im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    im.thumbnail((256, 256))
    ImageOps.contain(im, (256, 256)).save("icon.ico")
    im.save("out_image.png")


if __name__ == "__main__":
    request_example()
    pandas_example()
    numpy_example()
    matplotlib_example()
    pillow_example()
