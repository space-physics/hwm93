.. image:: https://travis-ci.org/scienceopen/pyhwm93.svg
    :target: https://travis-ci.org/scienceopen/pyhwm93

.. image:: https://codeclimate.com/github/scienceopen/pyhwm93/badges/gpa.svg
    :target: https://codeclimate.com/github/scienceopen/pyhwm93

============    
python-hwm93
============
NASA Horizontal Wind Model HWM93 in Python

Installation
=============
::

    python setup.py develop

Example usage
=============
::
    
    python demo_hwm93.py

Optional Fortran-only use
=========================
::
   
    cd bin
    cmake ../fortran
    make


Reference
=========
Original A. E. Hedin Fortran 77 HWM93 code from 
ftp://hanna.ccmc.gsfc.nasa.gov/pub/modelweb/atmospheric/hwm93/
