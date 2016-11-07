# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from rtracer import util

class UserData(object):
    """ this class stores all user data """

    def __init__(self, folder):
        
        user_data_path = os.path.join(util.get_data_path(), folder, 'user.csv')
        self.data = pd.read_csv(user_data_path)
        
        # useful 

    def get_cols(self):
        return self.data.columns
        
        
def main():
    
    users = UserData('data_csv_small')
    
    # print all columns
    print(users.data.columns)

    # plot histogramm of ratings
    plt.style.use('ggplot')
    plt.grid()
    plt.hist(users.data['average_stars'], bins=9, range=(0.75,5.25))
    plt.show()  


if __name__ == '__main__':
    main()
