# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from rtracer import data


user_data = data.load_data_frame('data_csv_small/user.csv')


# print all columns
print(user_data.columns)

# plot histogramm of ratings
plt.style.use('ggplot')
plt.hist(user_data['average_stars'], bins=9, range=(0.75,5.25))
plt.show()