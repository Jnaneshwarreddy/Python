# set up jira
# understand jira api-calls
# write the python script 
# excution of script
# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://jnanibalu.atlassian.net/rest/api/3/project"

# API_TOKEN 
auth = HTTPBasicAuth("your gmail", API_TOKEN )

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
 
output = json.loads(response.text)

name = output[0]["name"]
print(name)
