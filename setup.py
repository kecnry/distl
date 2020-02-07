#!/usr/bin/env python

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='distl',
      version='0.1.0-dev',
      description='Simple Distributions: math operations, serializing, covariances',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Kyle Conroy',
      author_email='kyleconroy@gmail.com',
      url='https://www.github.com/kecnry/distl',
      # download_url = 'https://github.com/kecnry/distl/tarball/1.0.0',
      packages=['distl'],
      classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
       ],
     )
