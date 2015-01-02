from setuptools import setup, find_packages
import sys, os

version = '0.2.0'

setup(name='pyboiler',
      version=version,
      description="Creates a configurable python project template in a given directory.",
      long_description="""\
Creates a configurable python project template in a given directory.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='boilerplate python script configurable',
      author='Link-',
      author_email='bd@bassemdy.com',
      scripts=['bin/pyboiler.py', 'bin/jparser.py', 'bin/jparser.pyc'],
      url='https://pypi.python.org/pypi/pyboiler',
      license='LICENSE',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
