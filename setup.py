#!/usr/bin/env python
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='sentfrag',
    version='0.0.1',
    description='Automating Gopen\'s techniques',
    author='Prajal Bishwakarma',
    author_email='prajal.b@gmail.com',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
)