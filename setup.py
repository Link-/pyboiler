from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pyboiler',
      version=version,
      description="Creates a configurable python project template in a given directory.",
      long_description="""\
Creates a configurable python project template in a given directory.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='boilerplate python script configurable',
      author='Link-',
      author_email='bd@bassemdy.com',
      url='http://bassemdy.com',
      license='WTFPL',
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
