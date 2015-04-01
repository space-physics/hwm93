#!/usr/bin/env python3
"""
NOTE: The performance of this demo has not been checked at all.
Please do basic sanity checks of output.
Quick demo of calling HWM93 using f2py3 from Python
Michael Hirsch
bostonmicrowave.com

Original fortran code by A. E. Hedin
from
ftp://hanna.ccmc.gsfc.nasa.gov/pub/modelweb/atmospheric/hwm93/
"""
from __future__ import division
from numpy import arange,asarray
from matplotlib.pyplot import figure,show
#
import sys
sys.path.append('../msise-00/') #git clone https://github.com/scienceopen/msise-00.git
from fortrandates import datetime2gtd
try:
    import hwm93
except ImportError as e:
    exit('you must compile using f2py. Please see README.md. ' + str(e))

def testhwm93(dtime,altkm,glat,glon,f107a,f107,ap):
    iyd,utsec,stl = datetime2gtd(dtime,glon)

    merid = []; zonal=[]
    for a in altkm:
        m,z = hwm93.gws5(iyd,utsec,a,glat,glon,stl,f107a, f107, ap)
        merid.append(m)
        zonal.append(z)

    return asarray(merid),asarray(zonal)

def plothwm(merid,zonal,alt,glat,glon):
    ax = figure().gca()
    ax.plot(merid,alt,color='b',label='merid')
    ax.plot(zonal,alt,color='r',label='zonal')
    ax.set_ylabel('altitude [km]')
    ax.set_xlabel('winds [m/s]')
    ax.legend(loc='best')
    ax.grid(True)
    ax.set_title('Meridional and Zonal winds from HWM93,\n lat/lon={:.1f},{:.1f}'.format(glat,glon))


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='calls HWM93 from Python, a basic demo')
    p.add_argument('simtime',help='yyyy-mm-ddTHH:MM:SSZ time of sim',type=str,nargs='?',default='')
    p.add_argument('-a','--altkm',help='altitude (km) (start,stop,step)',type=float,nargs='+',default=(60,1000,5))
    p.add_argument('-c','--latlon',help='geodetic latitude (deg)',type=float,default=(65,-148))
    p.add_argument('f107a',help=' 81 day AVERAGE OF F10.7 FLUX (centered on day DDD)',type=float,nargs='?',default=150)
    p.add_argument('f107',help='DAILY F10.7 FLUX FOR PREVIOUS DAY',type=float,nargs='?',default=150)
    p.add_argument('ap',help='daily ap',type=float,nargs='?',default=4)
    p = p.parse_args()

    altkm = arange(p.altkm[0],p.altkm[1],p.altkm[2])

    glat,glon = p.latlon

    mer,zon = testhwm93(p.simtime,altkm,glat,glon,p.f107a,p.f107,p.ap)

    plothwm(mer,zon,altkm,glat,glon)
    show()
