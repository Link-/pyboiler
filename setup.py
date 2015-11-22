from setuptools import setup, find_packages
import sys, os

VERSION = '0.3.0'
DESCRIPTION = """\
Creates a configurable python project template in a given directory."""

setup(name='pyboiler',
      version=VERSION,
      description=DESCRIPTION,
      long_description=DESCRIPTION,
      classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Build Tools'
      ],
      keywords='boilerplate python script configurable',
      author='Link-',
      author_email='bsm.dgdy@gmail.com',
      url='https://pypi.python.org/pypi/pyboiler',
      license='LICENSE',
      packages=['pyboiler'],
      include_package_data=True,
      zip_safe=True,
      entry_points={
          'console_scripts': [
              'pyboiler = pyboiler.pyboiler:main',
          ]
      }
)
