'''
Created on May 14, 2012

@author: spoganshev
'''
import unittest
from mock import Mock

class ProductionClass:
    def method(self):
        return "production stuff"

class Test(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass

    def testProductionClass(self):
        p = Mock(spec = ProductionClass)
        p.method = Mock(return_value = "mock stuff")
        self.assertEqual("mock stuff", p.method())
        p.method.assert_any_call()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
