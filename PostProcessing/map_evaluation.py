# usr/bin/env python
__author__ = "Sandeep kumar Nayak"
__email__ = "nayak.sandeep@rm.is.tohoku.ac.jp"
__copyright__ = "Copyright 2020, Tadokoro Lab"

import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline 
import seaborn as sns;sns.set()
import sys
import os

dir_path = os.getcwd()
# print dir_path
state_path = dir_path + '/data/2020-11-04-20-32-20/_slash_state.csv' 
waypoint_path = dir_path + '/data/2020-11-04-20-32-20/_slash_move_base_slash_goal.csv' 
time_column = "rosbagTimestamp"

state_df = pd.read_csv(state_path)

state_df.loc[:,time_column]
state_list = list(state_df.loc[:,'state'])
for index,state in enumerate(state_list):
    # switch(state)
    #     case 1 : print "start" 
    #     case 2 : print "end"

    if state == 1 :
        print("start")
        start_time = state_df.loc[index,"rosbagTimestamp"]
        
    if state == 2 : 
        print( "end")
        end_time = state_df.loc[index,"rosbagTimestamp"]
waypoint_df = pd.read_csv(waypoint_path)



waypoint_list_x = list(waypoint_df.loc[:,'x'])
waypoint_list_y = list(waypoint_df.loc[:,'y'])


trajectory_path = dir_path + '/data/2020-11-04-20-32-20/_slash_amcl_pose.csv' 
trajectory_df = pd.read_csv(trajectory_path)
# print trajectory_df
def interval_extractor(time_column, start_time, end_time, df, column):
    df_list = list(df.loc[:,time_column])
    final_list = []
    for index, time in enumerate(df_list):
        if time >= start_time and time <= end_time:
            final_list.append(df.loc[index,column])
    return final_list

# trajectory_list_x = list(trajectory_df.loc[:,'x'])
# trajectory_list_y = list(trajectory_df.loc[:,'y'])
trajectory_list_x = interval_extractor(time_column,start_time,end_time,trajectory_df,'x')
trajectory_list_y = interval_extractor(time_column,start_time,end_time,trajectory_df,'y')

fig, ax = plt.subplots()
ax.plot(waypoint_list_y,waypoint_list_x,'ro-',label="Waypoints")
ax.plot(trajectory_list_y,trajectory_list_x,'b.-',label="Trajectory")
plt.xlabel('X distance')
plt.ylabel('Y distance')
#Plotting startig & ending poistions 
ax.scatter(trajectory_list_y[0],trajectory_list_x[0],s=100,marker='D',c='red',label = "Begin")
ax.scatter(trajectory_list_y[-1],trajectory_list_x[-1],s=100,marker='D',c='black',label = "End")
plt.title("Distance")
plt.legend()
plt.show()
