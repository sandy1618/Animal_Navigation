# usr/bin/env python
__author__ = "Sandeep kumar Nayak"
__email__ = "nayak.sandeep@rm.is.tohoku.ac.jp"
__copyright__ = "Copyright 2020, Tadokoro Lab"

import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 26}

matplotlib.rc('font', **font)
# %matplotlib inline 
import seaborn as sns;sns.set()
import sys
import os
from os.path import expanduser
import math

home = expanduser("~")
# dir_path = home + '/Animal_Navigation/data/tamura/'
dir_path = os.getcwd() + "/"
# file_path = "2020-11-10-17-46-45"
# file_path = "2020-11-10-17-58-24"
# file_path = "2020-11-10-18-46-55"
# file_path = "2020-11-10-18-48-28"
# file_path = "2020-11-25-17-21-12"
file_path = "2020-11-25-17-40-24"


# dir_path = os.getcwd() 
# print dir_path
state_path = dir_path + file_path + '/_slash_state.csv' 
waypoint_path = dir_path + file_path + '/_slash_move_base_slash_goal.csv' 
# trajectory_path = dir_path + '/data/2020-11-06-09-33-29/_slash_amcl_pose.csv' 
trajectory_path = dir_path + file_path + '/_slash_map_slash_robot_pose.csv' 

time_column = "rosbagTimestamp"
start_time = 0
end_time = 0
state_df = pd.read_csv(state_path)
waypoint_df = pd.read_csv(waypoint_path)
trajectory_df = pd.read_csv(trajectory_path)


# Geeting the start time & end time from state_df.
state_df.loc[:,time_column]
state_list = list(state_df.loc[:,'state'])

for index,state in enumerate(state_list):
    if state == 1 :
        
        start_time = state_df.loc[index,time_column]
        print("start")
        
    if state == 2 : 
        
        end_time = state_df.loc[index,time_column]
        print("end")


# If there is no start_time / end_time, then make the starting time or end time.
if not start_time :
    start_time = trajectory_df[time_column].iloc[0]
if not end_time :
    end_time = trajectory_df[time_column].iloc[-1]
    

waypoint_list_x = list(waypoint_df.loc[:,'x'])
waypoint_list_y = list(waypoint_df.loc[:,'y'])
# Trying to add waypoint list to include the starting positoin as well. 
for index,time in enumerate(list(trajectory_df[time_column])):
    start_coordinate = []
    if time >= start_time:
        start_coordinate.append(trajectory_df["x"].iloc[index])
        start_coordinate.append(trajectory_df["y"].iloc[index])
        break 
waypoint_list_x.insert(0,start_coordinate[0])
waypoint_list_y.insert(0,start_coordinate[1])


# Exctract only the column defined by start_time, end_time column. 
def interval_extractor(time_column, start_time, end_time, df, column):
    df_list = list(df.loc[:,time_column])
    final_list = [] 
    for index, time in enumerate(df_list):
        if time >= start_time and time <= end_time:
            final_list.append(df.loc[index,column])
    return final_list

# Now, this list is extracted based on the start_time & end_time. 
trajectory_list_x = interval_extractor(time_column,start_time,end_time,trajectory_df,'x')
trajectory_list_y = interval_extractor(time_column,start_time,end_time,trajectory_df,'y')


#  distance = math.sqrt(pow(waypoint.pose.pose.position.x-animal_pose.pose.pose.position.x,2)+pow(waypoint.pose.pose.position.y-animal_pose.pose.pose.position.y,2))
def velocity_calc(time_column,start_time, end_time,df,column_x,column_y):
    df_list=list(df.loc[:,time_column])
    velocity_list_x = []
    velocity_list_y = []
    velocity_list_net = []
    velocity_time = []
    for index,time in enumerate(df_list):        
        if time >= start_time and time <= end_time:
            if index==0:
                pass
            else:                
                velocity_time.append(time)
                velocity_x=(df.loc[index,column_x]-df.loc[index-1,column_x])/(df.loc[index,time_column] - df.loc[index-1,time_column])
                # Converting into m/s
                velocity_x = velocity_x * pow(10,9)
                velocity_list_x.append(velocity_x)

                velocity_y=(df.loc[index,column_y]-df.loc[index-1,column_y])/(df.loc[index,time_column] - df.loc[index-1,time_column])
                # Converting into m/s
                velocity_y = velocity_y * pow(10,9)
                velocity_list_y.append(velocity_y)

                velocity_list_net.append(math.sqrt(pow(velocity_x,2)+pow(velocity_y,2)))
    out_df = pd.DataFrame(list(zip(velocity_time,velocity_list_net,velocity_list_x,velocity_list_y)),columns=["velocity_time","velocity_list_net","velocity_list_x","velocity_list_y"])
    # return velocity_list_net,velocity_list_x,velocity_list_y,velocity_time
    return out_df
# velocity_list_net,velocity_list_x,velocity_list_y,velocity_time = velocity_calc(time_column,start_time,end_time,trajectory_df,"x","y")
velocity_df = velocity_calc(time_column,start_time,end_time,trajectory_df,"x","y")

