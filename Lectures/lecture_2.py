#!/usr/bin/env python
# coding: utf-8

# # Correction of the practice

# ## Check Python

# In[1]:


#Check that your python environnment is working:
print('It\'s working')


# ## Open csv file with Python

# In[2]:


#installation => anaconda prompt => pip install csv
#Import the csv package
import csv


# In[6]:


#import the csv package and print every row in the console
# print("D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv")
# print(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv")
#'r' : reading
#'w' writing
#'a' append (writing)

file = open(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv", 'r')

csvfile = csv.reader(file)
for row in csvfile:
    print(row)
    
file.close()

#remeber to close files


# In[16]:


#I recommend : with open
#you can only iterate one time on csv.reader object

with open(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv", 'r') as file:
    csvfile = csv.reader(file)
    csvfile.__next__()
    for row in csvfile:
        print(row)


# In[19]:


#opened with a dictionnary
with open(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv", 'r') as file:
    csvfile = csv.DictReader(file)
    for row in csvfile:
        print(row)


# ## Get CSV data into python console

# In[20]:


#import csv package
import csv


# In[30]:


#Create lists to store data (here a list of list to go faster)
list1, list2, list3 = [], [], []


#Information:
# #don't do that :
# list1 = list2 = list3 = []
# list1.append(1)
# print(list1, list2)
# info = [1,2,3]
# info2 = info # wrong
# info2 = [i for i in info] #right
# info2.append(7)
# print(info, info2)

# #Be carefull of names
# #open = [] #do not do that
# open_list = []


# In[22]:


#Open csv file and store data in lists
#be careful with name of lists (ex : data, open)
with open(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv", 'r') as file:
    csvfile = csv.reader(file)
    csvfile.__next__()
    for row in csvfile:
        list1.append(row[0])
        list2.append(row[1])
        list3.append(row[2])


# In[25]:


#Check your lists
print(list1[:10])
print(list2[:10])


# In[40]:


#faster
lists = [[] for i in range(7)]
print(lists)

with open(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv", 'r') as file:
    csvfile = csv.reader(file)
    csvfile.__next__()
    for row in csvfile: 
        for index, l in enumerate(lists):
            l.append(row[index])
#         for index in range(0, len(lists)):
#             lists[index].append(row[index])  
#info about enumerate
a = [564, 166, 12]
for index, item in enumerate(a): 
    print(index)
    print(item)


# In[42]:


#Check your lists
print(lists[0][:10])
print(lists[1][:10])


# # Modify your data

# In[43]:


#First: Text into number (float)
for i in range(1,len(lists)):
    lists[i] = [float(j) for j in lists[i]]
    
print(lists[1][0])


# In[46]:


#Second: date
#first check the format
#1962-01-02
import datetime
print(type(datetime.datetime.strptime("1962-01-02" , "%Y-%m-%d")))


# In[52]:


#let's do it for all the list
lists[0] = [datetime.datetime.strptime(i , "%Y-%m-%d") for i in lists[0]]
print(lists[0])
# print(lists[0][3])
# print(lists[0][3].weekday())


# In[ ]:


#For this week :
#Prepare your code : clean
#result : 7 lists with datetime and float


# # DataFrame

# ## What are the advantages

# ### Using lists to manage data

# In[83]:


#You have a list of informations on students:
#Create the list
name = ['Bob', 'advgd', 'buo']
surname = ['jhg', 'hu', 'jio']
age = [18, 26, 17]


# In[55]:


#Diplay your data
print(name)
print(surname)
print(age)
#print last one

print(name[-1])
print(surname[-1])
print(age[-1])


# In[69]:


# Operate on this lists : delete one value,   
#advgd, hu
for i in range(0, len(name)):
    if name[i] == 'advgd' and surname[i] == 'hu':
        index_delete = i

del name[index_delete]
del surname[index_delete]
del age[index_delete]
print(name)


# In[73]:


# Operate on this lists : extract information on one student
for i in range(0, len(name)):
    if name[i] == 'advgd' and surname[i] == 'hu':
        print(name[i])


# In[77]:


# Operate on this lists : extract information on several students
for i in range(0, len(name)):
    if name[i] == 'advgd' or name[i] == 'Bob':
        print(name[i])


# In[86]:


# Sort datas
#function .sort
print(age)
age.sort()
print(name)
print(surname)
print(age)


# # Pandas

# ## The pandas package

# In[ ]:


#Install pandas
# pip install pandas


# In[87]:


#Import pandas package
#recommended as pd
import pandas as pd


# ## Let's create our first DataFrame

# In[89]:


#Create your first DataFrame
#Do not forget Uppercas for "D" and "F"
df = pd.DataFrame()
print(df)


# ## Populate it

# In[90]:


#Create a dictionnary with data from student
name = ['Bob', 'advgd', 'buo']
surname = ['jhg', 'hu', 'jio']
age = [18, 26, 17]


# In[93]:


#Create a dataframe from this dictionnary
# dictio = { 'key' : value}
dictio = {'names' : name, 'surnames' : surname, 'ages' : age}
print(dictio)
df = pd.DataFrame(dictio)


# In[94]:


# Display all your dataframe
print(df)


# In[97]:


# Display some lines of your dataframe
print(df['names'][1])


# In[100]:


#Your turn:
#Create a empty dataframe
#Populate it with 3 lines of 6 columns (invent your own data)
#12:05
import pandas
df = pd.DataFrame({'a' : [1, 2, 3],'bc' : [1, 2, 3],'c' : [1, 2, 3],'d' : [1, 2, 3],'e' : [1, 2, 3],'f' : [1, 2, 3], })
print(df)


# ## Populate with csv file

# In[125]:


# Select some data of the dataframe
df = pd.read_csv(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv")


# In[116]:


#display it
#'\' df continue on next lines
#'...' => undisplayed data
print(df)


# In[126]:


# Remove 2 last columns to be more clear
del df['Volume']
del df['Adj Close']
print(df)


# In[127]:


#Modify data for later use (date and float)
# print(type(df['Open'][0]))
# print(type(df['Date'][0]))
# df['Date_in_datetime'] = [datetime.datetime.strptime(i , "%Y-%m-%d") for i in df['Date']]
# print(df)
# print(type(df['Date_in_datetime'][0]))

df['Date'] = [datetime.datetime.strptime(i , "%Y-%m-%d") for i in df['Date']]
print(df)


# In[124]:


#YOUR TURN
#Use you data from last pratice to make a dataframe from it
#Choose your own names for the columns (check the documentation of read_csv method)
#Column names should be : 
#['Date', 'Open price', 'High price', 'Low price', 'Close price', 'Adjusted close price', 'Volume exchanged']
#Try to automaticaly change Date into datetime object with the read_csv emthod 
#(check the documentation of read_csv method)
#12:25
df = pd.read_csv( r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv",
                header=0,
                 names = ['Date', 'Open price', 'High price', 'Low price', 'Close price', 'Adjusted close price', 'Volume exchanged'],
                 parse_dates = [0]
                )
print(type(df['Date'][0]))


# ## Select data

# In[131]:


# Display of the first data of the dataframe
print(df['Date'][0])

# loc function => [index, name column]
print(df.loc[5245, 'Low'])


# In[133]:


#select only a line with index (iloc)

# iloc function => [index, index column]
print(df.iloc[5245, 3])


# In[136]:


#Select several lines with indexes
print(df.iloc[range(2165, 2170), range(2,4)])


# In[140]:


#Creation of a selection DataFrame
# a = 100
# print(a>1000)
print(df['High'] > 100)
select_df = df['High'] > 100


# In[142]:


#select a part.
print(df[select_df])
print(df[df['Open'] < 50])


# In[147]:


#Select a part of a Dataframe  ( () &() 
#& => AND
#| => OR
print(df[  (df['Open'] < 50) | (df['High'] > 50)  ])


# In[149]:


begin = datetime.datetime(year = 2021, month = 5, day = 25)
print(begin)
print(df[df['Date'] > begin])


# In[152]:


#Sort the dataframe (.sort_values)
print(df.sort_values('Low'))


# In[161]:


#YOUR TURN
#From your dataframe: extract data with the following conditions:
# - Only in 2021
# - Only date, Volume and High
# - Only when high price is superior than 2019 average high price (use .mean()) => df[].mean()
#12:50

df = pd.read_csv( r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv",
                parse_dates = [0]
                )

date_begin_mean = datetime.datetime(year = 2019, month = 1, day = 1)
date_end_mean = datetime.datetime(year = 2020, month = 1, day = 1)

mean = df[ (df['Date'] > date_begin_mean) & (df['Date'] < date_end_mean) ]['High'].mean()
print(mean)

date_begin = datetime.datetime(year = 2021, month = 1, day = 1)
date_end = datetime.datetime(year = 2022, month = 1, day = 1)

df = df[ (df['Date'] > date_begin) & (df['Date'] < date_end) & (df['High'] > mean)]
df = df.loc[:, ['Date', 'Volume', 'High']]

print(df)


#in 1 instruction
print(df.loc[:, ['Date', 'Volume', 'High']]       [ (df['Date'] > begin) &       (df['Date'] < date_end) &        (df['High']  > (df[ (df['Date'] > date_begin_mean) & (df['Date'] < date_end_mean) ]['High'].mean()))])


# In[ ]:


#Information:
# 80 students
# 95 crosses on attendance
# attendance => 12:40

