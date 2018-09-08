import unittest

from C import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(3, 2), 9)
        self.assertEqual(run(5, 3), 1)
        self.assertEqual(run(31415, 9265), 27)
        self.assertEqual(run(35897, 932), 114191)


if __name__ == '__main__':
    unittest.main()
