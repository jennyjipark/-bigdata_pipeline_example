import requests as re
import json

key = "d96110675909bd12630be745bd372320"

cities = ["London", "Chelsea"]
api = "http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={key}"

for city in cities:
    url = api.format(
        city_name=city, 
        limit='5',
        key=key)
    res = re.get(url)
    data = json.loads(res.text)

#     print(data)
    
    for d in data:
        print("NAME: ", d["name"])


