#!/usr/bin/env python
import pytest
import subprocess
import sys
from pathlib import Path

R = Path(__file__).resolve().parents[1]


def test_hwm():
    pytest.importorskip("matplotlib")
    subprocess.check_call([sys.executable, "RunHWM93.py"], cwd=R)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
