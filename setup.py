#!/usr/bin/env python3
import setuptools
import subprocess

try:
    subprocess.run(['conda','install','--yes','--file','requirements.txt'])
except Exception as e:
    print('you will need to install packages in requirements.txt  {}'.format(e))

from numpy.distutils.core import setup,Extension

with open('README.rst','r') as f:
  	long_description = f.read()

setup(name='pyhwm93',
      version='0.1',
	  description='HWM93 model',
	  long_description=long_description,
	  author='Michael Hirsch',
	  url='https://github.com/scienceopen/pyhwm93',
      dependency_links = ['https://github.com/scienceopen/gridaurora/tarball/master#egg=gridaurora'],
	  install_requires=['gridaurora'],
      packages=['pyhwm93'],
      ext_modules=[Extension(name='hwm93',
                sources=['fortran/hwm93_sub.for'],
                f2py_options=['--quiet'])]
	  )

