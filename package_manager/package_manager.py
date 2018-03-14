# http://docs.python-requests.org/en/master/
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
import requests
from bs4 import BeautifulSoup

url = "https://codingeverybody.github.io/scraping_sample/1.html"

# html 내용 받기
r = requests.get(url)
# print(r.text)

# html 내용(text)
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup)
print(soup.title) # <title>sample1</title>
print("Title : " + soup.title.string) # title 태그의 문자열 내용만 출력 # Title : sample1

articles = soup.findAll("div", {"class" : "em"}) # 배열(list)로 얻음.
print(articles) # [<div class="em">important information 1</div>]
print("Article : " + articles[0].text) # Article : important information 1
