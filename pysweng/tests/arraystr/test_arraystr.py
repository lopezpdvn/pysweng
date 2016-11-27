import unittest

from pysweng.arraystr import permutation

class TestStringsAlgs(unittest.TestCase):
    def test_permutation(self):
        permutation('ABCD')

if __name__ == '__main__':
    unittest.main(exit=False)
