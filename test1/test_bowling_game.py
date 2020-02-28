from unittest import TestCase
from bowling_game import Game


class TestGame(TestCase):
    def setUp(self):
        self.game = Game()

    def roll_all(self,rolls):
        for pins in rolls:
            self.game.roll(pins)

    def test_Bowling(self):
        self.roll_all(20 * [0])

        self.assertEqual(0, self.game.score())

    def test_Bowling_1(self):
        self.roll_all(20 * [1])

        self.assertEqual(20, self.game.score())

    def test_spare_bonus(self):
        self.roll_all([6,4,4] + 17 * [0])
  
        self.assertEqual(18, self.game.score())

    def test_is_strike_bonus(self):
        self.roll_all([10] + 19 * [10])
  
        self.assertEqual(300, self.game.score())
