import pandas as pd
from datetime import datetime
df = None
for i in range(1,109):
    f = f'./temp/{i}.csv'
    rdf = pd.read_csv(f, sep=';', encoding = 'cp1251', parse_dates=[0],
         date_parser=lambda d: datetime.strptime(d,'%d-%m-%Y'))
    if df is None:
        df = rdf
    else:
        df = pd.concat([df,rdf], sort=False)
        df.reset_index()
        df = df.drop_duplicates()
    print('.', end='')
df.columns = ['M_DATE','TEMP']
df.to_csv('temperature.csv', index=False)