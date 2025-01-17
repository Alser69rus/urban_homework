import logging
import unittest

logging.basicConfig(
    level=logging.INFO,
    filemode="w",
    filename="tests.log",
    encoding="utf8",
    format="%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
)


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(
                f"Имя может быть только строкой, передано {type(name).__name__}"
            )
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f"Скорость не может быть отрицательной, сейчас {speed}")

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):

        try:
            runner = Runner("Alex", -5)
            logging.info("test_walk выполнен успешно")
        except Exception as e:
            logging.warning(f"Неверная скорость для Runner в методе walk. {e}")

        runner = Runner("Alex", 5)
        self.assertEqual(runner.distance, 0, "Начальная дистанция не равна 0")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50, "Дистанция прогулки отлична от 50")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            runner = Runner(2)
            logging.info('"test_run" выполнен успешно')
        except Exception as e:
            logging.warning(f"Неверный тип данных для объекта Runner. {e}")

        runner = Runner("2", 5)
        self.assertEqual(runner.distance, 0, "Начальная дистанция не равна 0")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100, "Дистанция пробега не равна 100")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        walker = Runner("Moon")
        runner = Runner("Shadow")
        self.assertEqual(walker.distance, 0)
        self.assertEqual(runner.distance, 0)
        for _ in range(10):
            walker.walk()
            runner.run()
        self.assertNotEqual(runner.distance, walker.distance)


if __name__ == "__main__":
    unittest.main()
