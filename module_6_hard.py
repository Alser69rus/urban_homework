import math


class Figure:
    side_count: int = 0

    def __init__(self, color: tuple[int, int, int], *sides, filled: bool = False):
        self.__sides: list[int] = [1] * self.side_count
        self.set_sides(*sides)
        self.__color: list[int] = [0, 0, 0]
        self.set_color(*color)
        self.filled: bool = filled

    def get_color(self) -> list[int]:
        return self.__color

    def __is_valid_color(self, r: int, g: int, b: int) -> bool:
        return all([0 <= r <= 255, 0 <= g <= 255, 0 <= b <= 255])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides) -> bool:
        if len(sides) != self.side_count:
            return False
        if all([isinstance(side, int) and side > 0 for side in sides]):
            return True
        return False

    def get_sides(self) -> list[int]:
        return list(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    side_count = 1

    def __init__(self, color: tuple[int, int, int], *sides, filled: bool = False):
        super().__init__(color, *sides, filled=filled)
        self.__update_radius()

    def __update_radius(self):
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.__update_radius()

    def get_square(self) -> float:
        return math.pi * self.__radius**2


class Triangle(Figure):
    side_count = 3

    def get_square(self) -> float:
        p = len(self) / 2
        a, b, c = self.get_sides()
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    side_count = 12

    def __init__(self, color: tuple[int, int, int], *sides, filled: bool = False):
        super().__init__(color, *sides, filled=filled)
        self.set_sides(*sides)

    def __is_valid_sides(self, *sides) -> bool:
        if len(sides) != 1:
            return False
        if isinstance(sides[0], int) and sides[0] > 0:
            return True
        return False

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            side = new_sides[0]
            sides = [side] * self.side_count
            super().set_sides(*sides)

    def get_volume(self) -> float:
        return self.get_sides()[0] ** 3


if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())

    # Проверка площади треугольника:
    tr = Triangle((0, 0, 0), 3, 4, 5)
    print(tr.get_square())
