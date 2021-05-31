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