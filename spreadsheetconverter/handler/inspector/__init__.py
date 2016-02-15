# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from spreadsheetconverter.utils import load_module


def get_inspectors(settings):
    """
    :type settings: dict
    """
    if 'inspect' not in settings:
        return []

    inspectors = []
    for setting in settings['inspect']:
        loader_module = load_module('spreadsheetconverter.handler.inspector.{}',
                                    setting['type'])
        inspectors.append(loader_module.Inspector(setting))

    return inspectors
