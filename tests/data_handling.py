# -*- coding: utf-8 -*-

import os
import unittest

import context
#from rtracer import data

from rtracer import util
#import rtracer.data.util

class DataUtil(unittest.TestCase):

    def  test_get_data_path(self):
        self.assertEqual(util.get_data_path(),
                         os.path.abspath('../data'))
        self.assertTrue(os.path.exists(util.get_data_path()))


if __name__ == '__main__':
    unittest.main()
    

