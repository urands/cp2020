import requests
import json

url = 'https://br.so-ups.ru/webapi/api/CommonInfo/GenConsum?priceZone[]=1&oesTerritory[]=550000&startDate=2009.01.01&endDate=2020.11.27'

r = requests.get(url, verify=False, timeout=300)
f = open('gen_and_use3.json', 'w')
json.dump(r.json(), f)
f.close()

#print(data)
