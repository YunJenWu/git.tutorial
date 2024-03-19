import requests
from bs4 import BeautifulSoup

url="https://www.ptt.cc/bbs/Soft_Job/index.html"
response=requests.get(url)

if response.status_code!=200:
    print("failed")
    exit()

html=response.text
soup=BeautifulSoup(html,"html.parser")
titles=soup.select("div.title a")

titles_5=titles[0:4]
urls=[i["href"] for i in titles_5]
prefix="https://www.ptt.cc/"

for url in urls:
    response=requests.get(prefix+url)
    if response.status_code!=200:
        print("failed")
        exit()
    html=response.text
    soup=BeautifulSoup(html,"html.parser")
    chaos=soup.select_one("#main-content").text
    l=chaos.find("時間")+26
    r=chaos.find("--")
    print(chaos[l:r])
    break
