#!/usr/bin/env python
# coding: utf-8

# # LECTURE 6

# # Correction of the practice

# In[ ]:


import requests


# In[ ]:


headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
resp = requests.get('https://query1.finance.yahoo.com/v7/finance/download/MSFT?period1=1633828168&period2=1665364168&interval=1d&events=history&includeAdjustedClose=true', 
                    headers = headers)

print(resp.content)


# In[ ]:


import pandas as pd
import io
df = pd.read_csv(io.StringIO(resp.content.decode('utf-8')))
print(df)


# In[ ]:


df = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/MSFT?period1=1633828168&period2=1665364168&interval=1d&events=history&includeAdjustedClose=true')
print(df)


# In[ ]:


l = ['TSLA', 'MSFT', 'AAPL']
for i in l:
    headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
    resp = requests.get('https://query1.finance.yahoo.com/v7/finance/download/'+i+'?period1=1633828168&period2=1665364168&interval=1d&events=history&includeAdjustedClose=true', 
                        headers = headers)

    import pandas as pd
    import io
    df = pd.read_csv(io.StringIO(resp.content.decode('utf-8')))
    print(df)


# # LECTURE

# # Reminder => make a request

# In[ ]:


#YOUR TURN: Make a request to any website (except websites with login requiered) and print the html code
#10 minutes => just print the content of the response => 17:30


# In[ ]:


#install and import request library
import requests


# In[ ]:


#make a request
resp = requests.get('https://www.google.com')
print(resp.content)


# In[ ]:


#Use header with user-agent information for better result
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
resp = requests.get('https://www.google.com', headers = headers)
print(resp.content)


# # BeautifulSoup and Html

# ## Reminder

# In[ ]:


#Get the html file of a website
with open(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_6\html_example.html", 'r') as file:
    content = file.read()
    
print(content)


# In[ ]:


#Install an import beautiful soup
# for installation => pip install bs4
from bs4 import BeautifulSoup


# In[ ]:


#Make the soup !
# content is resp.content (where resp = requests.get(....))
soup = BeautifulSoup(content)
print(soup.prettify())


# In[ ]:


#YOUR TURN
#Make a soup of athe weather website (link on teams)
#10 minutes => 17:44
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
resp = requests.get('https://www.accuweather.com/en/kz/almaty/222191/weather-forecast/222191', headers = headers)
soup = BeautifulSoup(resp.content)
print(soup.prettify())


# # Using the soup

# ## Some useful functions

# In[ ]:


#Getting a html file in my files
with open(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_6\html_example.html", 'r') as file:
    content = file.read()
    
# print(content)
soup = BeautifulSoup(content)


# In[ ]:


# prettify
print(soup.prettify())


# In[ ]:


# Going trough tags
print(soup.div.div)


# In[ ]:


#YOUR TURN print the following tag ...
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
resp = requests.get('https://www.accuweather.com/en/kz/almaty/222191/weather-forecast/222191', headers = headers)
soup = BeautifulSoup(resp.content, 'html.parser')
print(type(soup.body.div.div.div.div.div))


# In[ ]:


# iteration on children of a tag:
with open(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_6\html_example.html", 'r') as file:
    content = file.read()
    
# print(content)
soup = BeautifulSoup(content)

# for child in soup.aside.ul.children:
#     print(child)


# In[ ]:


#On all descendant
for child in soup.header.descendants:
    print(child)


# In[ ]:


#YOUR TURN : print all descendats  of a tag: div class = "template-root"
#5 minutes
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
resp = requests.get('https://www.accuweather.com/en/kz/almaty/222191/weather-forecast/222191', headers = headers)
soup = BeautifulSoup(resp.content, 'html.parser')
for desc in soup.body.div.descendants:
    print(desc)


# In[ ]:


# Get the content of a tag
print(soup.body.div.header.contents)


# In[ ]:


#Get the string of a tag (only if no more children)
print(soup.body.div.header.h1.string)


# In[ ]:


#Finding all
print(soup.div.header.div.find_all('a'))


# In[ ]:


# more about find_all
# filtering with id
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
resp = requests.get('https://www.accuweather.com/en/kz/almaty/222191/weather-forecast/222191', headers = headers)
soup = BeautifulSoup(resp.content, 'html.parser')

print(soup.find_all('div', id = 'bottom'))


# In[ ]:


#filtering with class
print(soup.find_all('div', class_ = 'page-subnav'))


# In[ ]:


#filtering with several attribute
attrs = {'class' : 'header-city-link'}
print(soup.find_all('div', attrs))


# In[ ]:


print(soup.find_all('a', attrs)[0]['href'])


# In[2]:


#YOUR TURN : Get the current temperature and today air quality in the weather website
#10 minutes
import requests
from bs4 import BeautifulSoup
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
resp = requests.get('https://www.accuweather.com/en/kz/almaty/222191/weather-forecast/222191', headers = headers)
soup = BeautifulSoup(resp.content, 'html.parser')


# In[10]:


attrs = ('')
print(soup.find_all('a', class_ = 'cur-con-weather-card')[0].find_all('div', class_ = 'temp'))
# print(soup.find_all('div', class_ = 'page-column-1')[0].find_all('div', class_ = 'temp'))


# # Test with KBTU website

# In[ ]:


#Your Turn:
#Get all image of KBTU website
#Then get image of academic staff only


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




