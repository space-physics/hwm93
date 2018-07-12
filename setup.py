#!/usr/bin/env python
import setuptools  # noqa: F401
from numpy.distutils.core import setup, Extension

ext = Extension(name='hwm93',
                sources=['src/hwm93_sub.f'],
                f2py_options=['--quiet'])

setup(ext_modules=[ext])
