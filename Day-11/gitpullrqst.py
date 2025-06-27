
# * get the pull request information on repo using python
# steps
# 1) install request module
# 2) using this module make api-calls (for git use the git api doc to get the url)
# 3) once recieve the info convert the jason to dictionary
# 4) print the information



import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

# print(response.json())

complete_detail = response.json()

#print(complete_detail[0]["id"])
for i in range(len(complete_detail)):
 
 
 
 print(complete_detail[i]["user"]["login"])

#print(complete_detail[0]["user"]["login"])
#print(response.status_code)





