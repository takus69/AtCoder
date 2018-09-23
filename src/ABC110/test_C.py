import unittest

from C import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run('azzel', 'apple'), 'Yes')
        self.assertEqual(run('chokudai', 'redcoder'), 'No')
        self.assertEqual(run('abcdefghijklmnopqrstuvwxyz', 'ibyhqfrekavclxjstdwgpzmonu'), 'Yes')
        self.assertEqual(run('apple', 'alepp'), 'No')


if __name__ == '__main__':
    unittest.main()
