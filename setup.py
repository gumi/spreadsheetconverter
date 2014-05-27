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

install_requires = [
    'six >= 1.6',
    'PyYAML>=3.11',
    'xlrd >= 0.9.3',
]

setup(
    name="SpreadsheetConverter",
    version='0.0.8',
    url='https://github.com/yamionp/spreadsheetconverter/',
    author='yamionp',
    author_email='yami@crimsondream.jp',
    maintainer='yamionp',
    maintainer_email='yami@crimsondream.jp',
    description='Spreadsheet Converter',
    long_description=readme,
    license="MIT",
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      ssconvert = spreadsheetconverter.scripts.convert:main
    """,
)
