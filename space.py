import urllib.request
import json

def people_space():

  url ='http://api.open-notify.org/astros.json'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  
  return(f"{result['people'][0]['name']} flying craft {result['people'][0]['craft']} is in space right now")
