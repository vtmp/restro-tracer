# -*- coding: utf-8 -*-
""" an example for unit test cases """

import unittest 

import context
from rtracer import data  # import package that do all the data stuff
from rtracer import util  # import package for various helper functions

class JustAnExample(unittest.TestCase):
    """ example testcase """

    def test_unit_example(self):
        """ all testcase names must begin with test to be run """
        self.assertTrue(True)
        self.assertFalse(False)
        self.assertEqual(1, 1, '1==1')

if __name__ == '__main__':
    unittest.main()
