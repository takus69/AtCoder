import unittest
from simulator import run


class TestA(unittest.TestCase):
    def test_sample(self):
        score = run('testcases/seed0/0000.txt', 'testcases/seed0/0000_out.txt')
        print(score)


if __name__ == '__main__':
    unittest.main()
