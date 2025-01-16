import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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
            _ = [participant.run() for participant in self.participants]
            finishers_in_tour = [
                participant
                for participant in self.participants
                if participant.distance >= self.full_distance
            ]
            finishers_in_tour.sort(key=lambda x: x.distance, reverse=True)
            for participant in finishers_in_tour:
                finishers[place] = participant
                place += 1
                self.participants.remove(participant)
        return finishers


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.usein = Runner("Усэйн", 10)
        self.andrei = Runner("Андрей", 9)
        self.nik = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for tour in cls.all_results:
            for place, runner in tour.items():
                print(f"{place}:{runner} ", end="")
            print()

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_1(self):
        t = Tournament(90, self.usein, self.nik)
        finishers = t.start()
        self.all_results.append(finishers)
        last_runner = finishers[max(finishers.keys())]
        self.assertTrue(last_runner == self.nik)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_2(self):
        t = Tournament(90, self.andrei, self.nik)
        finishers = t.start()
        self.all_results.append(finishers)
        last_runner = finishers[max(finishers.keys())]
        self.assertTrue(last_runner == self.nik)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_3(self):
        t = Tournament(90, self.usein, self.andrei, self.nik)
        finishers = t.start()
        self.all_results.append(finishers)
        last_runner = finishers[max(finishers.keys())]
        self.assertTrue(last_runner == self.nik)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_4(self):
        t = Tournament(9, self.andrei, self.usein)
        finishers = t.start()
        self.all_results.append(finishers)
        last_runner = finishers[max(finishers.keys())]
        self.assertTrue(last_runner == self.andrei)


if __name__ == "__main__":
    unittest.main()
