# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from .base import BaseValueConverter
from six import text_type


class ValueConverter(BaseValueConverter):
    def to_python(self, value):
        return text_type(value)
