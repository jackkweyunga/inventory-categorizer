

"""
    Provided with consumption data over a given period of time,
    the program output a classified list for all your products.

    structure of the excel must be:

    sku | nc

    where sku - item number
    nc - number of consumption

"""

import numpy as np
import pandas as pd

path = './sample_data/data.xlsx'

class ABC():

    def __init__(self, path):
        self.upper_boundary = 0
        self.mid_boundary = 0
        self.df = pd.read_excel(path)

    def train(self):
        df = self.df
        # create an array from consumption data for a given product
        array_x = df['nc'].to_numpy()

        # calculate the quartiles
        a_type = np.quantile(array_x, .8)
        b_type = np.quantile(array_x, .5)

        self.upper_boundary = a_type
        self.lower_boundary = b_type


    def categorize(self, nc):
        df = self.df
        category = '';
        if nc >= self.upper_boundary: 
            category = 'A' 
        elif nc >= self.mid_boundary and nc < self.upper_boundary:
            category = 'B'
        else:
            category = 'C'
        return f"{category}"


cat = ABC(path)

# train 
cat.train()

# classify
x = cat.categorize(12)

print(x)






