# -*- coding: utf-8 -*-

import os
import pandas as pd

def get_data_path():
    rel_path = os.path.join(os.path.dirname(__file__), '../../data/')
    return os.path.abspath(rel_path)
    
def load_data_frame(csv_path_rel):
    user_data_path = os.path.join(get_data_path(), csv_path_rel)
    return pd.read_csv(user_data_path)
    
if __name__ == '__main__':
    print('hallo')
    print(get_data_path())