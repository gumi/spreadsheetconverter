# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals


class BaseValueFormatter(object):
    def __init__(self, settings):
        self.settings = settings

    def format(self, value):
        return value
