import pandas as pd


def load():
    # LOAD POWER
    power = pd.read_csv('./datasets/gen_and_use1.csv', parse_dates=['M_DATE', 'M_DATE_DAY'])
    power = power.drop(power[power.E_USE_FACT == 0].index).set_index('M_DATE')
    power['DAY'] = power.index.year * 1000 + power.index.dayofyear
    power['M_DATE'] = power.index

    # LOAD TEMPERATURE
    temp = pd.read_csv('./datasets/temperature.csv', parse_dates=[0])
    # temp = temp.drop_duplicates()
    temp['DAY'] = temp.M_DATE.dt.year * 1000 + temp.M_DATE.dt.dayofyear
    temp = temp[temp.M_DATE <= power.M_DATE.max()]
    # temp = temp.set_index('M_DATE')

    power = pd.merge(power, temp[['DAY', 'TEMP']], how='left', on='DAY').set_index('M_DATE')

    power['year'] = power.index.year
    power['month'] = power.index.month

    return power

def load_invest():
    invest = pd.DataFrame({ \
        'date': ['2009-06-01', '2010-06-01', '2011-06-01', '2012-06-01', '2013-06-01', '2014-06-01', '2015-06-01',
                 '2016-06-01'],
        'money': [2332.1, 3057.9, 12035.7, 5924.9, 44427.5, 51795.5, 4574.9, 8843.8]
    })
    invest['date'] = pd.to_datetime(invest['date'])
    invest = invest.set_index('date')
    invest['year'] = invest.index.year
    invest['month'] = invest.index.month
    return invest



def load_buildings():
    f = open('./datasets/house.txt', 'r')
    data = f.readline()
    f.close()
    dates = []
    for y in range(2015, 2021):
        for m in range(1, 13):
            dates.append(f'{y}-{m}-01')
    dates = dates[:-2]

    houses = pd.DataFrame({
        'square': list(map(float, data.split(','))),
        'date': dates
    })

    houses['date'] = pd.to_datetime(houses['date'])
    houses = houses.set_index('date')

    f = open('./datasets/apart.txt', 'r')
    data = f.readline()
    f.close()
    dates = []
    for y in range(2015, 2021):
        for m in range(1, 13):
            dates.append(f'{y}-{m}-01')
    dates = dates[2:-2]

    apart = pd.DataFrame({
        'square': list(map(float, data.split(','))),
        'date': dates
    })

    apart['date'] = pd.to_datetime(apart['date'])
    apart = apart.set_index('date')
    apart['sum'] = apart['square'] + houses['square']
    apart['year'] = apart.index.year
    apart['month'] = apart.index.month

    return apart
