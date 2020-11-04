# usr/bin/env python
__author__ = "Sandeep kumar Nayak"
__email__ = "nayak.sandeep@rm.is.tohoku.ac.jp"
__copyright__ = "Copyright 2020, Tadokoro Lab"

import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from typing import List,Dict
from sklearn.neighbors import KernelDensity
import seaborn as sns;sns.set()
import sys

class Datetime_Dataframe(object):
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.time_series = self.df.loc[:, '%time']

    # NOW CONVERT THE UNIX TIME TO LOCAL TIME AND DATE
    def number_extractor(self, number: np.int64) -> np.int64:
        """
        The ros time stamp is an appended time stamp of unix and somthing.
        The first 10 digits are the epoch timestamp.
        :param number:
        :return: np.int64
        """
        number = str(number)[:10]
        return np.int64(number)

    def unix_to_utc(self, unixtime: np.int64) -> datetime:
        utctime = datetime.utcfromtimestamp(unixtime).strftime('%Y-%m-%d %H:%M:%S')
        return utctime

    def convert_to_unix(self, series: pd.Series) -> pd.Series:
        unix = []
        # extracting each the unix time from each cell
        for number in series:
            unix.append(self.number_extractor(number))

        return pd.Series(unix, name='unix time')

    def convert_to_utc(self, series: pd.Series) -> pd.Series:
        from datetime import datetime
        utc = []
        # extracting each the unix time from each cell
        for number in series:
            utc.append(datetime.utcfromtimestamp(self.number_extractor(number)).strftime('%Y-%m-%d %H:%M:%S'))

        return pd.Series(utc, name='unix time')

    def utc_to_jst(self, series: pd.Series) -> pd.Series:
        from datetime import datetime
        from pytz import timezone
        import time

        jst = []
        # extracting each the unix time from each cell
        datetime_series = pd.to_datetime(series)
        for number in datetime_series:
            jst.append(time.ctime(number))

        return pd.Series(jst, name='unix time')

    def unix_to_jst(self, series: pd.Series) -> pd.Series:
        import time
        import datetime
        jst = []
        for number in series:
            jst.append(time.ctime(number))
        return pd.Series(jst, name='jst_time')

    def return_as_df(self, jst_series, unix_series):
        try:
            self.df.insert(1, "jst", jst_series)
        except ValueError:
            pass
        try:
            self.df.insert(2, "unix", unix_series)
        except ValueError:
            pass
        return self.df


# TODO : APPEND THE TWO DATAFRAME BASED ON TIMESTAMP, JOY AND SPATIAL


if __name__ == "__main__":
#----------------------------   VARIABLES ------------------------------------------

# field.buttons1 = right, field.buttons2 = left , field.buttons3 = center

# field.orientation.x, field.angular_velocity.x , field.linear_acceleration.x

#---------------------------------------------------------------------------------------

    # joy_path = '/home/kvothe/sandy/Animal_Behavior_Prediciton/data/ros_bag/2019-12-04-20-18-32/2019-12-04-20-18-32_joy.csv'
    # imu_path = '/home/kvothe/sandy/Animal_Behavior_Prediciton/data/ros_bag/2019-12-04-20-18-32/2019-12-04-20-18-32_spatial_imu.csv'
    joy_path = '/home/kvothe/sandy/Animal_Behavior_Prediciton/data/ros_bag/2019-12-04-20-33-31/2019-12-04-20-33-31_joy.csv'
    imu_path = '/home/kvothe/sandy/Animal_Behavior_Prediciton/data/ros_bag/2019-12-04-20-33-31/2019-12-04-20-33-31_spatial_imu.csv'

    joy_df = pd.read_csv(joy_path)
    time_series = joy_df.loc[:, '%time']

    convertclass1 = Datetime_Dataframe(joy_df)
    unix_series = convertclass1.convert_to_unix(time_series)
    utc_series = convertclass1.convert_to_utc(time_series)
    jst_series = convertclass1.unix_to_jst(unix_series)
    # print(jst_series.size)
    joy_final_df = convertclass1.return_as_df(jst_series, unix_series)

    # create imu df
    # convert respectively to date and time
    imu_df = pd.read_csv(imu_path)
    time_series2 = imu_df.loc[:, '%time']
    convertclass2 = Datetime_Dataframe(imu_df)
    unix_series2 = convertclass2.convert_to_unix(time_series2)
    jst_series2 = convertclass2.unix_to_jst(unix_series2)
    # print(jst_series2.size)
    imu_final_df = convertclass2.return_as_df(jst_series2, unix_series2)

