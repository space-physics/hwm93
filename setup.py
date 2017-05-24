#!/usr/bin/env python
req = ['nose','python-dateutil','pytz','numpy','matplotlib','seaborn']
pipreq=['gridaurora']

import pip
try:
    import conda.cli
    conda.cli.main('install',*req)
except Exception:
    pip.main(['install'] + req)
pip.main(['install'] + pipreq)

#%%
import setuptools
from numpy.distutils.core import setup,Extension

ext = Extension(name='hwm93',
                sources=['fortran/hwm93_sub.for'],
                f2py_options=['--quiet'])


setup(name='pyhwm93',
      ext_modules=[ext],
      packages=['pyhwm93'],
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/pyhwm93',
	  )

