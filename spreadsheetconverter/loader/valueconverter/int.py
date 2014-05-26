# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from .base import BaseValueConverter


class ValueConverter(BaseValueConverter):
    def _to_python(self, value):
        return int(value)
