
import os
import urllib.request
import json

def get_weather(city):
  my_secret = os.environ['weather']
  url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={my_secret}'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
 
  temp = round(result["main"]["temp"] - 273.15,2)
    
  return temp