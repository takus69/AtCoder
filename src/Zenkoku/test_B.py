import unittest

from B import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(4, 'west', 'east', 'wait'), 3)
        self.assertEqual(run(9, 'different', 'different', 'different'), 0)
        self.assertEqual(run(7, 'zenkoku', 'touitsu', 'program'), 13)


if __name__ == '__main__':
    unittest.main()
