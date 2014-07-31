# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from spreadsheetconverter import Converter, YamlConfig


def test_convert():
    converter = Converter(YamlConfig.get_config('user/user.yaml'))
    converter.run()
