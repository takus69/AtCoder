import unittest

from C import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run('aba', 4), 'b')
        self.assertEqual(run('atcoderandatcodeer', 5), 'andat')
        self.assertEqual(run('z', 1), 'z')


if __name__ == '__main__':
    unittest.main()