def euclidean_distance_calc(x_list,y_list):
    distance = 0
    # Assuming lenght of x_list & y_list are same
    try:
        if len(x_list) == len(y_list):
            for index,x in enumerate(x_list):
                if index == 0:
                    pass
                else:
                    distance += math.sqrt(pow(x_list[index]-x_list[index-1],2)+pow(y_list[index]-y_list[index-1],2))
        else:
            raise IndexError("List provided is not same length")
    except IndexError:
        pass
    return distance

# Measure of Deviation 1
waypoint_distance = euclidean_distance_calc(waypoint_list_x,waypoint_list_y)
trajectory_distance = euclidean_distance_calc(trajectory_list_x,trajectory_list_y)
print ("waypoint_distance",waypoint_distance)
print ("trajectory_distance",trajectory_distance)
trajectory_ratio = (((trajectory_distance-waypoint_distance)/waypoint_distance))*100
# Trajectory Deviation Ratio : TDR 
print ("TDR",trajectory_ratio)

# Navigation time evaluation: 
navigation_time = (end_time - start_time) * pow(10,-9)
print ("navigation_time",navigation_time)



image_path = dir_path+file_path+"/"+file_path+".png"
output_path =  dir_path+file_path+"/"+file_path+".txt"
with open(output_path, 'w') as f:
    # f.write("waypoint_distance",waypoint_distance)
    print ("waypoint_distance: {} ".format(waypoint_distance),file=f)    # Python 3.x
    print ("trajectory_distance: {} ".format(trajectory_distance),file=f)    # Python 3.x
    print ("TDR: {} ".format(trajectory_ratio),file=f)    # Python 3.x
    print ("navigation_time: {} ".format(navigation_time),file=f)    # Python 3.x
   
# with open(output_path, 'w') as f:
#     # f.write("waypoint_distance",waypoint_distance)
#     print ("waypoint_distance: {} ".format(waypoint_distance),file=f)    # Python 2.x
#     print >> f, "trajectory_distance",trajectory_distance
#     print >> f, "TDR",trajectory_ratio
#     print >> f,"navigation_time",navigation_time
#     # print('Filename:', filename, file=f)



#____PLOTTING_____###
# fig, ax = plt.subplots()
# ax.plot(waypoint_list_x,waypoint_list_y,'ro-',label="Waypoints")
# ax.plot(trajectory_list_x,trajectory_list_y,'b.-',label="Trajectory")
# plt.xlabel('X distance',fontsize=22)
# plt.ylabel('Y distance',fontsize=22)
# #Plotting startig & ending poistions 
# ax.scatter(trajectory_list_x[0],trajectory_list_y[0],s=100,marker='D',c='red',label = "Begin")
# ax.scatter(trajectory_list_x[-1],trajectory_list_y[-1],s=100,marker='D',c='black',label = "End")
# plt.title("Human Trajectory with Waypoint",fontsize=22)
# plt.legend()
# plt.savefig(image_path,bbox_inches='tight')
# plt.show()



# converting & appending the time into multiple format for simplification of functions later. 
# class Datetime_Dataframe:
#     def __init__(self, df: pd.DataFrame):
#         self.df = df.copy()
    
  
    
#     def time_col_concat(self,col1,col2,new_col_name):
#         if self.df[col1].dtype == 'int64':
#             self.df[col1]= self.df[col1].astype(str)
#         if self.df[col2].dtype == 'int64':
#             self.df[col2] = self.df[col2].astype(str)
#         temp = self.df[col1] + self.df[col2]
#         temp = temp.astype('int64')
#         try:
#             self.df.insert(1,new_col_name,temp)
#         except: 
#             pass
#         return self.df
        
#     def time_diff(self, time_col, ref_time, new_col_name):
#         temp_nano = self.df[time_col] - ref_time
#         temp_milli = temp_nano*math.pow(10,-6)
#         temp = temp_nano*math.pow(10,-9)
#         try:
#             self.df.insert(2,new_col_name,temp)
#             self.df.insert(3,new_col_name+"milli",temp_milli)
#             self.df.insert(4,new_col_name+"nano",temp_nano)
#         except:
#             pass
#         return self.df
# sensor_time = "sensor_time"
# ref_time = start_time
# time_diff = "time_diff"
# time_convert_obj = Datetime_Dataframe(trajectory_df)
# new_trajectory_df=time_convert_obj.time_col_concat("secs","nsecs",sensor_time)
# new_trajectory_df=time_convert_obj.time_diff(sensor_time,ref_time,time_diff)
# new_trajectory_df.head(1)
# from scipy.spatial.transform import Rotation 
# euler_name = ["roll","pitch","yaw"]
# quat_name = ["x.1","y.1","z.1","w"]

# quat_df = new_trajectory_df.loc[: , "x.1":"w"]
# quat_df
# rot = Rotation.from_quat(quat_df)
# rot_euler = rot.as_euler('xyz', degrees=True)
# euler_df = pd.DataFrame(data=rot_euler, columns=euler_name)
# euler_trajectory_df=new_trajectory_df.join(euler_df)
# euler_trajectory_df.describe()
# euler_trajectory_df.tail()
# euler_trajectory_df.plot(kind="scatter" , x="time_diff",y="yaw")
# plt.show()