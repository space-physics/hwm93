import numpy as np
import hwm93fort
from datetime import datetime
from sciencedates import datetime2gtd
from dateutil.parser import parse
import xarray


def run(time: datetime, altkm: np.ndarray, glat: float, glon: float,
        f107a: float, f107: float, ap: int) -> xarray.Dataset:
    altkm = np.atleast_1d(altkm).astype(float)

    if isinstance(time, str):
        time = parse(time)

    iyd, utsec, stl = datetime2gtd(time, glon)

    merid = np.empty(altkm.size, dtype=float)
    zonal = np.empty(altkm.size, dtype=float)

    for i, a in enumerate(altkm):
        w = hwm93fort.gws5(iyd, utsec, a, glat, glon, stl, f107a, f107, (ap, ap))
        merid[i] = w[0]
        zonal[i] = w[1]

# %% assemble output
    winds = xarray.Dataset({'meridional': ('alt_km', merid),
                            'zonal': ('alt_km', zonal)},
                           coords={'alt_km': altkm},
                           attrs={'time': time.isoformat(), 'glat': glat, 'glon': glon})

    return winds
