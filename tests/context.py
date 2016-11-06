# -*- coding: utf-8 -*-
""" helps to import local packages for test cases """
 
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
