import requests as re
import json
from config import get_secret

cities = ["London", "Chelsea"]
api = "http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={key}"
KEY = get_secret("OPEN_WEATHER_KEY") # 서비스키

for city in cities:
    url = api.format(
        city_name=city, 
        limit='5',
        key=KEY)
    res = re.get(url)
    data = json.loads(res.text)
    
    for d in data:
        print("NAME: ", d["name"])


