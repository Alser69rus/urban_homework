import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        enemies = 100
        days = 0
        while enemies > 0:
            time.sleep(1)
            enemies -= self.power
            days += 1
            print(f"{self.name} сражается {days}..., осталось {enemies} воинов.")

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")
        print()


if __name__ == "__main__":
    first_knight = Knight("Sir Lancelot", 10)
    second_knight = Knight("Sir Galahad", 20)
    first_knight.start()
    second_knight.start()
    first_knight.join()
    second_knight.join()
