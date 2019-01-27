import unittest

from B import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(3, [4980, 7980, 6980]), 15950)
        self.assertEqual(run(4, [4320]*4), 15120)


if __name__ == '__main__':
    unittest.main()
