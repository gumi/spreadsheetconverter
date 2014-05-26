# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals


class BaseValidator(object):
    def __init__(self, settings):
        self.settings = settings

    def validate(self, value):
        raise NotImplementedError

    @property
    def fieldname(self):
        return self.settings['column']
