# -*- coding: utf-8 -*-

import os
import unittest

import context

from rtracer import util
from rtracer import data


class DataUtil(unittest.TestCase):

    def  test_get_data_path(self):
        self.assertEqual(data.get_data_path(),
                         os.path.abspath('../data'))
        self.assertTrue(os.path.exists(data.get_data_path()))


if __name__ == '__main__':
    unittest.main()


