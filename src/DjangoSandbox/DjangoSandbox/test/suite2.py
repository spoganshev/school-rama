'''
Created on May 14, 2012

@author: spoganshev
'''
import unittest
from DjangoSandbox.test.tests import ProductionTest


class TestSuite2(unittest.TestSuite):

    def __init__(self):
        self.addTest(ProductionTest())
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()