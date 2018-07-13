import numpy as np
import hwm93
from datetime import datetime
from sciencedates import datetime2gtd
import xarray


def runhwm93(t: datetime, altkm: np.ndarray, glat: float, glon: float,
             f107a: float, f107: float, ap: int) -> xarray.Dataset:
    altkm = np.atleast_1d(altkm).astype(float)
    iyd, utsec, stl = datetime2gtd(t, glon)

    merid = np.empty(altkm.size, dtype=float)
    zonal = np.empty(altkm.size, dtype=float)

    for i, a in enumerate(altkm):
        m, z = hwm93.gws5(iyd, utsec, a, glat, glon, stl, f107a, f107, ap)
        merid[i] = m
        zonal[i] = z

# %% assemble output
    winds = xarray.Dataset({'meridional': ('alt_km', merid), 'zonal': ('alt_km', zonal)},
                           coords={'alt_km': altkm},
                           attrs={'time': t, 'glat': glat, 'glon': glon})

    return winds
