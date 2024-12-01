class Vehicle:
    __COLOR_VARIANTS = ["blue", "red", "green", "black", "white"]

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power

    def get_model(self) -> str:
        return self.__model

    def get_horsepower(self) -> int:
        return self.__engine_power

    def get_color(self) -> str:
        return self.__color

    def print_info(self):
        print(f"Модель: {self.get_model()}")
        print(f"Мощность двигателя: {self.get_horsepower()}")
        print(f"Цвет: {self.get_color()}")
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str):
        if new_color.lower() in [color.lower() for color in self.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__PASSENGERS_LIMIT = 5


if __name__ == "__main__":
    # Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    vehicle1 = Sedan("Fedos", "Toyota Mark II", "blue", 500)

    # Изначальные свойства
    vehicle1.print_info()

    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color("Pink")
    vehicle1.set_color("BLACK")
    vehicle1.owner = "Vasyok"

    # Проверяем что поменялось
    vehicle1.print_info()
