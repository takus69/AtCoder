import unittest

from C import run


class TestSample(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run(3, 3, ['.#.', '###', '.#.']), 'Yes')
        self.assertEqual(run(5, 5, ['#.#.#', '.#.#.', '#.#.#', '.#.#.', '#.#.#']), 'No')
        self.assertEqual(run(11, 11, ['...#####...', '.##.....##.', '#..##.##..#', '#..##.##..#', '#.........#', '#...###...#', '.#########.', '.#.#.#.#.#.', '##.#.#.#.##', '..##.#.##..', '.##..#..##.'
]), 'Yes')


if __name__ == '__main__':
    unittest.main()
