import unittest
from unittest.mock import patch
import src.globals
import src.buildencodedmap
from src.parseargs import input_map_filename


class Test_encoded_call_neighbors(unittest.TestCase):

    def test_encoded_call_neighbors(self):
        if input_map_filename == r'input/0.txt':
            self.assertEqual(src.globals.cell_dictionary['00'].N.cell_type, 'U')
            self.assertEqual(src.globals.cell_dictionary['00'].S.cell_type, 'X')
            self.assertEqual(src.globals.cell_dictionary['00'].E.cell_type, 'X')
            self.assertEqual(src.globals.cell_dictionary['00'].W.cell_type, 'U')

            self.assertEqual(src.globals.cell_dictionary['44'].N.cell_type, 'X')
            self.assertEqual(src.globals.cell_dictionary['44'].S.cell_type, 'U')
            self.assertEqual(src.globals.cell_dictionary['44'].E.cell_type, 'U')
            self.assertEqual(src.globals.cell_dictionary['44'].W.cell_type, 'X')


class Test_power_outlets(unittest.TestCase):
    def test_power_outlets(self):
        if input_map_filename == r'input/0.txt':
            self.assertEqual(len(src.globals.list_of_power_outlets), 2)
            self.assertEqual(src.globals.list_of_power_outlets[0], '02')
            self.assertEqual(src.globals.list_of_power_outlets[1], '34')
        else:
            self.assertTrue(self, True)

if __name__ == '__main__':
    unittest.main()
