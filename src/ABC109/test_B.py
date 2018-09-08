import unittest

from B import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(9, ['basic', 'c', 'cpp', 'php', 'python',
                                 'nadesico', 'ocaml', 'lua', 'assembly']
                                 ), 'Yes')


if __name__ == '__main__':
    unittest.main()
