import urllib.request
import json
import random

def get_char():

  url ='http://hp-api.herokuapp.com/api/characters'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  
  char = random.randint(1,40)

  
  
  if result[char]["ancestry"] != '':
       return(f"{result[char]['name']} is an excellent actor, who has  {result[char]['hairColour']} hair colour and is played by {result[char]['actor']} in Harry Potter")
  else:
      return(f"{result[char]['name']}'s' cat has been found")