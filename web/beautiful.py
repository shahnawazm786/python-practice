from bs4 import BeautifulSoup
import requests
#res=requests.get("https://webscraper.io/test-sites")
res=requests.get('http://books.toscrape.com/index.html')
data=''
if res.status_code == 200:
    data=res.text
    #print(data)
soup=BeautifulSoup(res.text,) # html parsing
#print(soup)
print(soup.find('title'))
books=soup.find_all('article',class_='product_pod')
#print(books[0])
print(len(books))