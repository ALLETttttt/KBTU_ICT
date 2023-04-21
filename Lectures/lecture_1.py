import csv
#Open the file in python with the path of the file in your computer
file = open(r"C:\Users\user\Downloads\Apple_price_csv.csv", 'r')
#open the file with reader function
csv_file = csv.reader(file)

# for i in csv_file:
#     print(i)

#read the file as a dict
csv_file = csv.DictReader(file)


#Advanced reading
with open(r"C:\Users\user\Downloads\Apple_price_csv.csv", 'r') as file:
    spam = csv.reader(file, delimiter=',')
    # for i in spam:
    #     print(','.join(i))


with open(r"C:\Users\user\Downloads\Apple_price_csv.csv", 'a', newline='') as file:
    spam = csv.writer(file, delimiter=';')
    spam.writerow(['1', '2', '3'])


#YOUR TURN
#What is the percentage of student who knows python?
#Open the file
#do number of yes divide by number of answers
#Print the result
# file on teams in the channel Lecture_wednesday_11_13
#time : 10 min => 12:05

yes = 0
total = 0

with open(r"C:\Users\user\Downloads\Skills assessment_modified.csv", 'r') as file:
    spam = csv.reader(file)
    for i in spam:
        total += 1
        if(i[1] == 'Yes'):
            yes += 1

# print(yes/total * 100, '%')

# # Work with .json file


import json

jsonData = open(r"C:\Users\user\Downloads\Example_json_data.json").read()
#Print the data (dictionnary)
data = json.loads(jsonData)
# for i in data:
#     print(i)


from xml.etree import ElementTree as ET

tree = ET.parse(r"C:\Users\user\Downloads\Example_xml_data.xml")

print(tree.getroot())

for i in tree.getroot():
    print(i)

item = tree.getroot()[0]
for i in item:
    print(i)
    print(i.text)

tree.write(r"C:\Users\user\Downloads\Example_xml_data.xml")




# # Work with excel files

# ## Read excel files
import xlrd


# book = xlrd.open_workbook(r"C:\Users\user\Downloads\Price_tesla_and_microsoft.xlsx")

#List a tabs
# for i in book.sheets():
#     print(i.name)

#Choose the right tab
# sheet = book.sheet_by_name('Tesla_price')
#Or just to get the first tab
# sheet = book.sheet_by_index(0)
# print(sheet)  

# print(sheet.col_values(0))
# print(sheet.row_values(0))
# print(sheet.cell_value(rowx=3, colx=3))

import xlwt


book = xlwt.Workbook(r"C:\Users\user\Downloads\Price_tesla_and_microsoft.xlsx")

ws = book.add_sheet('A Test Sheet')
ws = book.add_sheet('A Test Sheet1')
ws = book.add_sheet('A Test Sheet2')

for i in range(5, 10):
    ws.write(i, 0, 1)
    ws.write(i, 1, 2)

ws.write(5, 2, xlwt.Formula("A6+B6"))
 
#import package
import pandas as pd


# In[48]:


#Get the value of a column
values = ['Apple', 'Tesla', 'Microsoft']


# In[49]:


#Create a serie
my_serie = pd.Series(values)
# print(my_serie)
# print(my_serie[1])

#But you can specify them
my_serie = pd.Series(values, index = ['x', 'y', 'z'])
print(my_serie)
print(my_serie['y'])


#Label is automatic from a dictionary
dictionary = {"day1" : 1000, "day2": 1100, "day3": 0}
my_serie = pd.Series(dictionary)
print(my_serie)

#You can choose the one you want to keep
my_serie = pd.Series(dictionary, index = ["day1", "day2"])
print(my_serie)


#From a dictionary
#Create the dataset you want to analyze
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'numbers': [3, 7, 2]
}


# In[61]:


#Create a Dataframe from the dictionary 
my_df = pd.DataFrame(mydataset)
print(my_df)


# In[62]:


#You can locate a row (return a Serie)
print(my_df.loc[1])

#Or several row (return a dataframe)
print(my_df.loc[[1,2]])

#Create dataframe with indexes
df = pd.DataFrame({"Company" : ['Apple', 'Tesla', 'Microsoft'], "Creation" : [1976, 2003, 1975]}, 
                  index = ['favorite', 'so-so', 'Maybe'])
print(df)


#Acces to a value with the index
print(df.loc['favorite'])



