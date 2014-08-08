# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import os


def pytest_runtest_setup(item):
    base_dir = os.path.abspath(os.path.join(os.getcwd(), 'sample'))
    os.environ.setdefault('SSC_SEARCH_PATH',
                          os.path.join(base_dir))

    os.environ.setdefault('SSC_YAML_SEARCH_PATH',
                          os.path.join(base_dir, 'yaml'))
    os.environ.setdefault('SSC_YAML_SEARCH_RECURSIVE',
                          '1')

    os.environ.setdefault('SSC_XLS_SEARCH_PATH',
                          os.path.join(base_dir, 'xls'))
    os.environ.setdefault('SSC_XLS_SEARCH_RECURSIVE',
                          '1')

    os.environ.setdefault('SSC_JSON_BASE_PATH',
                          os.path.join(base_dir, 'json'))

    return ''
