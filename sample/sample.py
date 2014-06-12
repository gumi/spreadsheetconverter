# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import os
from spreadsheetconverter import Converter, YamlConfig


if __name__ == '__main__':
    os.environ.setdefault('SSC_SEARCH_PATH',
                          os.path.join(os.getcwd()))

    os.environ.setdefault('SSC_YAML_SEARCH_PATH',
                          os.path.join(os.getcwd(), 'yaml'))
    os.environ.setdefault('SSC_YAML_SEARCH_RECURSIVE',
                          '1')

    os.environ.setdefault('SSC_XLS_SEARCH_PATH',
                          os.path.join(os.getcwd(), 'xls'))
    os.environ.setdefault('SSC_XLS_SEARCH_RECURSIVE',
                          '1')

    os.environ.setdefault('SSC_JSON_BASE_PATH',
                          os.path.join(os.getcwd(), 'json'))

    converter = Converter(YamlConfig.get_config('user/user.yaml'))
    converter.run()
