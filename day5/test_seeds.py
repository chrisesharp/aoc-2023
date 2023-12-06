import unittest
from seeds import parse_section, parse_input, follow_map, get_value, reverse_map

class GameTest(unittest.TestCase):
    def test_samples_1(self):
        section = """seed-to-soil map:
50 98 2
52 50 48
""".splitlines()
        (source, dest, mappings) = parse_section(section)
        self.assertEqual('seed', source)
        self.assertEqual('soil', dest)
        self.assertEqual(52, get_value(50, mappings))
        self.assertEqual(81, get_value(79, mappings))
    
    def test_samples_2(self):
        data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".split("\n\n")
        (seeds, maps) = parse_input(data)
        self.assertEqual(4, len(seeds))
        self.assertEqual(79, seeds[0])

        location = follow_map(seeds[0], maps)
        self.assertEqual(82, location)
        