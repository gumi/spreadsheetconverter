# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals


class BaseInspector(object):
    def __init__(self, settings):
        self.settings = settings

    def inspect(self, data):
        raise NotImplementedError

    @property
    def target_fieldname(self):
        return self.settings['column']
