#!/usr/bin/env python
from pytest import approx
import pytest
from datetime import datetime
import hwm93


def test_hwm():
    t = datetime(2013, 3, 31, 12)
    glat = 65
    glon = -148
    altkm = 150
    f107a = 100
    f107 = 100
    ap = 4

    wind = hwm93.run(t, altkm, glat, glon, f107a, f107, ap)

    assert wind["meridional"] == approx(-110.16133881, rel=1e-4)  # gfortran 4.6 vs 5.2
    assert wind["zonal"] == approx(-12.40071201, rel=1e-4)  # gfortran 4.6 vs 5.2


if __name__ == "__main__":
    pytest.main(["-v", __file__])