#-------------------------------------------------------------------------
    # """
    # Data exploration column
    # """
    # print((joy_final_df.columns))
    # print(imu_final_df.columns)
    # # joy_final_df.describe()
    # # joy_final_df.memory_usage()
    # print(joy_final_df.max())

#-----------------------------------------------------------------------------



    #---------- TIME SELECTION ALOGRITHM ---------------------------------------

    # field.buttons1 = right, field.buttons2 = left , field.buttons3 = center

    # field.orientation.x, field.angular_velocity.x , field.linear_acceleration.x
    """
    For each of the unix timestamp in joy_final_df,
    """
    # variables required , joy_final_df, reduced_joy_df,
    right_button = 'field.buttons1'
    left_button = 'field.buttons2'
    middle_button = 'field.buttons3'
    # todo: Make this time selection as a function
    time_list = list(joy_final_df.loc[:,'unix'])
    reduced_joy_list = []
    for index, time in enumerate(time_list):
        try:
            if time_list[index] == time_list[index +1]:
                continue
            else:
                reduced_joy_list.append(list(joy_final_df.iloc[index,:]))
                continue
        except IndexError:
            reduced_joy_list.append(list(joy_final_df.iloc[index,:]))
    # print(reduced_joy_list)
    reduced_joy_df = pd.DataFrame(reduced_joy_list,columns=list(joy_final_df.columns))
    print(reduced_joy_df)


