import unittest

from A import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run('oxo'), 900)
        self.assertEqual(run('ooo'), 1000)
        self.assertEqual(run('xxx'), 700)


if __name__ == '__main__':
    unittest.main()
