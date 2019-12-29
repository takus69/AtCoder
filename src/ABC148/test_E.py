import unittest

from E import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(12), 1)
        self.assertEqual(run(5), 0)
        self.assertEqual(run(1000000000000000000), 124999999999999995)


if __name__ == '__main__':
    unittest.main()
