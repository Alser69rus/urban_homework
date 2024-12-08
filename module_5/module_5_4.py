class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
            return
        for floor in range(new_floor):
            print(floor + 1)

    def __len__(self) -> int:
        return self.number_of_floors

    def __str__(self) -> str:
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other
        else:
            raise TypeError

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other
        else:
            raise TypeError

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other
        else:
            raise TypeError

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other
        else:
            raise TypeError

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other
        else:
            raise TypeError

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other
        else:
            raise TypeError

    def __add__(self, other):
        if isinstance(other, House):
            self.number_of_floors += other.number_of_floors
            return self
        elif isinstance(other, int):
            self.number_of_floors += other
            return self
        else:
            raise TypeError

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, House):
            self.number_of_floors -= other.number_of_floors
            return self
        elif isinstance(other, int):
            self.number_of_floors -= other
            return self
        else:
            raise TypeError

    def __rsub__(self, other):
        return self.__sub__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, House):
            self.number_of_floors *= other.number_of_floors
            return self
        elif isinstance(other, int):
            self.number_of_floors *= other
            return self
        else:
            raise TypeError

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, House):
            self.number_of_floors /= other.number_of_floors
            return self
        elif isinstance(other, int):
            self.number_of_floors /= other
            return self
        else:
            raise TypeError

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __itruediv__(self, other):
        return self.__truediv__(other)


if __name__ == "__main__":
    h1 = House("ЖК Эльбрус", 10)
    print(House.houses_history)
    h2 = House("ЖК Акация", 20)
    print(House.houses_history)
    h3 = House("ЖК Матрёшки", 20)
    print(House.houses_history)

    # Удаление объектов
    del h2
    del h3
    print(House.houses_history)
