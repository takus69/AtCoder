import unittest

from app.AGC026_C import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(4, 'cabaacba'), 4)
        self.assertEqual(run(11, 'mippiisssisssiipsspiim'), 504)
        self.assertEqual(run(4, 'abcdefgh'), 0)
        self.assertEqual(run(18, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
                         9075135300)


if __name__ == '__main__':
    unittest.main()
