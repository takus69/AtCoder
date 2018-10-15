import unittest

from B import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(15000), '65')
        self.assertEqual(run(75000), '89')
        self.assertEqual(run(200), '02')


if __name__ == '__main__':
    unittest.main()
