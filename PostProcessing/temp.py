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
import Datetime_Dataframe
import math

class Map_evaluation():
    def __init__(self):

        # To get the main folder for analysis. 
        self.home = expanduser("~")
        # self.dir_path = home + '/Animal_Navigation/data/tamura/'
        self.dir_path = os.getcwd() + "/"
        self.file_path = "2020-11-25-18-09-37"

        # self.dir_path = os.getcwd() 
        # print self.dir_path
        self.state_path = self.dir_path + self.file_path + '/_slash_state.csv' 
        self.waypoint_path = self.dir_path + self.file_path + '/_slash_move_base_slash_goal.csv' 
        # trajectory_path = self.dir_path + '/data/2020-11-06-09-33-29/_slash_amcl_pose.csv' 
        self.trajectory_path = self.dir_path + self.file_path + '/_slash_map_slash_robot_pose.csv' 
        self.signal_path = self.dir_path + self.file_path + '/_slash_cmd_sig.csv'

        self.time_column = "rosbagTimestamp"
        self.start_time = 0
        self.end_time = 0
        self.state_df = pd.read_csv(self.state_path)
        self.waypoint_df = pd.read_csv(self.waypoint_path)
        self.trajectory_df = pd.read_csv(self.trajectory_path)

        # Calling the self.start_time & End_time calculating function
        self.get_start_end()

        # #Declaring the waypoint list variable.
        # self.waypoint_list_x = []
        # self.waypoint_list_y = []
        # Calling the waypoint fuction.
        self.get_waypoint()

        


        pass
    def get_start_end(self):
                # _______Getting Start & End time ___________________
        # Geeting the start time & end time from state_df.
        self.state_df.loc[:,self.time_column]
        self.state_list = list(state_df.loc[:,'state'])

        for index,state in enumerate(self.state_list):
            if state == 1 :
                
                self.start_time = state_df.loc[index,time_column]
                print("start")
                
            if state == 2 : 
                
                self.end_time = state_df.loc[index,time_column]
                print("end")

        # If there is no self.start_time / self.end_time, then make the starting time or end time.
        if not self.start_time :
            self.start_time = trajectory_df[time_column].iloc[0]
        if not self.end_time :
            self.end_time = trajectory_df[time_column].iloc[-1]
            
    def get_waypoint(self):
        ## These adds waypoint data point to waypoint x & waypoint y coordinate location. 
        self.waypoint_list_x = list(self.waypoint_df.loc[:,'x'])
        self.waypoint_list_y = list(self.waypoint_df.loc[:,'y'])
        # Trying to add waypoint list to include the starting positoin as well. 
        for index,time in enumerate(list(self.trajectory_df[time_column])):
            start_coordinate = []
            if time >= self.start_time:
                start_coordinate.append(self.trajectory_df["x"].iloc[index])
                start_coordinate.append(self.trajectory_df["y"].iloc[index])
                break 
        self.waypoint_list_x.insert(0,start_coordinate[0])
        self.waypoint_list_y.insert(0,start_coordinate[1])





# Exctract only the column defined by self.start_time, self.end_time column. 
def interval_extractor(time_column, self.start_time, self.end_time, df, column):
    df_list = list(df.loc[:,time_column])
    final_list = [] 
    for index, time in enumerate(df_list):
        if time >= self.start_time and time <= self.end_time:
            final_list.append(df.loc[index,column])
    return final_list

# Now, this list is extracted based on the self.start_time & self.end_time. 
trajectory_list_x = interval_extractor(time_column,self.start_time,self.end_time,trajectory_df,'x')
trajectory_list_y = interval_extractor(time_column,self.start_time,self.end_time,trajectory_df,'y')


#  distance = math.sqrt(pow(waypoint.pose.pose.position.x-animal_pose.pose.pose.position.x,2)+pow(waypoint.pose.pose.position.y-animal_pose.pose.pose.position.y,2))
def velocity_calc(time_column,self.start_time, self.end_time,df,column_x,column_y):
    df_list=list(df.loc[:,time_column])
    velocity_list_x = []
    velocity_list_y = []
    velocity_list_net = []
    velocity_time = []
    for index,time in enumerate(df_list):        
        if time >= self.start_time and time <= self.end_time:
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
# velocity_list_net,velocity_list_x,velocity_list_y,velocity_time = velocity_calc(time_column,self.start_time,self.end_time,trajectory_df,"x","y")
velocity_df = velocity_calc(time_column,self.start_time,self.end_time,trajectory_df,"x","y")

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
navigation_time = (self.end_time - self.start_time) * pow(10,-9)
print ("navigation_time",navigation_time)



image_path = dir_path+file_path+"/"+file_path+".png"
output_path =  dir_path+file_path+"/"+file_path+".txt"
with open(output_path, 'w') as f:
    # f.write("waypoint_distance",waypoint_distance)
    print ("waypoint_distance: {} ".format(waypoint_distance),file=f)    # Python 3.x
    print ("trajectory_distance: {} ".format(trajectory_distance),file=f)    # Python 3.x
    print ("TDR: {} ".format(trajectory_ratio),file=f)    # Python 3.x
    print ("navigation_time: {} ".format(navigation_time),file=f)    # Python 3.x
   
#     with open(output_path, 'w') as f:
#     # f.write("waypoint_distance",waypoint_distance)
#     print ("waypoint_distance: {} ".format(waypoint_distance),file=f)    # Python 2.x
#     print >> f, "trajectory_distance",trajectory_distance
#     print >> f, "TDR",trajectory_ratio
#     print >> f,"navigation_time",navigation_time
#     # print('Filename:', filename, file=f)


#____PLOTTING_____###
fig, ax = plt.subplots()
ax.plot(waypoint_list_x,waypoint_list_y,'ro-',label="Waypoints")
ax.plot(trajectory_list_x,trajectory_list_y,'b.-',label="Trajectory")
plt.xlabel('X distance',fontsize=22)
plt.ylabel('Y distance',fontsize=22)
#Plotting startig & ending poistions 
ax.scatter(trajectory_list_x[0],trajectory_list_y[0],s=100,marker='D',c='red',label = "Begin")
ax.scatter(trajectory_list_x[-1],trajectory_list_y[-1],s=100,marker='D',c='black',label = "End")
plt.title("Human Trajectory with Waypoint",fontsize=22)
plt.legend()
plt.savefig(image_path,bbox_inches='tight')
plt.show()
