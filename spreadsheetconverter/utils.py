# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import importlib
import re


def load_module(base_path_format, module):
    """
    path.to.module のような形式であればそのままimportし
    それ以外は base_path_format に埋め込んでからimportする

    :param base_path_format:
    :param module:
    """
    if re.match(r'[\w\-_]+\.[\w.\-]+[\w]$', module):
        return importlib.import_module(module)

    return importlib.import_module(base_path_format.format(module))
