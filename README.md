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

    RunHWM93



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
