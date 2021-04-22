import sys
import unittest

from main import Exercice3


class TestExercice3(unittest.TestCase):

    def test_split_str_by_len(self):
        test_ex = Exercice3()
        self.assertEqual('My string is so long, i have to add carriage returns', test_ex.split_string_by_len('My string is so long, i have to add carriage returns', 5))



if __name__ == '__main__':
    unittest.main()
