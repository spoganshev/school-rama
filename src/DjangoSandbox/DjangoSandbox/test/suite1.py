'''
Created on May 14, 2012

@author: spoganshev
'''
import unittest
from DjangoSandbox.test.tests import ProductionTest
from DjangoSandbox.test.more_tests import OtherTest


class TestSuite1(unittest.TestSuite):

    def __init__(self):
        self.addTest(ProductionTest())
        self.addTest(OtherTest())
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()