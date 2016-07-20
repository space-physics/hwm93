#!/usr/bin/env python
import setuptools
import subprocess

try:
    subprocess.call(['conda','install','--file','requirements.txt'])
except Exception as e:
    pass

from numpy.distutils.core import setup,Extension

ext = Extension(name='hwm93',
                sources=['fortran/hwm93_sub.for'],
                f2py_options=['--quiet'])


setup(name='pyhwm93',
	  description='HWM93 model',
	  author='Michael Hirsch',
	  url='https://github.com/scienceopen/pyhwm93',
      dependency_links = ['https://github.com/scienceopen/gridaurora/tarball/master#egg=gridaurora'],
	  install_requires=['gridaurora'],
      ext_modules=[ext],
      packages=['pyhwm93'],
	  )

