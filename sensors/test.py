import requests
url = "http://api.open-notify.org/astros.json"
r = requests.get(url)
data = r.json()
print(len(data['people']))
