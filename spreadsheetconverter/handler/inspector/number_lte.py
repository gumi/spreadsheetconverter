# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from .base import BaseInspector


class Inspector(BaseInspector):
    def __init__(self, settings):
        super(Inspector, self).__init__(settings)

    def inspect(self, data):
        """
        :param data: row data
        """
        if data[self.target_fieldname] <= self.get_compare_value(data):
            return

        raise Exception('%s %s', self.target_fieldname, data)

    def get_compare_value(self, data):
        return self.settings['value'].format(**data)
