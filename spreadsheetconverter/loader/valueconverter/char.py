# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from .base import BaseValueConverter
import six


class ValueConverter(BaseValueConverter):
    def to_python(self, value):
        if isinstance(value, six.string_types) \
                and self._has_default \
                and not value:
            return self.get_default()

        return six.text_type(value)
