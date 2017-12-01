#!/usr/bin/env python
install_requires = ['python-dateutil','pytz','numpy',
'gridaurora']
tests_require=['nose','coveralls']

from setuptools import find_packages
from numpy.distutils.core import setup,Extension

ext = Extension(name='hwm93',
                sources=['fortran/hwm93_sub.f'],
                f2py_options=['--quiet'])


setup(name='pyhwm93',
      ext_modules=[ext],
      packages=find_packages(),
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/pyhwm93',
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'tests':tests_require},
      python_requires='>=2.7',
	  )

