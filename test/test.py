#!/usr/bin/env python3
from __future__ import division,absolute_import
from numpy.testing import assert_allclose
from datetime import datetime
from pytz import UTC
#
from pyhwm93.runhwm93 import runhwm93

def test_hwm():
    t = datetime(2013,3,31,12,tzinfo=UTC)
    glat = 65; glon=-148
    altkm=150
    f107a=100; f107=100; ap=4

    mer,zon = runhwm93(t,altkm,glat,glon,f107a,f107,ap)

    assert_allclose(mer,-110.16133881,rtol=1e-4) #gfortran 4.6 vs 5.2
    assert_allclose(zon,-12.40071201,rtol=1e-4) #gfortran 4.6 vs 5.2

if __name__ == '__main__':
    test_hwm()
