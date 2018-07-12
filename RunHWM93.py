#!/usr/bin/env python
"""
NOTE: The performance of this demo has not been checked at all.
Please do basic sanity checks of output.
Quick demo of calling HWM93 using f2py3 from Python
Michael Hirsch

Original fortran code by A. E. Hedin
from ftp://hanna.ccmc.gsfc.nasa.gov/pub/modelweb/atmospheric/hwm93/
"""
from numpy import arange
from matplotlib.pyplot import show
from dateutil.parser import parse
from argparse import ArgumentParser
from pyhwm93 import runhwm93
from pyhwm93.plots import plothwm
import seaborn as sns
sns.set_context('talk')


def main():
    p = ArgumentParser(description='calls HWM93 from Python, a basic demo')
    p.add_argument('simtime', help='yyyy-mm-ddTHH:MM:SSZ time of sim', nargs='?', default='2016-01-01T12Z')
    p.add_argument('-a', '--altkm', help='altitude (km) (start,stop,step)', type=float, nargs='+', default=(60, 1000, 5))
    p.add_argument('-c', '--latlon', help='geodetic latitude (deg)', type=float, default=(65, -148))
    p.add_argument('f107a', help=' 81 day AVERAGE OF F10.7 FLUX (centered on day DDD)', type=float, nargs='?', default=150)
    p.add_argument('f107', help='DAILY F10.7 FLUX FOR PREVIOUS DAY', type=float, nargs='?', default=150)
    p.add_argument('ap', help='daily ap', type=float, nargs='?', default=4)
    p = p.parse_args()

    altkm = arange(p.altkm[0], p.altkm[1], p.altkm[2])

    glat, glon = p.latlon

    T = parse(p.simtime)

    mer, zon = runhwm93(T, altkm, glat, glon, p.f107a, p.f107, p.ap)

    plothwm(mer, zon, altkm, T, glat, glon)
    show()


if __name__ == '__main__':
    main()
