# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from .base import BaseValueFormatter
from six import text_type


class ValueFormatter(BaseValueFormatter):
    def format(self, value):
        return text_type(value)
