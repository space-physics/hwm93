from numpy import asarray,atleast_1d
from matplotlib.pyplot import figure
#
import hwm93
from histutils.fortrandates import datetime2gtd

def runhwm93(t,altkm,glat,glon,f107a,f107,ap):
    altkm = atleast_1d(altkm)
    iyd,utsec,stl = datetime2gtd(t,glon)

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
