import unittest

from B import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(2), 15)


if __name__ == '__main__':
    unittest.main()
