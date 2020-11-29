import json
from pprint import pprint
from datetime import datetime, timedelta

#with open('second.json') as json_data:
with open('gen_and_use2.json') as json_data:
    d = json.load(json_data)
    json_data.close()

print(len(d))


for ii in range(2):
    print(ii, d[ii]['m_Item1'],'LEN:', len(d[ii]['m_Item2']))
    f1 = open(f'gen_and_use{ii}.csv', 'w')
    f1.write("INTERVAL,M_DATE_DAY,M_DATE,PRICE_ZONE_ID,POWER_SYS_ID,E_USE_FACT,E_USE_PLAN,GEN_FACT,GEN_PLAN\n")

    for i in d[ii]['m_Item2']:
        df = [
            str(int(i['INTERVAL'])),
            datetime.strptime(i['M_DATE'], '%Y-%m-%dT%H:%M:%S%z').strftime('%Y-%m-%d'),
            (datetime.strptime(i['M_DATE'], '%Y-%m-%dT%H:%M:%S%z') +
             timedelta(hours=i["INTERVAL"])).strftime('%Y-%m-%d %H:%M:%S'),
            str(int(i['PRICE_ZONE_ID'])),
            str(int(i['POWER_SYS_ID'])),
            str(int(i['E_USE_FACT'])) if i['E_USE_FACT'] is not None else str(0),
            str(int(i['E_USE_PLAN'])),
            str(int(i['GEN_FACT'])) if i['GEN_FACT'] is not None else str(0),
            str(int(i['GEN_PLAN'])),
        ]
        f1.write(','.join([ v for v in df ]))
        f1.write("\n")
    f1.close()



