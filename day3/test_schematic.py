import unittest
from schematic import parse, is_attached, gear_ratio, add_part_to_gear

class GameTest(unittest.TestCase):
    def test_samples_1(self):
        schematic = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".splitlines()
        numbers = parse(schematic)
        self.assertTrue(is_attached(numbers['467'][0], schematic)[0])
        self.assertFalse(is_attached(numbers['114'][0], schematic)[0])
        self.assertTrue(is_attached(numbers['35'][0], schematic)[0])
        self.assertTrue(is_attached(numbers['633'][0], schematic)[0])
        self.assertTrue(is_attached(numbers['617'][0], schematic)[0])
        self.assertFalse(is_attached(numbers['58'][0], schematic)[0])
        self.assertTrue(is_attached(numbers['592'][0], schematic)[0])
        self.assertTrue(is_attached(numbers['755'][0], schematic)[0])
        self.assertTrue(is_attached(numbers['664'][0], schematic)[0])
        self.assertTrue(is_attached(numbers['598'][0], schematic)[0])

        gears = {}
        total = 0
        for number in numbers.keys():
            for coord in numbers[number]:
                (attached, gear) = is_attached(coord, schematic)
                if attached:
                    total += int(number)
                    if gear:
                        add_part_to_gear(number, gear, gears)
        self.assertEqual(4361, total)
        self.assertEqual(467835, sum([gear_ratio(gear) for gear in gears.values()]))



