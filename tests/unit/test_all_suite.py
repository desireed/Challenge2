import unittest


#import usertest
#import configtest # first test
import sys
import os
import unittest   # second test

import test_called_functions

sys.path.insert(0, os.path.abspath(''))

class ConfigTestCase(unittest.TestCase):
    def setUp(self):
        print('stp')
        ##set up code

    def runTest(self):
        #runs test
        print ('stp')

def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    #test_suite.addTest(unittest.makeSuite(ConfigTestCase))
    #test_suite.addTest(unittest.makeSuite(ConfigTestCase))
    #test_suite.addTest(unittest.makeSuite(test_called_functions))
    unittest.TestLoader().loadTestsFromTestCase(ConfigTestCase)
    unittest.TestLoader().loadTestsFromTestCase(test_called_functions)
    return test_suite

#mySuit = suite(suite.TestSuite)

# mySuite = suite
# unittest.TextTestRunner(verbosity=2).run(mySuite)
# unittest.runner.run(mySuit)
suite = unittest.TestLoader().loadTestsFromTestCase(test_called_functions)
unittest.TextTestRunner(verbosity=2).run(suite)

#
#
if __name__ == '__main__': pass
#    unittest.main()
