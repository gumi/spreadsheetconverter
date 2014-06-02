# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import six
from .base import BaseValueConverter


class ValueConverter(BaseValueConverter):
    def _to_python(self, value):
        if isinstance(value, six.string_types) and not value:
            return self.get_default()

        return bool(float(value))
