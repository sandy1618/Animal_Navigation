#!/usr/bin/python
from .to_df_converter import ToDfConverter

import pandas as pd


class CsvToDf(ToDfConverter):
    def __init__(self):
        pass
    # @staticmethod
    # def downsample_series(series, win_size):
    #     cumsum = 0
    #     avg = []
    #     count = 0 
    #     for element in series:
    #         cumsum = cumsum + element
    #         count += 1
    # #         print element
    #         if count == win_size:
    #             avg.append(cumsum/win_size)
    #             count = 0
    #             cumsum = 0
            
    #     return pd.Series(avg)
    @staticmethod
    def read(x_csv):
        """
        Reads in a CSV file representing the 2D grid and return a DataFrame
        :param x_csv: the CSV file containing X values
        :return: pandas DataFrame where indices are X and Y grid number
        :rtype: pd.DataFrame
        """
    
        xyz = pd.read_csv(x_csv)
        # df.columns = list('xyzrbc')
        
        # xyz=df.iloc[:,:3]
        # xyz = df.round(2)

        # x_df = pd.read_csv(x_csv, header=None)
        # y_df = pd.read_csv(y_csv, header=None)
        # z_df = pd.read_csv(z_csv, header=None)
        # xyz = pd.concat([x_df.stack(), y_df.stack(), z_df.stack()], axis=1)
        # xyz.columns = list('xyz')
        
        # x_series=downsample_series(xyz.iloc[:,0],20)
        # y_series=downsample_series(xyz.iloc[:,1],20)
        # z_series=downsample_series(xyz.iloc[:,2],20)
        # xyz = pd.concat([x_series,y_series,z_series],axis=1)
        # xyz.columns=list('xyz')
        return xyz
