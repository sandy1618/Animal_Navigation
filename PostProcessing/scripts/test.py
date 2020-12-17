# usr/bin/env python
__author__ = "Sandeep kumar Nayak"
__email__ = "nayak.sandeep@rm.is.tohoku.ac.jp"
__copyright__ = "Copyright 2020, Tadokoro Lab"
import pandas as pd
if __name__ == "__main__":
    joy_path = '../data/ros_bag/2019-12-04-20-18-32/2019-12-04-20-18-32_joy.csv'
    imu_path = '../data/ros_bag/2019-12-04-20-18-32/2019-12-04-20-18-32_spatial_imu.csv'
    joy_df = pd.read_csv(joy_path)
    print(joy_df.loc[10, '%time'])
    count = 0
    for index, value in enumerate(joy_df.loc[:,'%time']):

        if value >= joy_df.loc[10,'%time'] and count < 10:


                print ( value )
                count+=1