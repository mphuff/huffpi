# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

setup(
    name='huffpi',
    version='0.0.1',
    description='Pi configuration details',
    long_description=readme,
    author='Micah Huff',
    author_email='micah@micahhuff.com',
    url='https://github.com/mphuff/huffpi',
    packages=find_packages(exclude=('tests', 'docs'))
)

