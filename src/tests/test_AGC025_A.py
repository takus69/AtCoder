import unittest

from app.AGC025_A import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(15), 6)
        self.assertEqual(run(100000), 10)


if __name__ == '__main__':
    unittest.main()
