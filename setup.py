#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from setuptools import setup, find_packages

setup(
    name="SpreadsheetConverter",
    version='0.0.1',
    url='https://github.com/yamionp/spreadsheetconverter/',
    author='yamionp',
    author_email='yami@crimsondream.jp',
    maintainer='yamionp',
    maintainer_email='yami@crimsondream.jp',
    description='Spreadsheet Converter',
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
