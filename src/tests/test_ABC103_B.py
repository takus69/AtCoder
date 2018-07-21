import unittest

from app.ABC103_B import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run('kyoto', 'tokyo'), 'Yes')


if __name__ == '__main__':
    unittest.main()
