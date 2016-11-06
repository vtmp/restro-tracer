# -*- coding: utf-8 -*-

import os

def get_data_path():
    rel_path = os.path.join(os.path.dirname(__file__), '../../data/')
    return os.path.abspath(rel_path)
    
if __name__ == '__main__':
    print('hallo')
    print(get_data_path())