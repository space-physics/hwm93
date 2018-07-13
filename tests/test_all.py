#!/usr/bin/env python
from numpy.testing import assert_allclose
import pytest
from datetime import datetime
import pyhwm93


def test_hwm():
    t = datetime(2013, 3, 31, 12)
    glat = 65
    glon = -148
    altkm = 150
    f107a = 100
    f107 = 100
    ap = 4

    wind = pyhwm93.run(t, altkm, glat, glon, f107a, f107, ap)

    assert_allclose(wind['meridional'], -110.16133881, rtol=1e-4)  # gfortran 4.6 vs 5.2
    assert_allclose(wind['zonal'], -12.40071201, rtol=1e-4)  # gfortran 4.6 vs 5.2


if __name__ == '__main__':
    pytest.main()
