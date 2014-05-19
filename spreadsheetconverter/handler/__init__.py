# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import importlib


def get_handler(setting):
    """
    :type setting: dict
    """
    loader_module = importlib.import_module(
        'spreadsheetconverter.handler.{}'.format(setting['type']))
    return loader_module.Handler(setting)
