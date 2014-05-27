# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from spreadsheetconverter.utils import load_module


def get_validators(setting):
    """
    :type setting: dict
    """
    if 'validate' not in setting:
        return []

    validators = []
    for validator_name in setting['validate'].keys():
        loader_module = load_module(
            'spreadsheetconverter.loader.validator.{}',
            validator_name)
        validators.append(loader_module.Validator(setting))

    return validators
