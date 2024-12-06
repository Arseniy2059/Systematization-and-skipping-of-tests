import unittest
import o1


calcST = unittest.TestSuite()
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(o1.TournamentTest))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(o1.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcST)
