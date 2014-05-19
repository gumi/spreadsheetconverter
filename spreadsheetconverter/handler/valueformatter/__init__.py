# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import importlib
from .through import ValueFormatter as DefaultValueFormatter


def get_value_formatter(setting):
    """
    :type setting: dict
    """
    try:
        loader_module = importlib.import_module(
            'spreadsheetconverter.valueformatter.{}'.format(setting['type']))
        return loader_module.ValueFormatter(setting)
    except ImportError:
        return DefaultValueFormatter(setting)
