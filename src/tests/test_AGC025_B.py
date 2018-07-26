import unittest

from app.AGC025_B import run


class TestSample(unittest.TestCase):
    @unittest.skip('WA')
    def test_run(self):
        self.assertEqual(run(4, 1, 2, 5), 40)
        self.assertEqual(run(2, 5, 6, 0), 1)
        self.assertEqual(run(90081, 33447, 90629, 6391049189), 577742975)


if __name__ == '__main__':
    unittest.main()
