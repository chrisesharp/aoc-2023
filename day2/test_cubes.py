import unittest
from cubes import is_possible, parse, power


input_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".splitlines()

class GameTest(unittest.TestCase):
    def test_samples_1(self):
        games = parse(input_data)
        actuals = (12, 13, 14)
        self.assertTrue(is_possible(games[0], actuals))
        self.assertTrue(is_possible(games[1], actuals))
        self.assertFalse(is_possible(games[2], actuals))
        self.assertFalse(is_possible(games[3], actuals))
        self.assertTrue(is_possible(games[4], actuals))

    def test_adder(self):
        games = parse(input_data)
        actuals = (12, 13, 14)
        possibles = [i+1 for i, x in enumerate(games) if is_possible(x, actuals)]
        self.assertEqual(8, sum(possibles))

    def test_power(self):
        games = parse(input_data)
        self.assertEqual(48, power(games[0]))