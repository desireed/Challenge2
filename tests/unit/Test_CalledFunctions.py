#!/usr/bin/env python3

'''
    Name: Test_CalledFunnctions.py
    Author: Christine Desire Davis
    Date: 11 Mar 2021
'''

import unittest
from unittest.mock import create_autospec, Mock
import os
import tests.unit.Fixture
import src.globals
import src.parseargs
import src.buildencodedmap
import src.main


class Test_CallReportStatistics(tests.unit.Fixture.Fixture):
    def test_call_report_statistics(self):
        mock = Mock()
        mock.src.main.report_statistics()
        mock.src.main.report_statistics.assert_called_once()


class Test_ListOfPowerOutlets(tests.unit.Fixture.Fixture):
    def test_list_power(self):
        ''' test list of power outlets'''
        expect_list_of_power_outlets = ['02', '34']

        root_dir = os.path.dirname(os.path.abspath(__file__))
        input_map = root_dir + r'\\..\\..\\input\\' + r'0.txt'

        src.buildencodedmap.build_encoded_map(input_map)
        src.buildencodedmap.determine_neighboring_cell_type()

        self.assertEqual(src.globals.list_of_power_outlets, expect_list_of_power_outlets)


