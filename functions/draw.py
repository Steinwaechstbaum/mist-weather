'''
This module contains:
-Functions, which return its input as string
-Functions to plot and save the forecast
'''

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from operator import sub
from kivy.storage.jsonstore import JsonStore
import datetime
from functions import look_up

def rain_fill(num):
    '''
    Fills missing values and sets these to zero
    '''
    try:
        return num.get('rain').get('3h')
    except:
        return 0

def write_time(T, units):
    '''
    Return time string\n
    ToDo?: Different times
    '''
    T = datetime.datetime.fromtimestamp(T).strftime('%d %b %Y').center(50) + '\n' + (datetime.datetime.fromtimestamp(T).strftime('%H:%M:%S') + ' UTC').center(50)
    return T

def write_temp(TK, units):
    '''
    Return temp. string
    '''
    TK = (str(round(look_up.conv_temp(TK, units), 2)) + ' ' + look_up.temp_str.get(units)).center(50)
    return TK

def write_perc(num: float, units: int):
    '''
    Return perc. string
    '''
    num = round(look_up.conv_perc(num, units), 2)
    return str(num) + ' ' + look_up.perc_str.get(units)

def write_clouds(num, descr, units):
    '''
    Return clouds string
    '''
    return write_perc(num, units).center(50) + '\n' + ('(' + descr + ')').center(50)

def write_wind(vel, deg, units):
    '''
    Return wind string\n
    has to be build different from other strings
    '''
    if units == 0:
        vel = str(vel) + ' ' + look_up.vel_str.get(units)
    elif units == 1:
        vel = str(round(look_up.conv_speed(vel, units), 2)) + ' \u00D710[sup]-8[/sup]c'
    elif units == 2:
        vel = str(round(look_up.conv_speed(vel, units), 2)) + '\u00D710[sup]\u22124[/sup] AU/yr'#look_up.vel_str.get(units)
    return vel.center(50) + '\n' + ('(' + str(round(look_up.conv_deg(deg, units), 2)) + look_up.deg_str.get(units) + ')').center(50)

def weather_icon(id: int):
    '''
    Returns icon name depending on weather id
    '''
    name = ''
    if id > 800:
        name += '081.png'
    elif id == 800:
        name += '08.png'
    elif id >= 700:
        name += '07.png'
    elif id >= 600:
        name += '06.png'
    elif id >= 500:
        name += '05.png'
    elif id >= 300:
        name += '03.png'
    elif id >= 200:
        name += '02.png'
    return name

def background_image(T: int, id: int):
    '''
    Select background image dependend on current time and weather
    '''
    hour = int(datetime.datetime.fromtimestamp(T).strftime('%H'))
    name = ''
    if hour > 6 and hour < 18:
        name += 'day_'
    else:
        name += 'night_'
    return name + weather_icon(id)

def x_axis(ax, unit: int):
    '''
    Sets the axis labeling type and tick position\n
    ToDo?: Different times
    '''
    ax.xaxis.set_major_locator(mdates.DayLocator())
    ax.xaxis.set_minor_locator(mdates.HourLocator(interval=4))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %b %Y'))
    ax.xaxis.set_minor_formatter(mdates.DateFormatter('%H:%M'))


