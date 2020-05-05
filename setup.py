#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup


setup(
    name='wiz0',
    version='0.0.1',
    description='The wizard is in',
    author='Sean Jain Ellis',
    author_email='sellis@bandarji.com',
    packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests_*', 'tests']),
    py_modules=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests_*', 'tests']),
    entry_points={
        'console_scripts': [],
    },
    include_package_data=True,
    python_requires='>=3.7',
    install_requires=[]
)
