import unittest
from A import Solver


class TestA(unittest.TestCase):
    def test_mock(self):
        solver = MockSolver('testcases/0000.txt', 'testcases/0000_out.txt')
        solver.solve()
        score = solver.evaluate()
        print('スコア:', format(score, ','))
        solver.end()


class MockSolver(Solver):
    def __init__(self, in_file, out_file):
        self.in_file = open(in_file, 'r')
        self.out_file = open(out_file, 'w')
        super().__init__()

    def init(self):
        self.N = int(self.in_file.readline())
        self.h = [self.in_file.readline() for _ in range(self.N-1)]
        self.v = [self.in_file.readline() for _ in range(self.N)]
        self.d = [list(map(int, self.in_file.readline().split())) for _ in range(self.N)]
        self.visited = [[False for _ in range(self.N)] for _ in range(self.N)]
        self.in_file.close()

    def print(self, s='', end='\n'):
        self.out_file.write(s + end)

    def end(self):
        self.out_file.close()

    def evaluate(self):
        score = 0
        return score


if __name__ == '__main__':
    solver = MockSolver('testcases/0014.txt', 'testcases/0014_out.txt')
    solver.solve()
    score = solver.evaluate()
    solver.end()
    print('スコア:', format(score, ','))
