#!/usr/bin/env python
import setuptools  # noqa: F401
from numpy.distutils.core import setup, Extension
from pathlib import Path
import os


if os.name == "nt":
    sfn = Path(__file__).parent / "setup.cfg"
    stxt = sfn.read_text()
    if "[build_ext]" not in stxt:
        with sfn.open("a") as f:
            f.write("[build_ext]\ncompiler = mingw32")

ext = Extension(name="hwm93fort", sources=["src/hwm93_sub.f"], f2py_options=["only:", "gws5", ":"])

setup(ext_modules=[ext])
