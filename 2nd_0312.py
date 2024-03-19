'''
import requests
from bs4 import BeautifulSoup

url="https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html"
response=requests.get(url)
print(response.text)

import requests
from bs4 import BeautifulSoup
address="https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html"
datas={
    "from":"/bbs/Gossiping/index.html",
    "yes":"yes"
}

html=requests.post(address,data=datas).text

soup=BeautifulSoup(html,"html.parser")
titles=soup.select("div.title a")
for title in titles:
    print(title.text)
'''

import praw
import requests
from os.path import splitext

reddit = praw.Reddit(
    client_id="AdFF30yohtwUawwhfjqvOA",
    client_secret="DFt-iT3B-WdEqmB4Wx0WlSitCSqi2w",
    user_agent="Python:com.gdsc66.wyj910214app:v0.0.1:(by Either-Difficulty-77)"
)

post = [*reddit.subreddit("wallpapers").hot(limit=10)]
for i in post:
    img = requests.get(i.url).content
    if splitext(i.url)[1]!="":
        with open(i.title+splitext(i.url)[1],"ab") as f:
            f.write(img)
