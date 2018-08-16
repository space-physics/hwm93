#!/usr/bin/env python
"""
Michael Hirsch

Original fortran code by A. E. Hedin
from ftp://hanna.ccmc.gsfc.nasa.gov/pub/modelweb/atmospheric/hwm93/
"""
from pathlib import Path
from numpy import arange
from dateutil.parser import parse
from argparse import ArgumentParser
import hwm93
from matplotlib.pyplot import show
from hwm93.plots import plothwm


def main():
    p = ArgumentParser(description='calls HWM93 from Python, a basic demo')
    p.add_argument('simtime', help='yyyy-mm-ddTHH:MM:SS time of sim', nargs='?', default='2016-01-01T12')
    p.add_argument('-a', '--altkm', help='altitude (km) (start,stop,step)',
                   type=float, nargs='+', default=(60, 1000, 5))
    p.add_argument('-c', '--latlon', help='geodetic latitude (deg)',
                   type=float, default=(65, -148))
    p.add_argument('f107a', help=' 81 day AVERAGE OF F10.7 FLUX (centered on day DDD)',
                   type=float, nargs='?', default=150)
    p.add_argument('f107', help='DAILY F10.7 FLUX FOR PREVIOUS DAY',
                   type=float, nargs='?', default=150)
    p.add_argument('ap', help='daily ap', type=int, nargs='?', default=4)
    p.add_argument('-o', '--outfn', help='write NetCDF (HDF5) of data')
    p = p.parse_args()

    altkm = arange(p.altkm[0], p.altkm[1], p.altkm[2])

    glat, glon = p.latlon

    T = parse(p.simtime)

    winds = hwm93.run(T, altkm, glat, glon, p.f107a, p.f107, p.ap)

    if p.outfn:
        outfn = Path(p.outfn).expanduser()
        print('writing', outfn)
        winds.to_netcdf(outfn)

   
    plothwm(winds)

    show()


if __name__ == '__main__':
    main()
