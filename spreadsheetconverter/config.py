# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from .loader import get_loader
from .handler import get_handler


class Config(object):
    def __init__(self, rules):
        self.rules = rules
        self._fields = {
            field['name']: field for field in self.rules['fields']
        }
        self.loader = get_loader(self.rules['target'])
        self.handler = get_handler(self.rules['handler'])

        self._formatter = {}
        self._converter = {}

    @property
    def header_row_index(self):
        """
        カラム名のはいっている行
        :rtype: int
        """
        return self.rules.get('row', 1) - 1

    @property
    def data_start_row_index(self):
        """
        データのはいっている開始行
        :rtype: int
        """
        return self.header_row_index + 1

    def get_converter(self, item):
        if item not in self._fields:
            return None

        if item in self._converter:
            return self._converter[item]

        converter = self.loader.get_value_converter(self._fields[item])
        self._converter[item] = converter
        return converter

    def get_formatter(self, item):
        if item in self._formatter:
            return self._formatter[item]

        formatter = self.handler.get_value_formatter(self._fields[item])
        self._formatter[item] = formatter
        return formatter

    def get_sheet(self):
        return self.loader.sheet
