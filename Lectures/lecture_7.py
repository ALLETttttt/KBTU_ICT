# # Lecture 7 : Data cleaning

import pandas as pd
import numpy as np

# Read csv file into a pandas dataframe
df = pd.read_csv(r"C:\Users\user\Downloads\Apple_price_to_clean.csv")
print(df)

#Find the standard missing values isnull function
print(df.isnull().sum().sum())

#Non standard missing values : na_values in the read_csv function
#use of unique function to identify them
missing_values = ['na', '--']
df = pd.read_csv(r"C:\Users\user\Downloads\Apple_price_to_clean.csv", na_values = missing_values)
print(df)
print(df.isnull().sum().sum())


#Unexpected format missing values : check if value can be int for example
for index, lines in df.iterrows():
    try:
        a = int(lines['OWN_OCCUPIED'])
        print(a)
        df.iloc[3, 3] = np.nan
    except:
        pass

missing_values = ['-', 'ERROR']
df = pd.read_csv(r"C:\Users\user\Downloads\Apple_price_to_clean.csv", na_values = missing_values)
print(df.isnull().sum().sum())

for index, lines in df.iterrows():
    try:
        a = int(lines['Date'])
        print(a)
        df.loc[index, 'Date'] = np.nan
    except:
        pass
print(df.head(20))

#delete lines with dropna with subset and inplace aeguments
# df = df.dropna()
# print(df)



# Location based replacement with the loc function
df.loc[0, 'NUM_BATH'] = 1
print(df)

# Replace missing values with a number (fillna() function with inplace arg)
df.fillna(0, inplace = True)
print(df)


#Replacing the missing values with a median 
#(calculate median and then use the replace with a number)


print(df['Open'].mean())
df['Open'].fillna(df['Open'].mean(), inplace = True)
print(df)

#Replacing the values by the one before or after : df.fillna(method='bfill')
df['Open'].fillna(method = 'bfill', inplace = True)
print(df)

#YOUR TURN 5 minutes => 12:27
#replace all the missing values in the previous dataframe with the frontfilling (ffill) method 
#put 0 for the first ones
df.fillna(method='bfill', inplace = True)
df.fillna(0, inplace = True)
print(df)


#Use the drop() function with inplace and axis arg
df.drop(['Open'], axis = 1, inplace = True)
print(df)

#Use the drop duplicates to remove useless lines
df.drop_duplicates(inplace = True)
print(df)



#YOUR TURN 5 minutes
#Drop all duplicates in your df
#get number of rows
#drop duplicates
#get number of row again
df.drop_duplicates(inplace = True)
print(df)




#With the describe method
print(df.describe())



#select the df in the range
# df = df[df['SQ_M'] < 10000]
# df.plot(y = 'SQ_M')

#YOUR TURN 10 minutes
#Find the outliers in your dataset and remove them
import pandas as pd
missing_values = ['-', 'ERRROR']
df = pd.read_csv(r"C:\Users\user\Downloads\Apple_price_to_clean.csv", na_values = missing_values)
df.drop_duplicates(inplace = True)
df = df[df['High'] > 0]
print(df)
print(df.describe())


df = df[df['Low'] < 200]


