import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner("Alex")
        self.assertEqual(runner.distance, 0, "Начальная дистанция не равна 0")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50, "Дистанция прогулки отлична от 50")

    def test_run(self):
        runner = Runner("Olga")
        self.assertEqual(runner.distance, 0, "Начальная дистанция не равна 0")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100, "Дистанция пробега не равна 100")

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
