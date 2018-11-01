import unittest

from D import run, primes


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(5), '11 31 41 61 71')
        self.assertEqual(run(6), '11 31 41 61 71 101')
        self.assertEqual(run(7), '11 31 41 61 71 101 131')

    def test_primes(self):
        self.assertEqual(primes(5), [2, 3, 5])
        self.assertEqual(primes(20), [2, 3, 5, 7, 11, 13, 17, 19])


if __name__ == '__main__':
    unittest.main()
