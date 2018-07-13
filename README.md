[![image](https://travis-ci.org/scivision/pyhwm93.svg)](https://travis-ci.org/scivision/pyhwm93)
[![Coverage Status](https://coveralls.io/repos/github/scivision/pyhwm93/badge.svg?branch=master)](https://coveralls.io/github/scivision/pyhwm93?branch=master)
[![Build status](https://ci.appveyor.com/api/projects/status/xtxdcmk601xti6l6?svg=true)](https://ci.appveyor.com/project/scivision/pyhwm93)
[![PyPi version](https://img.shields.io/pypi/pyversions/pyhwm93.svg)](https://pypi.python.org/pypi/pyhwm93)
[![PyPi formats](https://img.shields.io/pypi/format/pyhwm93.svg)](https://pypi.python.org/pypi/pyhwm93)
[![PyPi Download stats](http://pepy.tech/badge/pyhwm93)](http://pepy.tech/project/pyhwm93)


# HWM93 in Python

NASA Horizontal Wind Model HWM93 in Python


![image](tests/example.png)

Works with many Fortran compilers, including:

* Gfortran 5, 6, 7, 8
* Intel `ifort`
* PGI `pgf90`
* Nvidia `flang`


## Install

    pip install -e .
    
test by 

    pytest -sv

## Usage

Command line:

    RunHWM93 -h
    
Write data to NetCDF (HDF5) with `-o` option.
 
As a Python module:
```python
import pyhwm93
from datetime import datetime

winds = pyhwm93.runhwm93(t=datetime(2017,11,12,8), altkm=150., 
                         glat=65., glon=-148., f107a=150, f107=150, ap=4)
```

`winds` is an [xarray.Dataset](http://xarray.pydata.org/en/stable/generated/xarray.Dataset.html)

```
 <xarray.Dataset>
Dimensions:     (alt_km: 1)
Coordinates:
  * alt_km      (alt_km) float64 150.0
Data variables:
    meridional  (alt_km) float64 4.827
    zonal       (alt_km) float64 -20.5
Attributes:
    time:     2017-11-12T08:00:00
    glat:     65.0
    glon:     -148.0
``` 

If you want just a single variable, say
```python
print(winds.zonal.values)
```

## Notes

### [Optional] Fortran-only use

Most users don't need this.

    cd bin
    cmake ..
    cmake --build .
    
    
or

    f2py -c src/hwm93_sub.f  -m hwm93 only: gws5 :


### Reference

Original A. E. Hedin Fortran 77 HWM93 [code](ftp://hanna.ccmc.gsfc.nasa.gov/pub/modelweb/atmospheric/hwm93/)
