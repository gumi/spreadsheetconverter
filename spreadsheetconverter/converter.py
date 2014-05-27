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
        :param quiet: 処理状況を出力しない
        :type quiet: bool
        """
        self.config = config
        self.quiet = quiet

    def echo(self, message, start_at=None):
        if self.quiet:
            return

        text = '--{} {}'.format(self.config.name, message)
        if start_at:
            delta = datetime.datetime.now() - start_at
            text += ' ({}.{}s)'.format(delta.seconds, delta.microseconds)

        print(text)

    def run(self):
        self.save(self.convert())

    def convert(self, target_fields=None):
        """
        データの変換を行う
        :type target_fields: list
        :rtype: list of dict
        """
        self.echo('load sheet start')
        start_at = datetime.datetime.now()
        sheet = self.config.get_sheet()
        self.echo('load sheet end', start_at=start_at)

        self.echo('convert start')
        start_at = datetime.datetime.now()
        _data = self.config.convert(sheet, target_fields=target_fields)
        self.echo('convert end', start_at=start_at)
        return _data

    def save(self, data):
        self.echo('save start')
        start_at = datetime.datetime.now()
        self.config.save(data)
        self.echo('save end', start_at=start_at)
