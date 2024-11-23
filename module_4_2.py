from math import sin
from datetime import datetime

print(sin(0))
print(datetime.now())


def test_function():
    def inner_function():
        print("Я, inner_function, в области видимости функции test_function")

    inner_function()


if __name__ == "__main__":
    test_function()

    try:
        inner_function()
    except Exception as e:
        print("Функция inner_function не видна из глобальной области видимости")
