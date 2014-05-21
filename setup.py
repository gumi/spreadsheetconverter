#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from setuptools import setup, find_packages


try:
    with open('README.rst') as f:
        readme = f.read()
except IOError:
    readme = ''

setup(
    name="SpreadsheetConverter",
    version='0.0.2',
    url='https://github.com/yamionp/spreadsheetconverter/',
    author='yamionp',
    author_email='yami@crimsondream.jp',
    maintainer='yamionp',
    maintainer_email='yami@crimsondream.jp',
    description='Spreadsheet Converter',
    long_description=readme,
    license="MIT",
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'License :: OSI Approved :: MIT License',
    ]
)
