# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from .base import BaseValidator


class Validator(BaseValidator):
    def __init__(self, settings):
        super(Validator, self).__init__(settings)
        self._data = set()

    def validate(self, value):
        if value in self._data:
            raise ValueError('Duplicate value {}: {}'.format(
                self.fieldname, value))

        self._data.add(value)
