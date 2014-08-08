# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import importlib
import os
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


def search_path(filename, path_env=None, recursive_env=None):
    """
    ファイル名を検索対象ディレクトリから検索

    :param filename: 対象ファイル名(パスの場合あり)
    :param path_env: 検索対象パスのはいった環境変数名
    :param recursive_env: 検索対象を再起検索するかが入った環境変数名
    """
    search_paths = []
    if path_env:
        search_path_env = os.environ.get(path_env)
        if search_path_env:
            search_paths += search_path_env.split(':')

    search_path_env = os.environ.get('SSC_SEARCH_PATH')
    if search_path_env:
        search_paths += search_path_env.split(':')

    if not search_paths:
        search_paths.append(os.getcwd())

    recursive = bool(int(os.environ.get(recursive_env, False)))

    def _search_file(_path):
        abs_path = os.path.join(_path, filename)
        if os.path.exists(abs_path):
            return abs_path

        if not recursive:
            return

        for name in os.listdir(_path):
            path = os.path.join(_path, name)
            if os.path.isdir(path):
                result = _search_file(path)
                if result:
                    return result

    for search_path in search_paths:
        path = _search_file(search_path)
        if path:
            return path

    raise IOError('File does not exist.', filename, search_paths, recursive)