#------------------------------- TIME CONVERSION ALOGRITHM FOR PLOTTING AND SYCING WITH IMU_FINAL_DF---------------------------------------

    # finding the miliseconds from 19 digit unix
    imu_timestamp_milliseconds_list= [data//(10**6) for data in  imu_final_df.loc[:,'%time']]
    reduced_joy_timestamp_milliseconds_list = [data//(10**6) for data in  reduced_joy_df.loc[:,'%time']]

    def start_time_diff_column(df:pd.DataFrame,x : List,column_name = 'time_diff', position = 0):
        """
        This function will convert the timestamp to timedelta with respect to the imu start time
        :param df:
        :param x:
        :param column_name:
        :param position:
        :return:
        """
        temp_list = []
        for index,time in enumerate(x):
            try:
                if index==0:
                    temp_list.append(0.0)
                else:
                    temp_list.append((x[index]-x[0]))
            except IndexError:
                break
        # temp_series = pd.Series(temp_list, name = column_name)
        # df.insert(position, column=temp_list, value=temp_list, allow_duplicates=False)
        return temp_list
    def sync_with_imu_timestamp(imu_time_list : List, joy_time_list : List):
        """
        This function will sync the second time list: joy_time list to first reference
        ie. the imu time list
        :param imu_time_list: preferably a millisecond converted time list of imu_joy unix time column
        :param joy_time_list: preferably a millisecond converted time list of imu_joy unix time column
        :return: list of milliseconds time difference of second lsit wtr first list ( eg joy wtr imu )

        """
        temp_list = []
        for index, time in enumerate(joy_time_list):
            try:
                temp_list.append((joy_time_list[index]-imu_time_list[0]))
            except IndexError:
                print("IndexError at {}".format(index))
        return  temp_list

    def timedelta_with_itself(time_list: List) -> List:
        """
        This function is mostly used for calculating deltaT of the same time list of same series.
        :param time_list:
        :return:
        """
        temp_list = []
        for index , time in enumerate(time_list):
            try:
                if index==0:
                    temp_list.append((0.0))
                else:
                    temp_list.append(time_list[index]-time_list[index-1])
            except IndexError:
                pass
        return  temp_list

    # this are list that stores the difference in miliseconds and are as long as their respected dfs.
    imu_milliseconds_timedelta = start_time_diff_column(imu_final_df,imu_timestamp_milliseconds_list)
    reduced_joy_milliseconds_timedelta_wtr_imu = sync_with_imu_timestamp(imu_timestamp_milliseconds_list,reduced_joy_timestamp_milliseconds_list)
    imu_milliseconds_timedelta_itself = timedelta_with_itself(imu_timestamp_milliseconds_list)

#-------------------------------- JOINING THE TIME DIFFERENCE IN MILLISECONDS IN BOTH THE IMU DATAFRAME AND REDUCED JOY DATAFRAME ----------------------------

    imu_final_df.insert(1,'timedelta_milliseconds',pd.Series(imu_milliseconds_timedelta), allow_duplicates = False)

    try:
        reduced_joy_df.insert(1
                              ,'timedelta_milliseconds_wtr_imu',reduced_joy_milliseconds_timedelta_wtr_imu,allow_duplicates = False)
    except ValueError:
        pass

    # Adding the  time delta to imu final df
    imu_final_df.insert(2,'relative_timedelta_milliseconds', imu_milliseconds_timedelta_itself, allow_duplicates = False)

#----------------------------------------------------RATE OF ANGULAR VELOCITY ------------------------------------------------------------------------------------
    def rate_wtr_time(df: pd.DataFrame, var_column_name : str,time_column_name :str, time_interval : int) -> List:
        # field.buttons1 = right, field.buttons2 = left , field.buttons3 = center

        # field.orientation.x, field.angular_velocity.x , field.linear_acceleration.x
        temp_list = []
        time_column_list = list(df.loc[:,time_column_name])
        var_column_list = list(df.loc[:,var_column_name])

        for index,time in enumerate(time_column_list):
            try:
                if index == 0 :
                    # I am making the rate of the firest element same that o the second element.
                    temp_list.append(((var_column_list[index + 1] - var_column_list[index])/
                                      ((time_column_list[index + 1] -time_column_list[index])*time_interval)))
                else :
                    # starting from the second element, the rate is second elemnet - previous element. ie
                    # with this rate it rached this leve.
                    temp_list.append(((var_column_list[index ] - var_column_list[index - 1]) /
                                      ((time_column_list[index ] - time_column_list[index - 1]) * time_interval)))

            except:
                print("{} at {}".format(sys.exc_info()[0], index))
        return temp_list
    var_column_name = 'field.angular_velocity.x'
    time_column_name = '%time'
    time_interval_rate_of_angular_velocity = 10 ** (-9) # f
    rate_of_angular_velocity_x_list = rate_wtr_time(imu_final_df, var_column_name, time_column_name,time_interval_rate_of_angular_velocity)


#--------------------------------------------IDENTIFY START TIME AND END TIME OF EXPERIMENT ---------------------------------------------------------------

    def start_end_time_detection(df: pd.DataFrame) -> list:

        """
        This function will return time list where the start and end of an experimtnt

        :return:
        """

        pass
    #

    #finding the maximum value of w
    # print("max value of w is {}".format(imu_final_df.loc[:,'field.angular_velocity.x'].max(numeric_only = float)))

    """
    ISSUES : FOR FINDING START AND END TIME DETECTION 
    1. For change detection, I was thinking of having amplitude threshold , but series.max() is giving me inf. 
    ('count', 152468.0) ('mean', nan) ('std', nan) ('min', -inf) ('25%', -0.04688478726895) ('50%', 0.004067070782185) ('75%', 0.033556154929125) ('max', inf)
    Soln: 1. search for inf value find the time stamp
        2. drop the rows having infinite value if inf is not during start or end of exp . 
        3. find max() and then put the threshold 10% below max value, or count the number that lies in 10 %, 20% etc. and then put the threshold. 
    """
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   DONT MERGE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#-----------------------------------------------------MERGING IMU_FINAL_DF WITH REDUCED_JOY_DF------------------------------------------------------
    #imu_joy_tasu_df = pd.merge(imu_final_df,joy_final_df,left_on='unix',right_on='unix',sort=False,how='outer',validate='many_to_one')
    # merged_imu_reduced_joy = pd.merge(imu_final_df,reduced_joy_df,left_on='unix',right_on='unix',sort=False,how='outer',validate='many_to_one')

#----------------------------------------------EXTRACTING RESPONSE FOR LEFT, RIGHT AND FRONT LIGHT SIGNALLING ALGORITHM ---------------------------------------------------------------
    def extract_lightsignalled_imu_data(imu_df:pd.DataFrame,joy_df:pd.DataFrame, timestamp_column : str,extract_data_column: str,button_column: str ,number_of_data = 200 ):


        count = 0
        recorded_df = pd.DataFrame(columns=['count',timestamp_column,extract_data_column,button_column])

        for joy_index , button_value  in enumerate(joy_df.loc[:,button_column]): # iterating over the joy df button value
            #identify right button
            if button_value == 1.0:
                extract_data_count = 0
                print("found button at {}".format(joy_index))
                #loop over the imu_df.%time to find the time greater then this time. and take a the data of 200

                for imu_index, imu_time in enumerate(imu_df.loc[:,timestamp_column]):
                    if imu_time >= joy_df.loc[joy_index,timestamp_column] and extract_data_count < number_of_data : # we will be collecting 200 data
                        _dict = {'count':count,
                                 timestamp_column:imu_df.loc[imu_index,timestamp_column],
                                 extract_data_column: imu_df.loc[imu_index,extract_data_column],
                                 button_column:joy_df.loc[joy_index,button_column]}
                        recorded_df = recorded_df.append(_dict,ignore_index=True)

                        extract_data_count += 1
                    else:
                        continue
                # break this loop after 200 samples extracted , check next botton
                count +=1

                #if w >0 then record till w > 0
                # else make anothr list
        return recorded_df
    ##_________________UNCOMMENT IT WHEN YOU NEED TO UPDATE EXTRAXTED_LIGHTSIGNALLED_________________________________________

    # extracted_lightsignalled_imu_data = extract_lightsignalled_imu_data(imu_df=imu_final_df,
    #                                                                     joy_df=reduced_joy_df,
    #                                                                     timestamp_column = '%time',
    #                                                                     extract_data_column ='field.angular_velocity.x',
    #                                                                     button_column=right_button,number_of_data=200)
    # #addiing milliseconds difference wtr imu_final
    # # making a millisecond list for the extracted data
    # extracted_lightsignalled_imu_data_timestamp_milliseconds_list = [data//(10**6) for data in  extracted_lightsignalled_imu_data.loc[:,'%time']]
    # # now calculating the timedelta wtr imu
    # extracted_lightsignalled_imu_data_milliseconds_timedelta_wtr_imu = sync_with_imu_timestamp(imu_timestamp_milliseconds_list,extracted_lightsignalled_imu_data_timestamp_milliseconds_list)
    # # inserting into the data frame
    # try:
    #     extracted_lightsignalled_imu_data.insert(1, 'timedelta_milliseconds_wtr_imu', extracted_lightsignalled_imu_data_milliseconds_timedelta_wtr_imu,
    #                           allow_duplicates=False)
    # except ValueError:
    #     pass
    # extracted_lightsignalled_imu_data.to_csv('/home/kvothe/sandy/Animal_Behavior_Prediciton/data/ros_bag/extracted_lightsignalled_imu_data_harata.csv')
    extracted_lightsignalled_imu_data = pd.read_csv('/home/kvothe/sandy/Animal_Behavior_Prediciton/data/ros_bag/extracted_lightsignalled_imu_data_harata.csv')

    ###-----------------------------FINDDING THE FREQUECNDY OF THE TIME DELAY ---------------------------------------
    statechange = False
    _dict2 = {}

    response_time_df = pd.DataFrame(columns=['count','response_time'])

    for index, count in enumerate(extracted_lightsignalled_imu_data.loc[:,'count']):
        # print(time)
    #todo: I will explain the algorithm as a comment later.

        if index == 0:
            base_time = extracted_lightsignalled_imu_data.loc[index,'timedelta_milliseconds_wtr_imu']
        elif count == 0.0:
            prev_velocity = extracted_lightsignalled_imu_data.loc[index-1 , 'field.angular_velocity.x']
            current_velocity = extracted_lightsignalled_imu_data.loc[index, 'field.angular_velocity.x']
            if statechange == False :
                if (prev_velocity * current_velocity) < 0:
                    new_time = extracted_lightsignalled_imu_data.loc[index,'timedelta_milliseconds_wtr_imu']
                    time_delta = new_time - base_time
                    _dict2= {'count': count,
                             'response_time':time_delta}
                    response_time_df = response_time_df.append(_dict2,ignore_index=True)
                    statechange = True
        else:
            previous_count = extracted_lightsignalled_imu_data.loc[index-1,'count']
            if previous_count != count :
                base_time = extracted_lightsignalled_imu_data.loc[index,'timedelta_milliseconds_wtr_imu']
                statechange = False
            else:
                prev_velocity = extracted_lightsignalled_imu_data.loc[index - 1, 'field.angular_velocity.x']
                current_velocity = extracted_lightsignalled_imu_data.loc[index, 'field.angular_velocity.x']
                if statechange == False: # putting state change above because if there is a state change in between ,
                    # then it will be skipped.
                    if (prev_velocity * current_velocity) < 0:
                        new_time = extracted_lightsignalled_imu_data.loc[index, 'timedelta_milliseconds_wtr_imu']
                        time_delta = new_time - base_time
                        _dict2 = {'count': count,
                                  'response_time': time_delta}
                        response_time_df = response_time_df.append(_dict2, ignore_index=True)
                        statechange = True


# # #-----------------------------KDE AND PLOTTING :FINDING THE FREQUECNY OF THE ANGLUAR VELOCITY,---------------------------------
#    ###-------------------------PREPARING DATA -----------------------------------------------
    frequency_extraction_series = extracted_lightsignalled_imu_data.groupby(by='count')['field.angular_velocity.x'].mean()
    frequency_extraction_df = frequency_extraction_series.to_frame(name='mean_field.angular_velocity.x')
    ## bins = np.arange(-2,2,0.1)
    ## frequency_extraction_df['binned ']= pd.cut(frequency_extraction_df['mean_field.angular_velocity.x'],bins)
    ## import scipy
    ## kernel_density_estimation = frequency_extraction_series.plot.kde()
    frequency_extraction_array = frequency_extraction_df.values
    x_d = np.linspace(-2, 2, 800)
    """ # This is for the x axis,but mostly used for quering by KernelDensity
    and as a resolution.
    """
   ###-------------------------OPTIMUM BANDWIDTH -----------------------------------------
    from sklearn.model_selection import GridSearchCV
    #todo: improvise the bandwidth sampling range be automating it according to the data type.
    grid = GridSearchCV(KernelDensity(),{'bandwidth':np.linspace(0,1.0,20)},cv = 2)
    grid.fit(frequency_extraction_array[:, ])
    bandwidth = float(grid.best_params_['bandwidth'])
    print(grid.best_params_)
    ###------------------------ APPLYING THE MODE----------------------------------------

    ### Here we are trying to take the frequency data and fit the data .
    kde = KernelDensity(kernel='gaussian', bandwidth=bandwidth).fit(frequency_extraction_array)
    #using tophat kernel (rectangular)
    # kde = KernelDensity(kernel='tophat', bandwidth=bandwidth).fit(frequency_extraction_array)
    logprob = kde.score_samples(x_d[:, None])  ### score_samples is basicall log normal density dist.
    exp_logprob = np.exp(logprob)
    pdf_sample_mean = np.mean(exp_logprob)
    pdf_sample_std = np.std(exp_logprob)
    plt.fill_between(x_d, (exp_logprob),
                     alpha=0.5)  ### So, here, we find the exp(lognorm) for getting the standard normal distribution
    plt.xlabel('Right Turn Angular Velocity rad/sec')
    plt.ylabel("Non-Parametric KDE estimated values")
    plt.title("Non-parametric KDE for Right turn angular velocity")

    plt.show()

#     # todo : modularizing the different models and the plotting .
#     # todo: finding the mean and standard deviation and skewness

#

# # #-----------------------------FINDING THE FREQUECNY OF THE TIME DELAY,KDE & PLOTTING ---------------------------------


   ###-------------------------PREPARING DATA -----------------------------------------------
    time_delay_array=response_time_df['response_time'].values.reshape(-1,1)
    x_d = np.linspace(np.min(time_delay_array), np.max(time_delay_array), 1000)

     # This is for the x axis,but mostly used for quering by KernelDensityd as a resolution.

   ###-------------------------OPTIMUM BANDWIDTH -----------------------------------------
    from sklearn.model_selection import GridSearchCV
    grid = GridSearchCV(KernelDensity(),{'bandwidth':np.linspace(-400,1000,50)},cv = 2)
    grid.fit(time_delay_array[:, ])
    bandwidth = float(grid.best_params_['bandwidth'])
    print(grid.best_params_)
    ###------------------------ APPLYING THE MODE----------------------------------------

    ### Here we are trying to take the frequency data and fit the data .
    kde = KernelDensity(kernel='gaussian', bandwidth=bandwidth).fit(time_delay_array)
    logprob = kde.score_samples(x_d[:, None])  ### score_samples is basicall log normal density dist.

    plt.fill_between(x_d, np.exp(logprob),
                     alpha=0.5)  ### So, here, we find the exp(lognorm) for getting the standard normal distribution
    plt.xlabel('Right Turn Time delay response millisec')
    plt.ylabel("Non-Parametric KDE estimated values")
    plt.title("Non-parametric KDE for Right turn Time delay response")
    plt.show()





#---------------------------------PLOTTING --------------------------------------------------------------------------------------------------------------
'''

    # lines = imu_final_df.plot.line(x=imu_final_df2, y='field.orientation.x')
    angular_velocity_x = list(imu_final_df.loc[:, 'field.angular_velocity.x'])
    angular_acceleration_x = list(imu_final_df.loc[:, 'field.angular_velocity.x'])
    left_button_list = list(reduced_joy_df.loc[:,left_button])
    middle_button_list = list(reduced_joy_df.loc[:,middle_button])
    right_button_list = list(reduced_joy_df.loc[:,right_button])

# # variables for checking out if merged data and reduced joy df are proper or not
#     merged_timedelta_milliseconds_list = list(merged_imu_reduced_joy.loc[3000:10000,'timedelta_milliseconds'])
#     merged_angular_velocity_x = list(merged_imu_reduced_joy.loc[:,'field.angular_velocity.x'])
#     merged_right_button_list = list(merged_imu_reduced_joy.loc[:,right_button])

## Variables for checking out extracted_lightsignalled_imu_data
   # extracted_lightsignalled_imu_data_milliseconds_timedelta_wtr_imu
    extracted_lightsignalled_imu_data_angular_velocity = list(extracted_lightsignalled_imu_data.loc[:,'field.angular_velocity.x'])
    extracted_lightsignalled_imu_data_milliseconds = list(extracted_lightsignalled_imu_data.loc[:,'timedelta_milliseconds_wtr_imu'])

    # fig, ax = plt.subplot()
    plt.figure(1)
    plt.subplot(211)
    plt.plot(imu_milliseconds_timedelta, angular_velocity_x, label ='IMU velocity x')
    plt.scatter(extracted_lightsignalled_imu_data_milliseconds,
                extracted_lightsignalled_imu_data_angular_velocity, label ='extracted_IMU velocity x' ,c = 'g')
    # plt.stem(reduced_joy_milliseconds_timedelta_wtr_imu,[item * -1 for item in left_button_list],linefmt='k-', markerfmt='ko', basefmt='b--', label = 'left button')
    # plt.stem(reduced_joy_milliseconds_timedelta_wtr_imu, [item * 0.5 for item in middle_button_list],linefmt='g-', markerfmt='go', basefmt='b--', label = 'middle button')
    plt.stem(reduced_joy_milliseconds_timedelta_wtr_imu,right_button_list,linefmt='r-', markerfmt='ro', basefmt='b--', label = 'right button')
    plt.legend()
    plt.xlabel('Time in Microseconds')
    plt.ylabel('X angular velocity ')

    # plt.subplot(212)
#
# # checking if the right button mergering is done properly or not
#     plt.plot(list(extracted_lightsignalled_imu_data.loc[:,'timedelta_milliseconds_wtr_imu']), list(extracted_lightsignalled_imu_data_angular_velocity[:,'field.angular_velocity.x']), label ='IMU velocity x')
#     plt.stem(extracted_lightsignalled_imu_data_milliseconds_timedelta_wtr_imu, [item * 2 for item in merged_right_button_list], linefmt='r-',
#              markerfmt='ro', basefmt='r--', label='right button of merged df')
#     plt.stem(reduced_joy_milliseconds_timedelta_wtr_imu,right_button_list,linefmt='k-', markerfmt='ko', basefmt='k--', label = 'right button of just reduced joy')
#     # plt.stem(reduced_joy_milliseconds_timedelta_wtr_imu, [item * 0.5 for item in middle_button_list], linefmt='g-',
#     #          markerfmt='go', basefmt='b--', label='middle button')
#     # plt.stem(reduced_joy_milliseconds_timedelta_wtr_imu, right_button_list, linefmt='r-', markerfmt='ro', basefmt='b--',
#     #          label='right button')
#     plt.legend()
#     plt.grid()
#     plt.xlabel('Time in Microseconds')
#     plt.ylabel('X angular velocity ')



# #--------------------------------------------------------------------------------------------------
#     plt.plot(imu_milliseconds_timedelta, rate_of_angular_velocity_x_list, label='IMU velocity x')
#     plt.stem(reduced_joy_milliseconds_timedelta_wtr_imu,[item * 100 for item in left_button_list],linefmt='k-', markerfmt='ko', basefmt='b--', label='left button')
#     plt.stem(reduced_joy_milliseconds_timedelta_wtr_imu, [item * 100 for item in middle_button_list],linefmt='g-', markerfmt='go', basefmt='b--', label='middle button')
#     plt.stem(reduced_joy_milliseconds_timedelta_wtr_imu, [item * 100 for item in right_button_list], linefmt='r-', markerfmt='ro', basefmt='b--',label='right button')
#     plt.legend()
#     plt.grid()
#     plt.xlabel('Time in Microseconds')
#     plt.ylabel('Rate of Angular Velocity X')
#     plt.ylim(-200,200)

    plt.show()
    #
'''

#---------------------------------------------------------------------




"""
    When count of jthe 200 hz data more the n180 then the value for the buttion field is considered ,
    if it is considered, then from the start to end of the button value , find the average of the angular
    velocy and acceleration field. 3 such disribution . 
    
"""
    # import string
    # test_time_list = []
    #
    # for i, right_button in enumerate(imu_joy_tasu_df.loc[:,'field.buttons1']):
    #     if right_button == 1.00:
    #         test_time_list.append(imu_joy_tasu_df.loc[i, 'jst_imu'])
    #         # print(i)
    #         # print(type(right_button))
    #
    # print(pd.Series(test_time_list))
    # test_time_list2 = []
    # for i, right_button in enumerate(joy_final_df.loc[:,'field.buttons1']):
    #     if right_button == 1.00:
    #         test_time_list2.append(joy_final_df.loc[i, 'jst'])
    #         # print(i)
    #         # print(type(right_button))
    #
    # print(pd.Series(test_time_list2))

    # print(type(imu_joy_tasu_df.loc[120468:,'field.buttons4']))


#-------------------------------------DO NOT MERGE ------------------------
    # append with key unix
    # imu_joy_tasu_df = imu_final_df.join(joy_final_df.set_index('unix'), on='unix', lsuffix='_imu', rsuffix='joy')
    # imu_joy_tasu_df = pd.merge(imu_final_df,joy_final_df,left_on='unix',right_on='unix',sort=False,how='outer',validate='many_to_one')
    ## Saving the data as csv
    # joy_final_df.to_csv(r'../data/ros_bag/joy_final_df.csv', header=True)
    # imu_final_df.to_csv(r'../data/ros_bag/imu_final_df.csv', header=True)
    # imu_joy_tasu_df.to_csv(r'../data/ros_bag/imu_joy_tasu_df.csv',header=True)
    # extracted_lightsignalled_imu_data.to_csv(r'../data/ros_bag/extracted_lightsignalled_imu_data.csv',header=True)
#-------------------------------------------------------------------------------

pass
