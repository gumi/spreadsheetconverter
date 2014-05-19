# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals


class BaseValueConverter(object):
    def __init__(self, settings):
        self.settings = settings

    def to_python(self, value):
        return value

    @property
    def fieldname(self):
        return self.settings['column']
