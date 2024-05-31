import unittest
from cube import Game

class TestCube(unittest.TestCase):
    '''
    Unit tests for cube.py functions
    '''
    def test_get_game(self):
        game_1 = Game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
        self.assertEqual(game_1.get_game(), 1)
        game_2 = Game("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
        self.assertEqual(game_2.get_game(), 2)
        game_3 = Game("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
        self.assertEqual(game_3.get_game(), 3)
        game_4 = Game("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
        self.assertEqual(game_4.get_game(), 4)
        game_5 = Game("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
        self.assertEqual(game_5.get_game(), 5)

    def test_get_sets(self):
        game_1 = Game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
        self.assertEqual(game_1.get_sets(), [{"blue":3, "red":4}, {"red":1, "green":2, "blue":6}, {"green":2}])
        game_2 = Game("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
        self.assertEqual(game_2.get_sets(), [{"blue":1, "green":2},{"green":3, "blue":4, "red":1}, {"green":1, "blue":1}])
        game_3 = Game("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
        self.assertEqual(game_3.get_sets(), [{"green":8, "blue":6, "red":20}, {"blue":5, "red":4, "green":13}, {"green":5, "red":1}])
        game_4 = Game("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
        self.assertEqual(game_4.get_sets(), [{"green":1, "red":3, "blue":6}, {"green":3, "red":6}, {"green":3, "blue":15, "red":14}])
        game_5 = Game("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
        self.assertEqual(game_5.get_sets(), [{"red":6, "blue":1, "green":3}, {"blue":2, "red":1, "green":2}])

    def test_game_possible(self):
        possible = {"red":12, "green":13, "blue":14}
        game_1 = Game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
        self.assertEqual(game_1.game_possible(valid_set=possible), True)
        game_2 = Game("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
        self.assertEqual(game_2.game_possible(valid_set=possible), True)
        game_3 = Game("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
        self.assertEqual(game_3.game_possible(valid_set=possible), False)
        game_4 = Game("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
        self.assertEqual(game_4.game_possible(valid_set=possible), False)
        game_5 = Game("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
        self.assertEqual(game_5.game_possible(valid_set=possible), True)

    def test_max_set(self):
        game_1 = Game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
        self.assertEqual(game_1.max_set(), {"red":4, "green":2, "blue":6})
        game_2 = Game("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
        self.assertEqual(game_2.max_set(), {"red":1, "green":3, "blue":4})
        game_3 = Game("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
        self.assertEqual(game_3.max_set(), {"red":20, "green":13, "blue":6})
        game_4 = Game("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
        self.assertEqual(game_4.max_set(), {"red":14, "green":3, "blue":15})
        game_5 = Game("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
        self.assertEqual(game_5.max_set(), {"red":6, "green":3, "blue":2})

    def test_get_power(self):
        game_1 = Game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
        self.assertEqual(game_1.get_power(), 48)
        game_2 = Game("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
        self.assertEqual(game_2.get_power(), 12)
        game_3 = Game("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
        self.assertEqual(game_3.get_power(), 1560)
        game_4 = Game("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
        self.assertEqual(game_4.get_power(), 630)
        game_5 = Game("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
        self.assertEqual(game_5.get_power(), 36)

if __name__ == "__main__":
    unittest.main()