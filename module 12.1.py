import runner
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        rn = runner.Runner("child")
        for i in range(10):
            rn.walk()
        self.assertEqual(rn.distance, 50)

    def test_run(self):
        rn1 = runner.Runner("Auto")
        for i in range(10):
            rn1.run()
        self.assertEqual(rn1.distance, 100)

    def test_challenge(self):
        rn2 = runner.Runner("man")
        rn3 = runner.Runner("bicycle")
        for i in range(10):
            rn2.walk()
            rn3.run()
        self.assertEqual(rn2.distance, rn3.distance)


if __name__ == "__main__":
    unittest.main()
