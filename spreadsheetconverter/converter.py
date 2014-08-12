# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
import datetime


class Converter(object):
    """
    変換
    """

    def __init__(self, config, quiet=False, indent=1):
        """
        :param quiet: 処理状況を出力しない
        :type quiet: bool
        """
        self.config = config
        self.quiet = quiet
        self.indent = indent

    def echo(self, message, start_at=None):
        if self.quiet:
            return

        text = '{}{} {}'.format('--' * self.indent, self.config.name, message)
        if start_at:
            delta = datetime.datetime.now() - start_at
            text += ' ({}.{}s)'.format(delta.seconds, delta.microseconds)

        print(text)

    def run(self):
        self.save(self.convert())

    def convert(self):
        """
        データの変換を行う
        :rtype: list of dict
        """
        if self.config.has_cache():
            self.echo('hit cache')
            return self.config.get_cache()

        self.echo('load sheet start')
        start_at = datetime.datetime.now()
        sheet = self.config.get_sheet()
        self.echo('load sheet end', start_at=start_at)

        self.echo('convert start')
        start_at = datetime.datetime.now()
        _data = self.config.convert(sheet)
        self.echo('convert end', start_at=start_at)
        return _data

    def save(self, data):
        self.echo('save start')
        start_at = datetime.datetime.now()
        self.config.save(data)
        self.echo('save end', start_at=start_at)
