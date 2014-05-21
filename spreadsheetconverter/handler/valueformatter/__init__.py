# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from spreadsheetconverter.utils import load_module


def get_value_formatter(setting):
    """
    :type setting: dict
    """
    try:
        loader_module = load_module(
            'spreadsheetconverter.handler.valueformatter.{}',
            setting['type'])
        return loader_module.ValueFormatter(setting)

    except ImportError:
        return None
