#!usr/bin/env python3

import sys
import urllib.request as req
import urllib.parse as parse

print(len(sys.argv))
if len(sys.argv) <= 1:
	print("usage: download-forecast-argv <region number>")

api_addr = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# params = parse.urlencode(value)
url = api_addr
print("url = ", url)

data = req.urlopen(url).read()
text = data.decode("utf-8")
print(text)


