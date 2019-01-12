
# coding: utf-8

# In[ ]:


#Extract weather data from API website. 

# Step-1
#Discover the endpoints of the city to forecast. Endpoints= Lat/longs.
#Go to this link https://www.weather.gov/documentation/services-web-api and type the city name in the search button and 
#press go. You will see the forecast in the same page in left corner and then click Get Detailed info icon, it will open 
#a new window. Copy the lat longs from the web address of new window . 
#30.27,  -97.74° (Austin, Tx, USA)


# In[ ]:


#Step-2
#Pin these points to the link provided in the NWS API website. 
#Website reference - https://www.weather.gov/documentation/services-web-api

#https://api.weather.gov/points/30.27,-97.74


# In[ ]:


# Step-3
#Open the website in the step-2 and you will find GeoJSON: application/geo+json file. 
#This response tells the application where to find relative information–including office, zone and forecast data–for a 
#given point. The application can then use the linked data in the previous response to locate the raw forecast:

#https://api.weather.gov/gridpoints/EWX/155,90/forecast (Austin, TX, USA)- You can locate this link in the properties section.


# In[21]:


# Step-4 Import all the required libraries 
import urllib
import json
import requests 
import pandas as pd


# In[16]:


#Step-5 Pull the request from NWS API website.
# Connect the url and call the request 
request = requests.get('https://api.weather.gov/gridpoints/EWX/155,90/forecast')
print(request)
# If your response is <Response[200]> means you are sucessfully connected. 

request = urllib.request.urlopen('https://api.weather.gov/gridpoints/EWX/155,90/forecast')
data = request.read()
print(data)
# this data is in dictionaries and each values of the keys are in lists. 


# In[23]:


#Step-6
# Parse JSON- Covert the string data into JSON 
data_json =json.loads(data)
print(data_json)

# Extract the required data. Required data starts from "periods"
properties_data_json = data_json['properties']
periods_data_json = properties_data_json['periods']
print(periods_data_json)


# In[39]:


# Step-7 Loop to Data Frame

from pandas import DataFrame

Austin_weather = pd.DataFrame()
for item in periods_data_json:
    weather_data = pd.DataFrame({'Date':item['startTime'],'Temperature':item['temperature'],
                                 'Unit':item['temperatureUnit'],'WindDir':item['windDirection'], 'Windspeed':item['windSpeed']},
                                index =[0])
    weather_data['Location']= 'Austin'
    Austin_weather = pd.concat([Austin_weather, weather_data])
    
print(Austin_weather)



