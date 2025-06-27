
# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

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

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
