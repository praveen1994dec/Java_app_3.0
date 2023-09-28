import requests

url = "https://myurl.jfrog.io/artifactory/reponame-generic-local"
auth = ("myusername", "mypassword")
file_name = "test.txt"

response = requests.put(url + "/data/" + file_name, auth=auth, data=open(file_name, "rb"))
print(response.status_code)
