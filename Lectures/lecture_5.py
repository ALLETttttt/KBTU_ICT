#!/usr/bin/env python
# coding: utf-8

# # Web scrapping

# ## Scrapping directly a document

# In[2]:


#import request library
import requests
print(requests.__version__)


# In[8]:


# Create a request
url = "https://console.python.org/python-dot-org-live-consoles-status"
resp = requests.get(url)
print(resp.content)


# In[ ]:


#YOUR TURN
# reproduce a request
#any website => open inspect tool => network tool => choose a request (html, josn, png, ...) => reproduce it with python
#10 minutes 11:30


# In[10]:


#Create a headers to get better result
#use the header from the "inspect" tool
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
resp = requests.get(url, headers = headers)
print(resp.content)


# In[ ]:


#YOUR TURN
#identify you headers of your web browser and use them to access to a website
#5 minutes => 11:35


# In[14]:


#Let's try with yahoo finance website  
url = "https://query1.finance.yahoo.com/v7/finance/download/MSFT?period1=1633376171&period2=1664912171&interval=1d&events=history&includeAdjustedClose=true"
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
resp = requests.get(url, headers = headers)
print(resp.content)


# In[ ]:


#YOUR TURN
#Try to get your own stock csv
#Yahoo finance => Stock page => Historical tab => Inspect => Download => find requests
#10 minutes = > 11:50


# In[21]:


#Finding the time period
# url = "https://query1.finance.yahoo.com/v7/finance/download/TSLA?period1=1633376171&period2=1664912171&interval=1d&events=history&includeAdjustedClose=true"
# resp = requests.get(url, headers= headers )
# print(resp.content)
# 1633376171 => 2021-10-04
print(1633376171 / 3600 /24/365)
# 0 => 1/1/1970


# In[28]:


#Automatize date choice
import datetime
origin = datetime.datetime(1970,1,1)
begin = datetime.datetime(2000,1,5)
delta = begin -origin
print(delta.total_seconds())


# In[38]:


#Choose your own dates
origin = datetime.datetime(1970,1,1)
begin = datetime.datetime(1971,1,5)
delta = begin -origin
delta = delta.total_seconds()

params = {'period1': str(int(delta)),'period2': '1664912171','interval':'1d','events':'history','includeAdjustedClose':'true'}
url = "https://query1.finance.yahoo.com/v7/finance/download/MSFT"
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
resp = requests.get(url, headers = headers, params = params)
print(resp.content)


# In[ ]:


#YOUR TURN
#get your csv file from practice 1 with a python resquest with another date
#10 minutes
#12:30


# # Scrapping a page

# In[ ]:


#Get the html file with a query on google news


# In[ ]:


# Extracting news data on company with BeautifulSoup
from bs4 import BeautifulSoup
import requests

#Use the url found with private browser
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0', 'Accept-Language' : 'en-GB,en;q=0.5'}
page = requests.get('https://news.google.com/search?q=tesla&hl=en-US&gl=US&ceid=US%3Aen',
                    headers = headers)
print(page.content)
bs = BeautifulSoup(page.content)


# In[ ]:


#Display info 
#Docs at : https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# print(bs.prettify())


# In[ ]:


#YOUR TURN
#Identify all url of the news about your stock
# 10 minutes


# # Browser-based scrapping : Selenium

# In[ ]:


#import the package
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# In[ ]:


#Download geckodriver from here : https://github.com/mozilla/geckodriver/releases
#Unzip it
#Add the path to geckodriver folder to the system path


# In[ ]:


#Create your browser
browser = webdriver.Firefox()  
#open the required page
browser.get("https://www.python.org")
browser.maximize_window()


# In[ ]:


#print some information
print(browser.title)


# In[ ]:


#Fin the research bar and write in it
search_bar = browser.find_element(By.NAME, "q")
search_bar.clear()
search_bar.send_keys("getting started with python")


# In[ ]:


#Run the research
search_bar.send_keys(Keys.RETURN)


# In[ ]:




