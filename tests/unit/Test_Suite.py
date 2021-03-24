#!/usr/bin/env python3

'''
    Name: Tet_Suite.py
    Author: Christine Desire Davis
    Date: 11 Mar 2021
'''

import sys
import os
import unittest
import tests.unit.Test_CalledFunctions
import tests.unit.Test_BuildEncodedMap

sys.path.insert(0, os.path.abspath(''))

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add test modules to the test suite
suite.addTests(loader.loadTestsFromModule(tests.unit.Test_CalledFunctions))
suite.addTests(loader.loadTestsFromModule(tests.unit.Test_BuildEncodedMap))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

if __name__ == '__main__':
    pass
