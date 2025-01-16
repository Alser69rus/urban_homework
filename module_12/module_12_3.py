import unittest
from module_12_1 import RunnerTest
from module_12_2 import TournamentTest

suit = unittest.TestSuite()
suit.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suit.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suit)
