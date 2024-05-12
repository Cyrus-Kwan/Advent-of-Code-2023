import unittest
import trebuchet
import re

class TestTrebuchet(unittest.TestCase):
    '''
    Unit tests for trebuchet.py functions
    '''
    def test_first_digit(self):
        self.assertEqual(trebuchet.first_digit("1abc2"), "1")
        self.assertEqual(trebuchet.first_digit("pqr3stu8vwx"), "3")
        self.assertEqual(trebuchet.first_digit("a1b2c3d4e5f"), "1")
        self.assertEqual(trebuchet.first_digit("treb7uchet"), "7")
        self.assertEqual(trebuchet.first_digit("nqninenmvnpsz874"), "8")

    def test_last_digit(self):
        self.assertEqual(trebuchet.last_digit("1abc2"), "2")
        self.assertEqual(trebuchet.last_digit("pqr3stu8vwx"), "8")
        self.assertEqual(trebuchet.last_digit("a1b2c3d4e5f"), "5")
        self.assertEqual(trebuchet.last_digit("treb7uchet"), "7")

    def test_join_digits(self):
        self.assertEqual(trebuchet.join_digits("1","2"), 12)
        self.assertEqual(trebuchet.join_digits("3","8"), 38)
        self.assertEqual(trebuchet.join_digits("1","5"), 15)
        self.assertEqual(trebuchet.join_digits("7","7"), 77)

    def test_sum_nums(self):
        self.assertEqual(trebuchet.sum_nums(12, 38, 15, 77), 142)

    def test_sub_words(self):
        self.assertEqual(trebuchet.sub_words("two1nine"), "219")
        self.assertEqual(trebuchet.sub_words("eightwothree"), "823")
        self.assertEqual(trebuchet.sub_words("abcone2threexyz"), "123")
        self.assertEqual(trebuchet.sub_words("xtwone3four"), "2134")
        self.assertEqual(trebuchet.sub_words("4nineeightseven2"), "49872")
        self.assertEqual(trebuchet.sub_words("zoneight234"), "18234")
        self.assertEqual(trebuchet.sub_words("7pqrstsixteen"), "76")

    def test_answer(self):
        # Checked own solution to HyperNeutrino's solution on youtube:
        #   https://www.youtube.com/watch?v=y-kOUFrHaKs
        
        n = "one two three four five six seven eight nine".split()
        p = "(?=(" + "|".join(n) + "|\\d" + "))"

        with open(trebuchet.current_dir()+"calibrations") as file:
            lines = file.read().split("\n")
            f = lambda search: str(n.index(search)+1) if search in n else search
            for line in lines:
                digits = [*map(f, re.findall(p, line))]
                self.assertEqual(trebuchet.answer(line), int(digits[0]+digits[-1]))

if __name__ == "__main__":
    unittest.main()