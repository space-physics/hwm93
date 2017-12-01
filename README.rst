.. image:: https://travis-ci.org/scivision/pyhwm93.svg
    :target: https://travis-ci.org/scivision/pyhwm93
.. image:: https://coveralls.io/repos/github/scivision/pyhwm93/badge.svg?branch=master 
    :target: https://coveralls.io/github/scivision/pyhwm93?branch=master

============    
python-hwm93
============
NASA Horizontal Wind Model HWM93 in Python

.. contents::

.. image:: tests/example.png
    :scale: 25%

Installation
=============
::

    pip install -e .

Example usage
=============
::
    
    python demo_hwm93.py

Optional Fortran-only use
=========================
::
   
    cd bin
    cmake ..
    make


Reference
=========
Original A. E. Hedin Fortran 77 HWM93 code from 
ftp://hanna.ccmc.gsfc.nasa.gov/pub/modelweb/atmospheric/hwm93/
