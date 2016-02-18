# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from spreadsheetconverter.utils import load_module


def get_inspectors(settings, target_fields):
    """
    :type settings: dict
    :type target_fields: list of string
    """
    if 'inspect' not in settings:
        return []

    inspectors = []
    for setting in settings['inspect']:
        if target_fields and setting['column'] not in target_fields:
            continue

        loader_module = load_module('spreadsheetconverter.handler.inspector.{}',
                                    setting['type'])
        inspectors.append(loader_module.Inspector(setting))

    return inspectors
