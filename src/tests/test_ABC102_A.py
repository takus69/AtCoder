import unittest

from app.ABC102_A import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(3), 6)
        self.assertEqual(run(10), 10)
        self.assertEqual(run(999999999), 1999999998)


if __name__ == '__main__':
    unittest.main()
