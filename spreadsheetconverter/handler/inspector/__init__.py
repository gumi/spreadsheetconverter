# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from spreadsheetconverter.utils import load_module


def get_inspectors(setting):
    """
    :type setting: dict
    """
    if 'inspect' not in setting:
        return []

    inspectors = []
    for inspector_name in setting['inspect'].keys():
        loader_module = load_module(
            'spreadsheetconverter.loader.inspector.{}',
            inspector_name)
        inspectors.append(loader_module.Inspector(setting))

    return inspectors
