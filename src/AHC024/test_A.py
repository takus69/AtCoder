import unittest
from A import parse_graph, check, solver
from simulator import output
from simulator import fetch_input


class TestA(unittest.TestCase):
    def test_parse_graph(self):
        n, m, c = fetch_input('sample.txt')
        con = parse_graph(n, m, c)
        self.assertSetEqual({0, 1, 2, 3, 4}, con[0])
        self.assertSetEqual({0, 2, 3}, con[1])
        self.assertSetEqual({0, 1, 3, 4}, con[2])
        self.assertSetEqual({0, 1, 2}, con[3])
        self.assertSetEqual({0, 2, 5}, con[4])
        self.assertSetEqual({4}, con[5])
    
    def test_check(self):
        n, m, c = fetch_input('sample.txt')
        con = parse_graph(n, m, c)
        self.assertTrue(check(n, m, c, con))
        con2 = {0: {0, 1, 2, 3, 4}, 1: {0, 2, 3}, 2: {0, 1, 3, 4}, 3: {0, 1, 2}, 4: {0, 2, 5}, 5: {4}}
        self.assertTrue(check(n, m, c, con2))
        con2 = {0: {0, 1, 2, 3}, 1: {0, 2, 3}, 2: {0, 1, 3, 4}, 3: {0, 1, 2}, 4: {0, 2, 5}, 5: {4}}
        self.assertFalse(check(n, m, c, con2))
    
    def test_main(self):
        n, m, c = fetch_input('sample.txt')
        d = solver(n, m, c)
        output(d, 'sample_out.txt')



if __name__ == '__main__':
    unittest.main()
