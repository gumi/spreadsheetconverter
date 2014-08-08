# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from collections import namedtuple
import importlib

try:
    from urllib.parse import urlparse
except ImportError:
    # Py2
    from urlparse import urlparse


class LoaderParams(namedtuple('LoaderParams',
                              'scheme netloc path query fragment')):
    pass


def get_loader(uri):
    """
    :type uri: string
    :rtype: BaseLoader
    """
    parsed = urlparse(uri)
    if not parsed.fragment and '#' in parsed.path:
        # failed fragment parse
        path, fragment = parsed.path.split('#')
        parsed = LoaderParams(
            parsed.scheme, parsed.netloc, path, parsed.query, fragment
        )

    loader_module = importlib.import_module(
        'spreadsheetconverter.loader.{}'.format(parsed.scheme))

    return loader_module.Loader(parsed)
