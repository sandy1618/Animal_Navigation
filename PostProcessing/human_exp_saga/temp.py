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

##____________COMMON FUNCTIONS __________________________--
## Common Class

import pandas as pd
class Datetime_Dataframe:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
    
  
    
    def time_col_concat(self,col1,col2,new_col_name):
        if self.df[col1].dtype == 'int64':
            self.df[col1]= self.df[col1].astype(str)
        if self.df[col2].dtype == 'int64':
            self.df[col2] = self.df[col2].astype(str)
        temp = self.df[col1] + self.df[col2]
        temp = temp.astype('int64')
        try:
            self.df.insert(1,new_col_name,temp)
        except: 
            pass
        return self.df
        
    def time_diff(self, time_col, ref_time, new_col_name):
        
        temp_nano = self.df[time_col] - ref_time
        temp_milli = temp_nano*math.pow(10,-6)
        temp = temp_nano*math.pow(10,-9)
        try:
            self.df.insert(2,new_col_name,temp)
            self.df.insert(3,new_col_name+"milli",temp_milli)
            self.df.insert(4,new_col_name+"nano",temp_nano)
        except:
            pass
        return self.df


def interval_extractor(time_column, start_time, end_time, df, column):
    """# Exctract only the column defined by start_time, end_time column. """
    df_list = list(df.loc[:,time_column])
    final_list = [] 
    for index, time in enumerate(df_list):
        if time >= start_time and time <= end_time:
            final_list.append(df.loc[index,column])
    return final_list

def velocity_calc(time_column,start_time, end_time,df,column_x,column_y):

#  distance = math.sqrt(pow(waypoint.pose.pose.position.x-animal_pose.pose.pose.position.x,2)+pow(waypoint.pose.pose.position.y-animal_pose.pose.pose.position.y,2))
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


home = expanduser("~")
# dir_path = home + '/Animal_Navigation/data/tamura/'
dir_path = os.getcwd() + "/"
file_df = pd.read_csv(dir_path + '/Exp_time_mapping.csv')
light_df = file_df.iloc[0:8,1:7]
audio_df = file_df.iloc[0:8,7:13]


threshold_list = []
exp_date_list = []
tdr_list=[]
navigation_time_list=[]


for col_index,col_val in enumerate(light_df.iloc[0,1:3]):
    # print(col_val)
    for row_index,row_val in enumerate(light_df.iloc[1:3,col_index]):
        

        file_path=row_val
        # This is where the entire list for tdr calculation & time calculation . 
        state_path = dir_path + file_path + '/_slash_state.csv' 
        waypoint_path = dir_path + file_path + '/_slash_move_base_slash_goal.csv' 
        trajectory_path = dir_path + file_path + '/_slash_map_slash_robot_pose.csv' 
        signal_path = dir_path + file_path + '/_slash_cmd_sig.csv'

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




        # Now, this list is extracted based on the start_time & end_time. 
        trajectory_list_x = interval_extractor(time_column,start_time,end_time,trajectory_df,'x')
        trajectory_list_y = interval_extractor(time_column,start_time,end_time,trajectory_df,'y')



        # # velocity_list_net,velocity_list_x,velocity_list_y,velocity_time = velocity_calc(time_column,start_time,end_time,trajectory_df,"x","y")
        # velocity_df = velocity_calc(time_column,start_time,end_time,trajectory_df,"x","y")


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
        
        ## Adding the TDR & navigation_time to the list & also appending the threshold.
        threshold_list.append(col_val) # Appending threshold list. 
        tdr_list.append(trajectory_ratio)
        navigation_time_list.append(navigation_time)

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

      
print(threshold_list)
print(tdr_list)
print(navigation_time_list)

result_df = pd.DataFrame(
    {'threshold':threshold_list,
    'tdr':tdr_list,
    'navigation_time':navigation_time_list
    })
result_df.to_csv( dir_path +'results/light.csv')

