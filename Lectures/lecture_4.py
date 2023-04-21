#!/usr/bin/env python
# coding: utf-8

# # API

# In[ ]:


#install the requests package: pip install requests


# In[ ]:


#Import the package requests
import requests
print(requests.__version__)


# In[ ]:


#Calling the API of randomuser.me website (address is "https://randomuser.me/api/")
response = requests.get("https://randomuser.me/api/")
print(response)


# In[ ]:


#Check the text in the reponse
print(response.text)


# In[ ]:


#The dog API connection (https://api.thedogapi.com/)
response = requests.get("https://api.thedogapi.com/")
print(response.text)


# In[ ]:


#Connecting to an Endpoint
response = requests.get("https://api.thedogapi.com/v1/breeds")
print(response.text)


# In[ ]:


# YOUR TURN
# Connect to TheCatApi through the url : https://api.thecatapi.com/ 
# Check in the documentation how to get a random picture of a cat
# Make the calling and print the text of the answer
#10 minutes

resp = requests.get("https://api.thecatapi.com/v1/images/search")
print(resp.text)


# In[ ]:


#Some information about a request
#response.request
#.url
#.path_url
#.method
#.headers

resp = requests.get("https://api.thecatapi.com/v1/images/search")
print(resp.request)
print(resp.request.url)
print(resp.request.path_url)
print(resp.request.method)
print(resp.request.headers)


# In[ ]:


#Some information about a response
#.text
#.status_code
#.reason
#.headers
resp = requests.get("https://api.thecatapi.com/v1/images/search")
print(resp.url)
print(resp.status_code)
print(resp.reason)
print(resp.headers)


# In[ ]:


#Let's get other response than 200

resp = requests.get("https://api.thecatapi.com/images/searc")
print(resp)


# In[ ]:


#check headers of the response and the request

resp = requests.get("https://api.thecatapi.com/v1/images/search")


# In[ ]:


#Print headers of server and client
print(resp.request.headers)
print(resp.headers)


# In[ ]:


#Create your own headers
#make a request with your own headers
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'}
url = 'https://api.thecatapi.com/v1/images/search'
resp = requests.get(url, headers = headers)
print(resp.request.headers)


# In[2]:


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'}
url = 'https://cdn2.thecatapi.com/images/d8k.jpg'
resp = requests.get(url, headers = headers)
print(resp.headers)


# In[11]:


#The differents methods of the response
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'}
url = 'https://api.thecatapi.com/v1/images/search'
resp = requests.get(url, headers = headers)
resp_json = resp.json()
print(resp_json[0]['url'])


# In[14]:


#The different content type
url = 'https://api.thecatapi.com/v1/images/search'
resp = requests.delete(url)
print(resp)


# In[16]:


#Request an image
url = 'https://cdn2.thecatapi.com/images/250.jpg'
resp = requests.get(url)
print(resp.content)


# In[17]:


#Save the image
with open(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_4\cute_cat.jpg", 'wb') as file:
    file.write(resp.content)
    


# In[28]:


#The use of a query parameter to specify your request
url = "https://randomuser.me/api?gender=male"
resp = requests.get(url)
print(resp.text)


# In[29]:


# YOUR TURN
# Use the api for rendomuser.me to generat only male from nat : 'FR'
# 10 minutes
url = "https://randomuser.me/api?gender=male&nat=FR"
resp = requests.get(url)
print(resp.text)


# In[32]:


#use a dictionary to for query parameters
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'}
dictio = {
    'gender' : 'male', 
    'nat' : 'FR'
}
url = "https://randomuser.me/api"
resp = requests.get(url, params = dictio, headers = headers)
print(resp.text)


# In[38]:


#Make a request to nasa website for image with the DEMO_KEY
#endpoint is : https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos
# use also a query parameter : "earth_date": "2020-07-01"
query_param = {
    "api_key" : "DEMO_KEY",
    "earth_date": "2020-07-01"
}

resp = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos', params = query_param)
print(resp.text)


# In[45]:


#get only the url of the photos
for i in resp.json()['photos']:
    print(i['img_src'])


# In[49]:


# YOUR TURN
# with the previous code (to save jpg into file), loop on all the photos and save them in your computer
# 15 minutes

query_param = {
    "api_key" : "DEMO_KEY",
    "earth_date": "2020-07-01"
}

resp = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos', params = query_param)
for index, data in enumerate(resp.json()['photos']):
    resp2 = requests.get(data['img_src'])
    with open(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_4\photo_curio_"+ str(index) +".jpg", 'wb') as file:
        file.write(resp2.content)


# In[58]:


#Make a API request on polygon.io

url = "https://api.polygon.io/v2/aggs/ticker/TSLA/range/1/minute/2021-07-22/2021-09-22?sort=asc&limit=5000&apiKey=lFm05uiT4LHXMiZbEQzcTCmnwZpWAJXU"
resp = requests.get(url)
print(resp.json())


# In[ ]:




