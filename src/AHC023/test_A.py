import unittest
from simulator import run


class TestA(unittest.TestCase):
    def test_sample(self):
        score = run('testcases/sample/input.txt', 'testcases/sample/output.txt')
        print(score)


if __name__ == '__main__':
    unittest.main()
