# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import importlib


def get_value_converter(setting):
    """
    :type setting: dict
    """
    loader_module = importlib.import_module(
        'spreadsheetconverter.loader.valueconverter.{}'.format(setting['type']))
    return loader_module.ValueConverter(setting)
