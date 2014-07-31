#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import os

from setuptools import setup, find_packages


try:
    with open('README.rst') as f:
        readme = f.read()
except IOError:
    readme = ''


def _requires_from_file(filename):
    return open(filename).read().splitlines()


tests_require = _requires_from_file('test-requirements.txt')

# version
here = os.path.dirname(os.path.abspath(__file__))
version = next((line.split('=')[1].strip().replace("'", '')
                for line in open(os.path.join(here,
                                              'spreadsheetconverter',
                                              '__init__.py'))
                if line.startswith('__version__ = ')),
               '0.0.dev0')

setup(
    name="SpreadsheetConverter",
    version=version,
    url='https://github.com/yamionp/spreadsheetconverter/',
    author='yamionp',
    author_email='yami@crimsondream.jp',
    maintainer='yamionp',
    maintainer_email='yami@crimsondream.jp',
    description='Spreadsheet Converter',
    long_description=readme,
    license="MIT",
    packages=find_packages(),
    install_requires=_requires_from_file('requirements.txt'),
    tests_require=tests_require,
    extras_require={"testing": tests_require},
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
