import requests
from bs4 import BeautifulSoup as bs
import datetime

url = "https://m.stock.naver.com/marketindex/home/major/exchange/bond"

re = requests.get(url)

soup = bs(re.text, "html.parser")
usd_rate_elem = soup.select_one("#content > div.MainList_article__sGjxm > ul > li:nth-child(1) > a > span.MainListItem_price__dP8R6")
usd_rate = usd_rate_elem.get_text()

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"{now} USD: {usd_rate}")