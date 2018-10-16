import unittest

from C import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(127), 4)
        self.assertEqual(run(3), 3)
        self.assertEqual(run(9), 1)
        #self.assertEqual(run(44852), 16)


if __name__ == '__main__':
    unittest.main()
