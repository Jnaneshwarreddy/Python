# sombody commnet on github issues that we have immediately github should send the perticular issue to Python Application which is in the ec2 instance via webhook (which is complete JSON payload)
# and Python Application should talk to JIRA through jira API.
# steps
# 1. what exactly the Api
# 2. convert python script to api ( beacause github needs to login to ec2 instance and reun the program as we run normally so if its api  hithub directly invoke  to the ec2 without login)
# 3. Deploy python application to server.
# 4. how to setup github webhook.
# 5.conditional handling 


# start writing APi using (flask framework)
# what is user interface( its platform whrere user will interact with the application to perform certain task ex: bookmy show to book a ticket) & application interface (when it comes to automation user interface is not that easy when application point of view the programming application is needed )
# the entire api's works on http protocol
# there are 4 types of http requests 1)post 2)get 3)put 4) delete

import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask # here i have imported flask module from flask package because flask package have some other modules which are not required why means it will take lot of time to excute the program if we use flask package


app = Flask(__name__) # createing flask app instantiation

@app.route('/createJIRA', methods=['POST'])     #decorator performs the action before execution of any function.
def createJIRA():
    
   url = "https://jnanibalu.atlassian.net/rest/api/3/issue"

   API_TOKEN 

   auth = HTTPBasicAuth("gmail", API_TOKEN)

   headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
  }

   payload = json.dumps( {
  "fields": {
  "issuetype": {
      "id": "10010"
    },
    "project": {
      "key": "JNAN"
    },
   "summary": "MY FIRST JIRA TICKET",
  },
  "update": {}
 } )

   response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
   )
   return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))


app.run('0.0.0.0', port=5000)


