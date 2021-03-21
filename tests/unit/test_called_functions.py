import unittest
from unittest.mock import patch
import src.globals
import src.parseargs
import src.buildencodedmap
import src.main

# target = __import__("my_sum.py")
# sum = target.sum


# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)


# @patch('main.report_statistics')
# def test_call_report_statistics(x, mock_func):
#     report_statistics()
#     mock_func.assert_called_with()

# class TestCallReportStatistics(unittest.TestCase):
#     def test_call_report_statistics(self):
#         report_statistics()
#         self.called(report_statistics)


class Test_list_of_power_outlets(unittest.TestCase):
    def test_list_power(self):
        ''' test list of power outlets'''
        expect_list_of_power_outlets = ['02', '34']
        src.buildencodedmap.build_encoded_map(r'../../input/0.txt')
        if src.parseargs.input_map_filename == r'../../input/0.txt':
            self.assertEqual(src.globals.list_of_power_outlets, expect_list_of_power_outlets)


# class TestSum(unittest.TestCase):
#     def test_list_int(self):
#         """
#         Test that it can sum a list of integers
#         """
#         data = [1, 2, 3]
#         result = sum(data)
#         self.assertEqual(result, 6)




# @patch('module.report_statistics')
# def test(MockReportStatictics):
#     module.report_statistics()
#     assert MockReportStatictics is module.report_statistics
#     assert MockReportStatictics.called

if __name__ == '__main__':
    unittest.main()
