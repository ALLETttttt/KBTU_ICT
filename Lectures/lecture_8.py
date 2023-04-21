#!/usr/bin/env python
# coding: utf-8

# # Correction of practice 7

# In[9]:


import csv
import pandas as pd


# In[6]:


all_sym = []
with open(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_7\list_symbols_euronext.csv", 'r') as file:
    csvfile = csv.reader(file)
    for row in csvfile:
#         for i in row:
#             all_sym.append(i)
        all_sym = all_sym + row
#         print(row)
        break
print(len(all_sym))


# In[7]:


with open(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_7\list_symbols_US.csv", 'r') as file:
    csvfile = csv.reader(file)
    for row in csvfile:
#         for i in row:
#             all_sym.append(i)
        all_sym = all_sym + row
#         print(row)
        break
print(len(all_sym))


# In[15]:


list_df = []
for i in all_sym[:10]:
    print(i)
    try:
        df = pd.read_csv("https://query1.finance.yahoo.com/v7/finance/download/"+ i +"?period1=0&period2=1661904000&interval=1d&events=history&includeAdjustedClose=true")
        df['SYM'] = i
        list_df.append(df)
    except:
        print('error')


# In[16]:


df_final = pd.concat(list_df, ignore_index = True)
print(df_final)


# In[17]:


df_final.to_csv(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_7\the_csv_version.csv")


# In[18]:


df_final.to_parquet(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_7\the_parquet_version.parquet")


# # Lecture 8: Graphs

# In[19]:


#import
import pandas as pd


# In[20]:


#load our data
#pip install : pyarrow and fastparquet
df_origin = pd.read_parquet(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_8\df_final_US_EUR.parquet")


# In[21]:


#print our data
print(df_origin)


# In[44]:


#Select only a part of the data and reset_index (drop = True)
df = df_origin[df_origin['Name'] == 'GOOGL'].copy()
df.reset_index(drop = True, inplace = True)
print(df)


# In[45]:


#install packages:
#pip install matplotlib
#pip install seaborn


# In[27]:


#Make you first plot without x axis (default is index)
#import matplotlib.pyplot as plt
#plt.show()
df.plot(y = 'Open')


# In[28]:


#you can also use another column as x axis
df.plot(x = 'Date', y = 'Close')


# In[29]:


#You can select a smaller amount of data
import datetime
df_small = df[df['Date'] > datetime.datetime(2022,8,1)]


# In[30]:


#use the bar kind
#use the kind attribute
df_small.plot(kind = 'bar', x = 'Date', y = 'Volume')


# In[31]:


#use the horizontal bar kind
df_small.plot(kind = 'barh', x = 'Date', y = 'Volume')


# In[33]:


# use the histogram
df_small.plot(kind = 'hist', y = ['Open', 'Close'])


# In[34]:


# use the boxplot (kind  = 'box')
df_small.plot(kind = 'box', y = ['Open', 'Close'])


# In[35]:


# use the area
df_small.plot(kind = 'area', y = ['Open', 'Close'])


# In[38]:


#the scatter version
df_small.plot(kind = 'scatter', x = 'Close', y = 'Open')


# In[ ]:


#YOUR TURN (15 minutes)(with my parquet file install pyarrow and fastparquet package first)
#) or any csv data (price))
#%matplotlib inline
#Draw the evolution of the volume with the date in line
#Draw the scatter plot of the volume in function of the Open price
#import matplotlib.pyplot as plt
#plt.show()


# In[41]:


df.plot(x = 'Date', y = 'Volume')
df.plot(kind = 'scatter', x = 'Open', y = 'Volume')


# In[48]:


# Add column:
#percentage change for 'Open'
#('open'[dayi] - 'open'[dayi-1]) / 'open'[dayi] *100
col = ['Open', 'High', 'Low', 'Close', 'Volume']
for c in col:
    perc = []
    for index, line in df.iterrows():
        if index == 0:
            perc.append(0)
        else:
            perc.append( (line[c] - df.loc[index-1, c])/line[c] *100)

    df['perc_'+c] = perc
print(df)


# In[ ]:


#YOUR TURN (10 minutes)
#Add the percentage change for all prices column and the volume


# In[54]:


#print the link between datas (ex: perc or volume)
df.plot(kind = 'scatter', x = 'Date', y = 'perc_Open')
df.plot(kind = 'scatter', x = 'perc_Close', y = 'perc_Open')
df.plot(kind = 'scatter', x = 'Close', y = 'Open')


# In[63]:


#Use matplotlib also
#https://matplotlib.org one of the most famous package to plot
# the command : "%matplotlib inline" may be necessary
import matplotlib.pyplot as plt


# In[64]:


#create a figure with subplots and scatter
fig, ax = plt.subplots(3)
ax[0].plot(df['Date'], df['perc_Open'])
ax[1].plot(df['Date'], df['perc_High'])
ax[2].plot(df['Date'], df['perc_Low'])
plt.show()


# In[72]:


#Create a figure with plot
fig, ax = plt.subplots(3)
ax[0].scatter(df['Date'], df['perc_Open'], marker = 'x')
ax[1].plot(df['Date'], df['perc_High'], linewidth = 1)
ax[2].plot(df['Date'], df['perc_Low'], color = 'red')
plt.show()


# In[76]:


#Is the volume and the perc of change are linked? And the perc and the voume of the day before?
fig, ax = plt.subplots()
ax.scatter(df['perc_Open'], df['Volume'], marker = '+')
plt.show()


# In[77]:


#Seaborn to draw plots
#https://seaborn.pydata.org/
import seaborn as sns


# In[79]:


#draw your first plot, use data = df and the relplot() function, use linewidth to change the white order
sns.relplot(data = df, x = 'Date', y = 'perc_Volume', linewidth = 0)


# In[84]:


#Change min et max (ylim)
sns.relplot(data = df, x = 'perc_Open', y = 'perc_Volume', hue = 'perc_Close')
plt.ylim(-50,50)
plt.show()


# In[ ]:


#another style with the set_style function
#list of style: https://seaborn.pydata.org/tutorial/aesthetics.html#seaborn-figure-styles


# In[ ]:




