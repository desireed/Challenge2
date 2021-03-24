#!/usr/bin/env python3

'''
    Name: Test_BuildEncodedMap.py
    Author: Christine Desire Davis
    Date: 11 Mar 2021
'''

import os
import unittest
import tests.unit.Fixture
import src.globals
import src.buildencodedmap



class Test_EncodedCellNeighbors(tests.unit.Fixture.Fixture):
    ''' Test 2 cells neighbors for their symbol types for map 0.txt. '''

    def setUp(self):
        root_dir = os.path.dirname(os.path.abspath(__file__))
        input_map = root_dir + r'\\..\\..\\input\\' + r'0.txt'
        src.buildencodedmap.build_encoded_map(input_map)
        src.buildencodedmap.determine_neighboring_cell_type()
        src.buildencodedmap.print_neighboring_cell_information()

    def test_encoded_cell_neighbors_for_two_cells(self):
        src.buildencodedmap.print_neighboring_cell_information()
        self.assertEqual(src.globals.cell_dictionary['00'].N.cell_type, 'U')
        self.assertEqual(src.globals.cell_dictionary['00'].S.cell_type, 'X')
        self.assertEqual(src.globals.cell_dictionary['00'].E.cell_type, 'X')
        self.assertEqual(src.globals.cell_dictionary['00'].W.cell_type, 'U')

        self.assertEqual(src.globals.cell_dictionary['44'].N.cell_type, 'X')
        self.assertEqual(src.globals.cell_dictionary['44'].S.cell_type, 'U')
        self.assertEqual(src.globals.cell_dictionary['44'].E.cell_type, 'U')
        self.assertEqual(src.globals.cell_dictionary['44'].W.cell_type, 'O')


class Test_PowerOutlets(tests.unit.Fixture.Fixture):
    ''' Test for discovering the number of power outlets in map 0.txt. '''

    def setUp(self):
        root_dir = os.path.dirname(os.path.abspath(__file__))
        input_map = root_dir + r'\\..\\..\\input\\' + r'0.txt'
        src.globals.list_of_power_outlets = []
        src.buildencodedmap.build_encoded_map(input_map)
        src.buildencodedmap.determine_neighboring_cell_type()

    def test_power_outlets(self):
        self.assertEqual(len(src.globals.list_of_power_outlets), 2)
        self.assertEqual(src.globals.list_of_power_outlets[0], '02')
        self.assertEqual(src.globals.list_of_power_outlets[1], '34')


