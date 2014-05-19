# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import json
from .base import BaseHandler
from .valueformatter.string import ValueFormatter as StringValueFormatter


class Handler(BaseHandler):
    def save(self, data):
        with open(self._config['path'], 'w') as f:
            f.write(json.dumps(data))

    def get_value_formatter(self, setting):
        if setting['type'] == 'datetime':
            return StringValueFormatter(setting)

        return super(Handler, self).get_value_formatter(setting)
