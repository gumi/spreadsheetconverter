# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import six

from .base import BaseInspector


class Inspector(BaseInspector):
    def __init__(self, setting):
        super(Inspector, self).__init__(setting)

    def inspect(self, data):
        """
        :param data: row data
        """
        if data[self.target_fieldname] <= self.get_compare_value(data):
            return

        raise Exception('%s %s', self.target_fieldname, data)

    def get_compare_value(self, data):
        if isinstance(self.setting['value'], six.string_types):
            return self.setting['value'].format(**data)

        return self.setting['value']
