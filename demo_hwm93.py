#!/usr/bin/env python3
"""
NOTE: The performance of this demo has not been checked at all.
Please do basic sanity checks of output.
Quick demo of calling NRL MSISE-00 using f2py3 from Python
Michael Hirsch
bostonmicrowave.com

Original fortran code by A. E. Hedin
(retired, formerly at NASA/GSFC)
from
ftp://hanna.ccmc.gsfc.nasa.gov/pub/modelweb/atmospheric/hwm93/
"""
from __future__ import division
from pandas import Series
from numpy import arange,asarray
from matplotlib.pyplot import figure,show
#
import hwm93

def testhwm93(ip,ap,altkm):
    stl = ip['sec']/3600 + ip['glon']/15

    merid = []; zonal=[]
    for a in altkm:
        m,z = hwm93.gws5(ip['iyd'],ip['sec'],a,ip['glat'],ip['glon'],stl,
                    ip['f107a'],ip['f107'], ap)
        merid.append(m)
        zonal.append(z)

    return asarray(merid),asarray(zonal)

def plothwm(merid,zonal,alt,ip):
    ax = figure().gca()
    ax.plot(merid,alt,color='b',label='merid')
    ax.plot(zonal,alt,color='r',label='zonal')
    ax.set_ylabel('altitude [km]')
    ax.set_xlabel('winds [m/s]')
    ax.legend(loc='best')
    ax.grid(True)
    ax.set_title('Meridional and Zonal winds from HWM93, lat/lon={:.1f},{:.1f}'.format(
                 ip['glat'],ip['glon']))


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='calls HWM93 from Python, a basic demo')
    p.add_argument('iyd',help='day of year [0-366]',type=int,nargs='?',default=172)
    p.add_argument('utsec',help='utc second from midnight [0-86400]',type=float,nargs='?',default=29000)
    p.add_argument('altkm',help='altitude (km) (start,stop,step)',type=float,nargs='?',default=(60,1000,5))
    p.add_argument('glat',help='geodetic latitude (deg)',type=float,nargs='?',default=60)
    p.add_argument('glon',help='geodetic longitude (deg)',type=float,nargs='?',default=-70)
    p.add_argument('F107a',help=' 81 day AVERAGE OF F10.7 FLUX (centered on day DDD)',type=float,nargs='?',default=150)
    p.add_argument('F107',help='DAILY F10.7 FLUX FOR PREVIOUS DAY',type=float,nargs='?',default=150)
    p.add_argument('AP',help='daily ap',type=float,nargs='?',default=4)
    p.add_argument('mass',help=('MASS NUMBER (ONLY DENSITY FOR SELECTED GAS IS ' +
                    'CALCULATED.  MASS 0 IS TEMPERATURE.  MASS 48 FOR ALL. '+
                    'MASS 17 IS Anomalous O ONLY.'),nargs='?',default=48)
    p = p.parse_args()

    inp = Series({'iyd':p.iyd, 'sec':p.utsec, 'glat':p.glat, 'glon':p.glon,
                  'f107a':p.F107a, 'f107':p.F107})

    altkm = arange(p.altkm[0],p.altkm[1],p.altkm[2])

    mer,zon = testhwm93(inp,p.AP,altkm)

    plothwm(mer,zon,altkm,inp)
    show()
