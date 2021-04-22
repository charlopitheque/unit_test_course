import sys
import unittest

# sys.path.append('C:\\Ynov\\tests_unitaires\\assenceur')
from main import Exercice1


class TestJoinStringList(unittest.TestCase):

    def test_join_string_list(self):
        test_ex = Exercice1()
        self.assertEqual('Hello World', test_ex.join_string_list(['Hello', 'World'], " "))
        self.assertEqual('Hello-World', test_ex.join_string_list(['Hello', 'World'], "-"))

    def test_calc_moy_list(self):
        test_ex = Exercice1()
        self.assertEqual(15, test_ex.calc_moy_list([10, 20]))

if __name__ == '__main__':
    unittest.main()
