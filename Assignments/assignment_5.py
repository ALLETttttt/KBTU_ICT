'''
The objective of this assignment is to clean the csv file of the attendance.
The path to the csv file is "attendance_to_clean.csv"
You can find it in the instruction folder.
List of installed and authorized packages :
    - csv
    - pandas
    - datetime
    - numpy
You cannot use other packages than the listed ones (except built-in default package in python).
You can write you code after this comment :
'''

# Your code here:

import pandas as pd
import csv
import datetime
import numpy as np


x = ['error','two','na','_']
BakesDataFrame = pd.read_csv("attendance_to_clean.csv", na_values = x)


for qq, ll in BakesDataFrame.iterrows():
    try:
        datetime.datetime.strptime(ll['DATE'],'%Y-%m-%d')
    except:
        BakesDataFrame.loc[qq, 'DATE'] = np.nan
        pass
    try:
        int(ll['NAME_STUDENT'])
        BakesDataFrame.loc[qq, 'NAME_STUDENT'] = np.nan
    except:
        pass
    if ll['DATE']== '1968-09-27' or ll['DATE']=='2020-10-07' or ll['DATE'] == '2022-01-13':
        BakesDataFrame.loc[qq,'KBTU_ID']=np.nan
    if ll['BEGIN_HOUR']==23 or ll['COUNT'] == 10:
        BakesDataFrame.loc[qq,'KBTU_ID']=np.nan

BakesDataFrame.dropna(subset = ['BEGIN_HOUR','COUNT','DATE','WEEK', 'KBTU_ID','TYPE','NAME_STUDENT'], inplace = True)

BakesDataFrame = BakesDataFrame.drop_duplicates()
BakesDataFrame["DATE"] = pd.to_datetime(BakesDataFrame['DATE'])
BakesDataFrame = BakesDataFrame.sort_values(by=['NAME_STUDENT', 'DATE', 'BEGIN_HOUR', 'WEEK'])

BakesDataFrame.reset_index(drop=True, inplace=True)
print(BakesDataFrame)
