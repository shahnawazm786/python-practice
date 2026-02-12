import requests
data=requests.get("https://webscraper.io/test-sites")
if data.status_code==200:
    print('connected with website')
    print(data.content)