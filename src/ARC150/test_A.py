import unittest
import A


class test_A(unittest.TestCase):
    def test_check(self):
        self.assertEqual('Yes', A.check('1??', 2))
        self.assertEqual('No', A.check('?1?0', 2))
        self.assertEqual('No', A.check('011?1?', 3))
        self.assertEqual('Yes', A.check('00?1???10?', 5))


if __name__ == '__main__':
    unittest.main()
