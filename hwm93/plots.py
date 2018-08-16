from matplotlib.pyplot import figure
import xarray


def plothwm(winds: xarray.Dataset):

    ax = figure().gca()
    ax.plot(winds['meridional'], winds.alt_km, label='meridional')
    ax.plot(winds['zonal'], winds.alt_km, label='zonal')
    ax.set_ylabel('altitude [km]')
    ax.set_xlabel('winds [m/s]')
    ax.legend(loc='best')
    ax.grid(True)
    ax.set_title(f'HWM93 Meridional / Zonal winds,\n '
                 f'{winds.time} lat/lon={winds.glat:.1f}, {winds.glon:.1f}')
