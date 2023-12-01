import unittest
from calibrate import calibrate

class GameTest(unittest.TestCase):
    def x_test_samples_1(self):
        input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""".split()
        self.assertEqual(12, calibrate(input[0]))
        self.assertEqual(38, calibrate(input[1]))
        self.assertEqual(15, calibrate(input[2]))
        self.assertEqual(77, calibrate(input[3]))
    

    def test_samples_2(self):
        input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""".split()
        
        self.assertEqual(29, calibrate(input[0]))
        self.assertEqual(83, calibrate(input[1]))
        self.assertEqual(13, calibrate(input[2]))
        self.assertEqual(24, calibrate(input[3]))
        self.assertEqual(42, calibrate(input[4]))
        self.assertEqual(14, calibrate(input[5]))
        self.assertEqual(76, calibrate(input[6]))