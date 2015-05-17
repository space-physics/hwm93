[![Code Climate](https://codeclimate.com/github/scienceopen/pyhwm93/badges/gpa.svg)](https://codeclimate.com/github/scienceopen/pyhwm93)
# python-hwm93
NASA Horizontal Wind Model HWM93 in Python

Installation
-------------
```
git clone --depth 1 --recursive https://github.com/scienceopen/pyhwm93
pip install -r requirements.txt
make -f Makefile.f2py
```

Example usage:
----------------
```
python demo_hwm93.py
```


#### Reference
Original A. E. Hedin Fortran 77 HWM93 code from
ftp://hanna.ccmc.gsfc.nasa.gov/pub/modelweb/atmospheric/hwm93/
