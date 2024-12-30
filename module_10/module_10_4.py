import queue
import random
import time
from threading import Thread


class Table:
    def __init__(self, number: int):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self):
        delay = random.randint(3, 10)
        time.sleep(delay)


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            table = self.get_free_table()
            if table is None:
                self.guest_takes_the_queue(guest)
            else:
                self.seat_the_guest_at_the_table(guest, table)

    def discuss_guests(self):
        while self.there_are_more_guests():
            self.cleaning_free_table()
            self.discuss_next_guests_in_queue()
            time.sleep(1)

    def get_free_table(self):
        free_tables = [table for table in self.tables if table.guest is None]
        if free_tables:
            return free_tables[0]
        return None

    def guest_takes_the_queue(self, guest):
        self.queue.put(guest)
        print(f"{guest.name} в очереди")

    def seat_the_guest_at_the_table(self, guest, table):
        table.guest = guest
        guest.start()
        print(f"{guest.name} сел(-а) за стол номер {table.number}")

    def there_are_more_guests(self) -> bool:
        if not self.queue.empty():
            return True
        if any(self.occupied_tables()):
            return True
        return False

    def occupied_tables(self):
        return [table for table in self.tables if table.guest is not None]

    def cleaning_free_table(self):
        dirty_table = [
            table for table in self.occupied_tables() if not table.guest.is_alive()
        ]
        for table in dirty_table:
            print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
            print(f"Стол номер {table.number} свободен")
            table.guest = None

    def discuss_next_guests_in_queue(self):
        while not self.queue.empty():
            table = self.get_free_table()
            if table is None:
                return
            guest = self.queue.get()
            print(
                f"{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}"
            )
            self.seat_the_guest_at_the_table(guest, table)


if __name__ == "__main__":
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        "Maria",
        "Oleg",
        "Vakhtang",
        "Sergey",
        "Darya",
        "Arman",
        "Vitoria",
        "Nikita",
        "Galina",
        "Pavel",
        "Ilya",
        "Alexandra",
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()