def plot_all(unit: int):
    '''
    Plots Temp., rain, wind, pressure, humdity, clouds and stores the plots in one .png
    '''
    #Read in data and divide it into lists
    data = JsonStore('./storage/forecast.json').get('list')

    dt = [look_up.conv_time(i.get('dt'), unit) for i in data]
    dt = [datetime.datetime.strptime(i, '%d %b %Y\n%H:%M:%S') for i in dt]
    T = [look_up.conv_temp(i.get('main').get('temp'), unit) for i in data]
    T_min, T_max = [look_up.conv_temp(i.get('main').get('temp_min'), unit) for i in data], [look_up.conv_temp(i.get('main').get('temp_max'), unit) for i in data] 
    T_err_min, T_err_max = list(map(sub, T, T_min)), list(map(sub, T_max, T))
    rain_lst = [look_up.conv_len(rain_fill(i), unit) for i in data]
    wind_speed = [look_up.conv_speed(i.get('wind').get('speed'), unit) for i in data]
    gust_speed = [look_up.conv_speed(i.get('wind').get('gust'), unit) for i in data]
    press_lst = [look_up.conv_pres(i.get('main').get('pressure'), unit) for i in data]
    hum_lst = [look_up.conv_perc(i.get('main').get('humidity'), unit) for i in data]
    cloud_lst = [look_up.conv_perc(i.get('clouds').get('all'), unit) for i in data]

    #Create figure
    fig = plt.figure()
    fig.set_size_inches(20, 20)
    fig.tight_layout()
    fig.set_edgecolor('white')
    fig.set_facecolor((1,1,1,0))

    temp   = fig.add_subplot(6,1,1)
    rain   = fig.add_subplot(6, 1, 2)
    wind   = fig.add_subplot(6, 1, 3)
    pres   = fig.add_subplot(6, 1, 4)
    hum    = fig.add_subplot(6, 1, 5)
    clouds = fig.add_subplot(6,1,6)

    #Apply plot specific settings
    for i in [temp, rain, wind, pres, hum, clouds]:
        i.set_facecolor((.9,.9,.9,.2))
        i.tick_params('y', colors='white')
        x_axis(i, 0)
        i.tick_params('x', colors='white', which='minor')
        i.tick_params('x', colors=(1,1,1,0), which='major')
        i.xaxis.grid(True,'minor')
        i.xaxis.grid(True,'major',linewidth=2)
        for j in ['right', 'left', 'top', 'bottom']:
            i.spines[j].set_color('white')

    temp.set_ylabel(f'Temperature ({look_up.temp_str.get(unit)})', color='white')
    rain.set_ylabel(f'Rain ({look_up.length_str.get(unit)})', color='white')
    wind.set_ylabel(f'Wind ({look_up.vel_str.get(unit)})', color='white')
    pres.set_ylabel(f'Pressure ({look_up.pressure_str.get(unit)})', color='white')
    hum.set_ylabel(f'Humidity ({look_up.perc_str.get(unit)})', color='white')
    clouds.set_ylabel(f'Clouds ({look_up.perc_str.get(unit)})', color='white')
    temp.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
    temp.tick_params('x', colors=(1,1,1,1))

    #Plot temperature
    temp.errorbar(dt, T, yerr=(T_err_min, T_err_max), 
                ls='dashed', marker='x', color='orange', 
                barsabove=True, capsize=2.5, markerfacecolor='red',
                ecolor='red', markeredgecolor='red')
    temp.fill_between(dt, min(T), T, 
                      color=(.5,.3,0,.7))

    #Plot rain
    rain.fill_between(dt, 0, rain_lst, 
                      color=(0,0,.5,.7))
    rain.plot(dt, rain_lst, 
              color='blue')

    #Plot wind
    wind.plot(dt, wind_speed, 
              color='navy', ls='dashed', marker='x', 
              markeredgecolor='darkred',
              markerfacecolor='darkred')
    wind.fill_between(dt, 0, gust_speed, 
                      color=(1,1,1,.7))

    #Plot pressure
    pres.plot(dt, press_lst, 
              color='white', marker='x')

    #Plot humidity
    hum.plot(dt, hum_lst, 
             color=(.2,.2,.8,1), ls='dashed', marker='x')
    hum.fill_between(dt, min(hum_lst), hum_lst, 
                     color=(.2,.2,.8,.7))

    #Plot clouds
    clouds.plot(dt, cloud_lst, 
                color=(.3,.3,.3,1), marker='o')
    clouds.fill_between(dt, min(cloud_lst), cloud_lst, 
                        color=(1,1,1,.7))

    fig.savefig('./Images/forecast.png', facecolor=fig.get_facecolor())
    return 0

plot_all(1)