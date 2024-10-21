'''
This module contains:
-Look-up dictionaries for the units
-conversion functions
'''
import datetime
from math import sqrt

#String dictionaries
temp_str = {0:'\u00b0C', 1:'meV', 2: '\u03bcm'}
length_str = {0: 'mm', 1: '1/meV', 2:'$r_\u2641\u00D710\u207B\u2077$'}
pressure_str = {0: 'hPa', 1:'$\\frac{\mathrm{eV}^4}{c^2\hbar^3}\u00D710^{-3}$', 2:'pm'}
perc_str = {0: '%', 1: '\u03b1', 2: 'sr'}
deg_str = {0: '\u00b0', 1: '\u03c0', 2: '"'}
vel_str = {0: 'm/s', 1: '$c\u00D710^{-8}$', 2: 'AU/yr\u00D710\u207B\u2074'}

#Constants
r_e = 6378137
PI = 3.1415927

def conv_temp(T: float, units: int):
    '''
    Converts temperature dependent on given unit
    '''
    #K to SI, [T]=°C
    if units == 0:
        T = T - 273.15
    #K to eV via k_b, [T]=meV
    elif units == 1:
        T = T * (1.380649e-23/1.602176634e-19)*1000
    #K to \mu m via Wien law (\lambda_peak) [T]=\mu m
    elif units == 2:
        T = 2.897772e3 /T
    return T

def conv_len(l: float, units: int):
    '''
    Converts length dependent on given unit
    '''
    #Default: [l]=mm
    if units == 0:
        l = l
    #Nat.: [l]=1/meV, via \hbar*c
    elif units == 1:
        l *= 0.197
    #Astr.: [l]=r_earth
    elif units == 2:
        l = l/r_e*1e7
    return l

def conv_speed(v: float, units: int):
    '''
    Converts speed dependent on given unit
    '''
    #SI: [v]=m/s
    if units == 0:
        v = v 
    #Nat.: [v]=c
    elif units == 1:
        v = v / 299792458 * 1e8
    #Astr.: [v]=AU/yr
    elif units == 2:
        v = v * (31557600/14959787e4) * 1e4
    return v

def conv_time(t: float, units: int):
    '''
    ToDo?: Different times
    '''
    t = datetime.datetime.fromtimestamp(t).strftime('%d %b %Y\n%H:%M:%S')
    return t

def conv_perc(num: float, units: int):
    #Default: Given in %
    if units == 0:
        pass
    #Nat.: Multiples of \alpha
    elif units == 1:
        num *= 137/100
    #Astr.: Given in sr
    else:
        num = num/100*4*PI
    return num

def conv_deg(deg: float, units: int):
    '''
    Converts deg dependent on given unit
    '''
    #Default: Given in deg
    if units == 0:
        pass
    #Nat.: Given in rad
    elif units == 1:
        deg = deg/180
    #Astr.: Given in arcsec
    elif units == 2:
        deg = deg/3600
    return deg

def conv_pres(P: float, units: int):
    '''
    Converts pressure [bar] dependent on given unit
    '''
    #Default: [P]=bar
    if units == 0:
        pass
    #Nat.: [P]=eV^4/c^3hbar^2
    elif units == 1:
        P = P/4.7956683e4*1e3
    #Astr.: r of neutron star with \rho=8.35e16kg/m^3
    elif units == 2:
        P = sqrt(3/(2*PI)*P/(6.67430e-11*(8.35e16)**2))*1e12
    return P
