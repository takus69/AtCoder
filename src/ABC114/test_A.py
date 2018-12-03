import unittest

from A import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(), )


if __name__ == '__main__':
    unittest.main()
