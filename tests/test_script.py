#!/usr/bin/env python
import pytest
import subprocess


def test_hwm():
    subprocess.check_call(['RunHWM93', ])


if __name__ == '__main__':
    pytest.main()
