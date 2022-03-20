import requests

# post request

data = {

}

response = requests.post(url, data=data)

# intranet need to be authenticated

auth = (user,pwd)

response_auth = requests.get(url, auth=auth)
