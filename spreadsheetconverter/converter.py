# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals


class Converter(object):
    """
    変換
    """

    def __init__(self, config):
        """
        :type config: Config
        """
        self.config = config

        self._data = []
        self._column_name_index_map = {}

    def run(self):
        sheet = self.config.get_sheet()

        for i, row in enumerate(sheet.rows):
            if i == self.config.header_row_index:
                # タイトル行
                self.load_header_row(row)
                continue

            if i < self.config.data_start_row_index:
                continue

            self._data.append(self.convert_column(row))

        self.config.handler.save(self._data)

    def convert_column(self, row):
        result = {}
        for i, value in enumerate(row):
            value_converter = self.config.get_converter(
                self._column_name_index_map[i])
            if not value_converter:
                continue

            value = value_converter.to_python(value)

            value_formatter = self.config.get_formatter(
                self._column_name_index_map[i])

            result[value_converter.fieldname] = value_formatter.format(value)

        return result

    def load_header_row(self, row):
        print(row)
        for i, name in enumerate(row):
            self._column_name_index_map[i] = name
