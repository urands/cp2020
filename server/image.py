import io
from sklearn.linear_model import LinearRegression
from flask import Response, request
from shared import power, invest, apart
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from pylab import rcParams

rcParams['figure.figsize'] = 16, 8
rcParams.update({'figure.autolayout': True})


def base_model(df, ax1, field = 'E_USE_FACT'):
    color = 'tab:blue'
    # fig.title('График')
    ax1.set_xlabel('Дата')
    ax1.set_ylabel('Потребление (МВт*ч)', color=color)
    ax1.plot(df.index, df[field], color=color)
    ax1.tick_params(axis='y', labelcolor=color)

def add_plot(df,ax1, field = 'TEMP', title = 'Температура (С)', color = 'tab:red'):
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    ax2.set_ylabel(title, color=color)  # we already handled the x-label with ax1
    ax2.plot(df.index, df[field], color=color)
    ax2.tick_params(axis='y', labelcolor=color)



def clear_data(year=2015):
    global power
    lr = LinearRegression()
    df_year = power[power.index.year == year].groupby('M_DATE_DAY').mean().fillna(0)
    df_year['TEMP2'] = df_year['TEMP']* df_year['TEMP']
    df_year['TEMP3'] = df_year['TEMP'] ** 3
    x = df_year[['TEMP', 'TEMP2', 'TEMP3']].fillna(0).values
    # x = df_year[['TEMP','TEMP2']].values
    # x = df_year[['TEMP']].values
    y = df_year.E_USE_FACT.values
    lr.fit(x, y)
    a = lr.intercept_
    b = lr.coef_[0]
    c = lr.coef_[1]
    d = lr.coef_[2]
    f = lambda x: a + b*x + c*x*x + d*x*x*x
    # f = lambda x : a + b*x +c*x*x
    power['E_USE_LINE'] = power.TEMP.apply(f)
    power['E_USE_CLEAN'] = power.E_USE_FACT - power.E_USE_LINE


def render_image():
    global power, invest, apart
    fig = Figure()
    ax1 = fig.add_subplot(1, 1, 1)
    
    fig.tight_layout()  # otherwise the right y-label is slightly clipped

    start = request.args.get('start', default='2020-01-01', type=str)
    stop = request.args.get('stop', default='2020-12-01', type=str)
    mode = request.args.get('mode', default='', type=str)
    invest_f = request.args.get('invest', default='', type=str)
    apart_f = request.args.get('apart', default='', type=str)
    temp_f = request.args.get('temp', default='', type=str)


    try:
        df = power[(power.index >= start) & (power.index <= stop)]
    except:
        start = '2020-01-01'
        stop = '2020-12-01'
        df = power[(power.index >= start) & (power.index <= stop)]



    if mode == 'clean':
        clear_data()
        df = power[(power.index >= start) & (power.index <= stop)]
        #base_model(df, ax1,'E_USE_CLEAN')
    elif mode == 'invest1':
        clear_data()
        df = power[(power.index >= start) & (power.index <= stop)]
        base_model(df, ax1,'E_USE_CLEAN')
    else:
        if mode == 'year':
            df = df.groupby('year').mean()
        if mode == 'month':
            df = df.groupby('month').mean()

        base_model(df, ax1)


    if temp_f!='':
        df = power[(power.index >= start) & (power.index <= stop)]
        if mode == 'year':
            df = df.groupby('year').mean()
        if mode == 'month':
            df = df.groupby('month').mean()

        if len(df) > 0:
            add_plot(df,ax1)

    if invest_f!='':
        df = invest[(invest.index >= start) & (invest.index <= stop)]
        if mode == 'year':
            df = df.groupby('year').mean()
        if mode == 'month':
            df = df.groupby('month').mean()

        if len(df)>0:
            add_plot(df,ax1, 'money', 'ИНВЕСТИЦИИ млн. руб.', color='green')

    if apart_f!='':
        df = apart[(apart.index >= start) & (apart.index <= stop)]
        if mode == 'year':
            df = df.groupby('year').mean()
        if mode == 'month':
            df = df.groupby('month').mean()

        if len(df) > 0:
            add_plot(df,ax1, 'sum', 'Введенная недвижимость  кв.м.', color='green')

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return output
