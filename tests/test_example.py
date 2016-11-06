# -*- coding: utf-8 -*-
""" an example for unit test cases """

import unittest 

import context

class JustAnExample(unittest.TestCase):
    """ example testcase """

    def test_unit_example(self):
        self.assertTrue(True)
        self.assertFalse(False)
        self.assertEqual(1, 1, '1==1')

if __name__ == '__main__':
    unittest.main()
