import unittest

from A import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(3, 2, 'acp', 'ae'), 6)
        self.assertEqual(run(6, 3, 'abcdef', 'abc'), -1)
        self.assertEqual(run(15, 9, 'dnsusrayukuaiia', 'dujrunuma'), 45)


if __name__ == '__main__':
    unittest.main()
