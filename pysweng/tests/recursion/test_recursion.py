import unittest

from pysweng.recursion import get_path0, get_path2

class TestRobotInAGrid(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.maze0 = ((True, True, True),
                    (True, True, True),
                    (True, True, True))
        cls.maze1 = ((True, True, True),
                    (False, True, True),
                    (True, True, True))
        cls.maze2 = ((True, True, False),
                    (True, False, True),
                    (True, False, True))
        cls.mazes = [cls.maze0, cls.maze1, cls.maze2]

    def test_get_path0(self):
        print()
        for maze in self.mazes:
            print(get_path0(maze))

    def test_get_path2(self):
        print()
        for maze in self.mazes:
            print(get_path2(maze))

if __name__ == '__main__':
    unittest.main(exit=False)
