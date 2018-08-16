#!/usr/bin/env python
import setuptools  # noqa: F401
from numpy.distutils.core import setup, Extension

ext = Extension(name='hwm93fort',
                sources=['src/hwm93_sub.f'],
                f2py_options=['only:', 'gws5', ':'])

setup(ext_modules=[ext])
