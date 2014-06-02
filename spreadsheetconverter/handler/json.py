# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import datetime
import json
import os

from six import text_type

from .base import BaseHandler
from .valueformatter.base import BaseValueFormatter


class DatetimeValueFormatter(BaseValueFormatter):
    def format(self, value):
        if isinstance(value, datetime.datetime):
            return text_type(value)

        return value


class Handler(BaseHandler):
    def save(self, data):
        path = self.handler_config['path']
        base_path = os.environ.get('SSC_JSON_BASE_PATH')
        if base_path:
            path = os.path.join(base_path, path)

        # 親までのディレクトリが存在しなければ作成
        _path, _filename = os.path.split(path)
        if not os.path.exists(_path):
            os.makedirs(_path)

        with open(path, 'w') as f:
            indent = self.handler_config.get('indent')
            sort_keys = self.handler_config.get('sort_keys', False)
            f.write(json.dumps(data, indent=indent, sort_keys=sort_keys))

    def get_value_formatter(self, setting):
        if setting['type'] == 'datetime':
            return DatetimeValueFormatter(setting)

        return super(Handler, self).get_value_formatter(setting)
