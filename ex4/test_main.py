import unittest
from unittest import TestCase
from unittest.mock import MagicMock

from main import Exercice4


class TestExercice4(TestCase):

    def test_get_actual_temp(self):
        mock = MagicMock()
        mock.get_actual_temp.return_value = 10.5
        mock.get_last_days_temps.return_value = [14.2, 15, 13.6, 17, 21]
        mock.set_heater.return_value = None
        test_ex = Exercice4(functions=mock)

        # test_ex.functions.get_actual_temp()
        # test_ex.functions.get_last_days_temps()
        # test_ex.functions.set_heater(True)

        test_ex.start_heater()

        self.assertEqual(10.5, test_ex.functions.get_actual_temp())
        self.assertEqual([14.2, 15, 13.6, 17, 21], test_ex.functions.get_last_days_temps())
        self.assertEqual(None, test_ex.functions.set_heater(False))

        self.assertEqual('Heater stopped', test_ex.heater_state_str)

if __name__ == '__main__':
    unittest.main()
