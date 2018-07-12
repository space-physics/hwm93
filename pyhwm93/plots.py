from matplotlib.pyplot import figure


def plothwm(merid, zonal, alt, T, glat, glon):
    ax = figure().gca()
    ax.plot(merid, alt, color='b', label='merid')
    ax.plot(zonal, alt, color='r', label='zonal')
    ax.set_ylabel('altitude [km]')
    ax.set_xlabel('winds [m/s]')
    ax.legend(loc='best')
    ax.grid(True)
    ax.set_title('HWM93 Meridional / Zonal winds,\n {} lat/lon={:.1f},{:.1f}'.format(T, glat, glon))
