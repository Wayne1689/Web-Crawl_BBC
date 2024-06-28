import requests
from bs4 import BeautifulSoup

# 定義目標 URL
url = 'https://www.bbc.com/news'

# 發送 GET 請求
web = requests.get(url)
web.encoding = 'utf-8'
soup = BeautifulSoup(web.text,"html.parser")
headlines = soup.find_all('h2', attrs={'data-testid': 'card-headline'}) #用來尋找 h2 段落， 跟 屬性為'data-testid'，名字為'card-headline'

for headline in headlines:
        title = headline.get_text().strip()  # 獲取標題文字並去除多餘的空白
        print(f"Title: {title}\n")
