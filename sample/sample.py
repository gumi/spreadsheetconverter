# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from spreadsheetconverter import Converter, YamlConfig


if __name__ == '__main__':
    converter = Converter(YamlConfig('user.yaml'))
    converter.run()
