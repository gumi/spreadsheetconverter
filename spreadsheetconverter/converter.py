# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import datetime


class Converter(object):
    """
    変換
    """

    def __init__(self, config, quiet=False):
        """
        :type config: Config
        :param quiet: 処理状況を出力しない
        :type quiet: bool
        """
        self.config = config
        self.quiet = quiet

        self._column_name_index_map = {}

    def echo(self, message, start_at=None):
        if self.quiet:
            return

        text = '-- {}'.format(message)
        if start_at:
            delta = datetime.datetime.now() - start_at
            text += ' ({}.{}s)'.format(delta.seconds, delta.microseconds)

        print(text)

    def run(self):
        self.save(self.convert())

    def convert(self):
        self.echo('load sheet start')
        start_at = datetime.datetime.now()
        sheet = self.config.get_sheet()
        self.echo('load sheet end', start_at=start_at)

        self.echo('convert start')
        start_at = datetime.datetime.now()
        # 変換済みデータ
        _data = []
        # 処理行数
        count = 0
        for i, row in enumerate(sheet.rows):
            if i == self.config.header_row_index:
                # タイトル行
                self.load_header_row(row)
                continue

            if i < self.config.data_start_row_index:
                continue

            _data.append(self.convert_column(row))

            # 処理行数
            count += 1
            if self.config.limit and count >= self.config.limit:
                break

        self.echo('convert end', start_at=start_at)
        return _data

    def save(self, data):
        self.echo('save start')
        start_at = datetime.datetime.now()
        self.config.save(data)
        self.echo('save end', start_at=start_at)

    def convert_column(self, row):
        result = {}
        for i, value in enumerate(row):
            converter = self.config.get_converter(
                self._column_name_index_map[i])
            if not converter:
                continue

            result[converter.fieldname] = converter.to_python(value)

        return result

    def load_header_row(self, row):
        for i, name in enumerate(row):
            self._column_name_index_map[i] = name
