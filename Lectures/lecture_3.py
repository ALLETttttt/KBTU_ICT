#!/usr/bin/env python
# coding: utf-8
from distutils.sysconfig import get_python_lib
# In[ ]:


#information : absent from 22/09 until 3/10 included (=> lecture and practice => Teams or videos)
#office hours tursday 29/09 from 9 to 11/12


# # Creating a DataFrame

# In[1]:


from distutils.sysconfig import get_python_inc
from sysconfig import get_python_version
import pandas as pd
print(pd.__version__)


# ## Using a dictionnary

# In[ ]:


# Data :
# Brand : 'Coca', 'pepsi', 'Sprite', 'water'
# Taste : 5, 6, 9, 8
# Sugar content : 'high', 'high', 'high', 'low'
# YOUR TURN : Create a dataframe from the dictionnary (10 minutes) => 11:20
df = pd.DataFrame ({  ...  })


# In[2]:


# Create the dataframe directly with dictionary
df = pd.DataFrame ({
        'Brand' : ['Coca', 'pepsi', 'Sprite', 'water'],
        'Taste': [5, 6, 9, 8],
        'Sugar_content' : ['high', 'high', 'high', 'low']
                })
print(df)
#Do not use dict as dictionary (this is like int, float)


# In[5]:


# Take csv data to dictionnary adn create dataframe
import csv
with open(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_3\Apple_price_csv.csv", 'r') as file:
    csvfile = csv.DictReader(file)
    df = pd.DataFrame(csvfile)
    
print(df)


# ## Using a list

# In[ ]:


# Data :
# Brand : 'Coca', 'pepsi', 'Sprite', 'water'
#Taste : 5, 6, 9, 8
#Sgar content : 'high', 'high', 'high', 'low'
#YOUR TURN : 
#Create a dtaframe from the lists (10 minutes) => 11:33
#Without using any dictionary
brand = ['Coca', 'pepsi', 'Sprite', 'water']
taste = [5, 6, 9, 8]
sugar_content = ['high', 'high', 'high', 'low']
df = pd.DataFrame(  ...  )


# In[6]:


# Create the lists
brand = ['Coca', 'pepsi', 'Sprite', 'water']
taste = [5, 6, 9, 8]
sugar_content = ['high', 'high', 'high', 'low']


# In[7]:


#Create dataframe from lists
# with pd.DataFrame()
df = pd.DataFrame([brand, taste, sugar_content] )
print(df)
#dataframe is waiting for [line1, line2, line3, ...]


# In[8]:


#The zip function
list0 = [0,1,2]
list1 = ['a', 'b', 'c']
list2 = ['g', 'h', 'k']
print(list(zip(list0, list1, list2)))


# In[ ]:


#YOUR TURN
# Come back to your previous dataframe and use the zip function (5 minutes) 11:38


# In[10]:


#Creation of dataframe with the zip function
df = pd.DataFrame(list(zip(brand, taste, sugar_content)), columns = ['Brand', 'Taste', 'Suagr_content'])
print(df)
#Do not do list = [kxsvjxfmb] it's like doing => print = 5


# In[15]:


#With the csv file (easier)
with open(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_3\Apple_price_csv.csv", 'r') as file:
    csvfile = csv.reader(file)
    columns_name = csvfile.__next__()
#     print(columns_name)
    df = pd.DataFrame(csvfile,  columns = columns_name)
    
print(df)


# ## Using read_csv method

# In[20]:


#create dataframe from read_csv method
df = pd.read_csv(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_3\Apple_price_csv.csv")
print(df)


# In[44]:


# with the date in datetime object

df = pd.read_csv(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_3\Apple_price_csv.csv" , 
                  parse_dates = ['Date'])
print(type(df['Date'][0]))


# # Modify the dataframe

# In[45]:


# Change the column names (2 methods)
df.columns = ['Date', 'Open_price', 'High_price', 'Low_price', 'Close_price', 'Adj Close', 'Volume']
df = df.rename(columns = {'Date' : 'Date_time'})
print(df)


# In[46]:


#sort values
df = df.sort_values('Open_price')
print(df)


# In[39]:


# Reset index of dataframe
df = df.reset_index(drop = True)
print(df)


# In[43]:


#Use your own index: (set_index function)
# df = df.set_index(['Date_time'])
print(df)


# In[47]:


# use several indexes
df = df.set_index(['Date_time', 'Open_price'])
print(df)


# In[86]:


#Your TURN
#Use your csv data to get your df and put dates as index (10 minutes)
#break at 12:00
df = pd.read_csv(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_3\Apple_price_csv.csv" , 
                  parse_dates = ['Date'])
# df = df.set_index(['Date'])
print(df)


# In[49]:


# Why indexes and not columns (use %timeit function)
get_python_inc().run_line_magic('timeit', "print('hi')")


# In[53]:


#display columns of dataframe (2 methods)
get_python_version().run_line_magic('timeit', "a = df[df['Open'] == 28.057501]")


# In[54]:


get_python_inc().run_line_magic('timeit', 'a = df.loc[2]')


# In[56]:


#Adding a new columns to your DataFrame
df['name'] = ['Gaetan' for i in range(0,1763)]
df['surname'] = 'Chardon'
print(df)


# In[64]:


# Apply a function to your dataframe
# df['2_times_open'] = df['Open'] * 2
def my_function(x):
    if x >170:
        return x*2
    else:
        return x
df['Open_modified'] = df['Open'].apply(my_function)
print(df)


# In[69]:


# iterate on a Dataframe
for index, item in df.iterrows():
    if index == 5:
        print(item['Date'])


# In[77]:


# Concatenate two dataframes
df1 = pd.DataFrame ({
        'Brand' : ['Coca', 'pepsi', 'Sprite', 'water'],
        'Taste': [5, 6, 9, 8],
        'Sugar_content' : ['high', 'high', 'high', 'low']
                })
df2 = pd.DataFrame ({
        'Brand' : ['Coca', 'dfd', 'df', 'wsdgi'],
        'Taste': [5, 5, 1, 0],
        'Sugar_content' : ['high', 'medium', 'high', 'low']
                })
# print(df1, "\n", df2)

df = pd.concat([df1, df2])
# print(df)
df = df.reset_index(drop = True)
print(df)


# In[79]:


# Delete the duplicate drop_duplicates function (see doc)
df = df.drop_duplicates()
print(df)


# # Save the Dataframe

# In[81]:


#Save it to excel
writer = pd.ExcelWriter(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_3\df.xlsx")
df.to_excel(writer, 'DataFrame')
writer.save()


# In[87]:


#SAve it to csv
df.to_csv(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_3\df.csv", index = False)
df = pd.read_csv(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_3\df.csv")
print(df)


# In[88]:


# save it to json
df.to_json(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_3\df.json")


# # Useful functions

# In[89]:


# Getting info about the dataframe
print(df.info())


# In[90]:


# Getting shapes of dataframe
print(df.shape)


# In[91]:


# description of the dataframe
print(df.describe())


# In[97]:


# Count similar values (.value_counts() method)
print(df['Open'].value_counts())


# In[98]:


# get correlation
print(df.corr())


# # pip install matplotlib

# In[99]:


# Quick plotting
df.plot(x = 'Date', y = 'Open')
#pip install matplotlib


# In[ ]:


#YOUR TURN 
#Plot the evolution of volume exchanged through the time of your csv file (10 minutes)
# I will speak bout assignment at 12:45

