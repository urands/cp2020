import requests
import time

i = 0

for y in range(2012,2021):
    for m in range(1,13):
        i+=1
        print(f"Download 01.{m}.{y}")
        url = f'https://www.so-ups.ru/index.php?id=oes_south_temperature&tx_ms1cdu_pi1[dt]=01.{m}.{y}&tx_ms1cdu_pi1[format]=csv'
        r = requests.get(url)
        open(f'./temp/{i}.csv', 'wb').write(r.content)
        time.sleep(1)
