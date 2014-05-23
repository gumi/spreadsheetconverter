# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import importlib

try:
    from urllib.parse import urlparse
except ImportError:
    # Py2
    from urlparse import urlparse


def get_loader(uri):
    """
    :type uri: string
    :rtype: BaseLoader
    """
    parsed = urlparse(uri)

    loader_module = importlib.import_module(
        'spreadsheetconverter.loader.{}'.format(parsed.scheme))

    return loader_module.Loader(parsed)
