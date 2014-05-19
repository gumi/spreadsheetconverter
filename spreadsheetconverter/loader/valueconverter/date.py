# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from datetime import datetime
from .base import BaseValueConverter


class ValueConverter(BaseValueConverter):
    def to_python(self, value):
        try:
            _datetime = datetime.strptime(value, '%Y/%m/%d')
        except ValueError:
            _datetime = datetime.strptime(value, '%Y/%m/%d %H:%M:%S')

        return _datetime.date()
