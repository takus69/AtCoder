import unittest

from B import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(4, 4, ['##.#', '....', '##.#', '.#.#']),
                         ['###', '###', '.##'])


if __name__ == '__main__':
    unittest.main()
