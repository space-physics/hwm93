#!/usr/bin/env python
import setuptools
try:
    import conda.cli
    conda.cli.main('install','--file','requirements.txt')
except Exception as e:
    print(e)

from numpy.distutils.core import setup,Extension

ext = Extension(name='hwm93',
                sources=['fortran/hwm93_sub.for'],
                f2py_options=['--quiet'])


setup(name='pyhwm93',
      dependency_links = ['https://github.com/scienceopen/gridaurora/tarball/master#egg=gridaurora'],
	  install_requires=['gridaurora'],
      ext_modules=[ext],
      packages=['pyhwm93'],
	  )

