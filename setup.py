#!/usr/bin/env python3
import setuptools
from numpy.distutils.core import setup,Extension

with open('README.rst','r') as f:
  	long_description = f.read()

setup(name='pyhwm93',
      version='0.1',
	  description='HWM93 model',
	  long_description=long_description,
	  author='Michael Hirsch',
	  url='https://github.com/scienceopen/pyhwm93',
   dependency_links = ['https://github.com/scienceopen/histutils/tarball/master#egg=histutils'],
	  install_requires=['histutils'],
      packages=['pyhwm93'],
  ext_modules=[Extension(name='hwm93',
                sources=['fortran/hwm93_sub.for'],
                f2py_options=['--quiet'])]
	  )

