from numpy import asarray,atleast_1d
#
import hwm93
from sciencedates import datetime2gtd

def runhwm93(t,altkm,glat,glon,f107a,f107,ap):
    altkm = atleast_1d(altkm)
    iyd,utsec,stl = datetime2gtd(t,glon)

    merid = []; zonal=[]
    for a in altkm:
        m,z = hwm93.gws5(iyd,utsec,a,glat,glon,stl,f107a, f107, ap)
        merid.append(m)
        zonal.append(z)

    return asarray(merid),asarray(zonal)
