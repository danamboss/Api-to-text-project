#Importing the request required modules
import os, json
from twilio.rest import Client
from space import people_space
from weather import get_weather
from heroku import get_char
from flask import Flask, render_template

#functions
app = Flask('app')

@app.route('/')
def hello_world():
  return render_template("index.html")

@app.route('/sms')
def send_sms():
  account_sid = os.environ['accsiddan']
  auth_token = os.environ['authdan']
  
  
  client = Client(account_sid, auth_token)


  #message to be sent by Twillo
  msg = f' Information Requested: 1: {people_space()}.  2:  {get_char()}. 3: {get_weather("Ottawa")} is the weather in Ottawa, Canada.   '
  message = client.messages \
                  .create(
                       body=msg,
                       from_='+19034884362',
                       to='+14379905621'
                   )

  #json file
  filename = "data.json"
  with open(filename, "a") as f:
    json.dump(msg, f, indent = 4)
    
  print(message.sid)
  return render_template("final.html")

app.run(host='0.0.0.0', port=8080)