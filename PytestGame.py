import unittest
from Game import popadanie


class GameTest(unittest.TestCase):
    def test1(self):
        x_pl = 15
        y_pl = 15
        w_pl = 30
        h_pl = 30
        self.assertEqual(popadanie(x_pl, y_pl, x_pl, y_pl, w_pl, h_pl), True)

    def test2(self):
        x_pl = -10
        y_pl = 10
        w_pl = 30
        h_pl = 30
        self.assertEqual(popadanie(x_pl, y_pl, x_pl, y_pl, w_pl, h_pl), False)

    def test3(self):
        x_pl = -10
        y_pl = 10
        w_pl = 30
        h_pl = 30
        self.assertEqual(popadanie(x_pl, y_pl, x_pl, y_pl, w_pl, h_pl), False)
