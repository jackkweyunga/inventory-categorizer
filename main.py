

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

    def __init__():
        pass

    def train(path):
        df = pd.read_excel(path)

        # create an array from consumption data for a given product
        array_x = df['nc'].to_numpy()

        # calculate the top quartiles
        a_type = np.quantile(array_x, .8)
        b_type = np.quantile(array_x, .5)


    def categorize():
        pass



# print(df)

# print(df['nc'])



# print(a_type)
# print(b_type)
# print(c_type)

# upper = df[df['nc'] > a_type]
# mid = df[(df['nc'] >= b_type and df['sku'] < b_type)]
# lower = df[df['nc'] <= b_type]

# print(upper)

# plt.scatter(array_x, array_y)
# plt.show()



