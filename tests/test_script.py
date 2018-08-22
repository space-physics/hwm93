#!/usr/bin/env python
import pytest
import subprocess


def test_hwm():
    pytest.importorskip('matplotlib')
    subprocess.check_call(['RunHWM93'])


if __name__ == '__main__':
    pytest.main(['-xv', __file__])
