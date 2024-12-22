import threading
from random import randint
from threading import Lock
from time import sleep


class Bank:
    def __init__(self, balance: int = 0):
        self.balance = balance
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            cash = randint(50, 500)
            self.balance += cash
            print(f"Пополнение: {cash}. Баланс: {self.balance}")

            if self.lock.locked() and self.balance >= 500:
                self.lock.release()

            sleep(0.001)

    def take(self):
        for _ in range(100):
            cash = randint(50, 500)
            print(f"Запрос на {cash}")

            if cash <= self.balance:
                self.balance -= cash
                print(f"Снятие: {cash}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire(timeout=0.001)

            sleep(0.001)


if __name__ == "__main__":
    bk = Bank()
    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))
    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(f"Итоговый баланс: {bk.balance}")
