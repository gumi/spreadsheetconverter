# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import pytest
from spreadsheetconverter import Converter, YamlConfig
from spreadsheetconverter.exceptions import (
    TargetFieldDoesNotExistError,
    ForeignkeyTargetDataDoesNotExistError,
)


def test_convert():
    Converter(YamlConfig.get_config('dummy1.yaml')).run()
    Converter(YamlConfig.get_config('dummy2.yaml')).run()


def test_nothing_field_convert_error():
    with pytest.raises(TargetFieldDoesNotExistError):
        Converter(YamlConfig.get_config('nothing_field.yaml')).run()


def test_nothing_foreignkey_convert_error():
    with pytest.raises(ForeignkeyTargetDataDoesNotExistError):
        Converter(YamlConfig.get_config('nothing_foreignkey.yaml')).run()
