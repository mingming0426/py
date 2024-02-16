import requests
from bs4 import BeautifulSoup
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"}
content=requests.get("https://v2ex.com",headers=headers)
print(content.text)
soup=BeautifulSoup(content,"html.parser")
print(soup)