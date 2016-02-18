# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from .base import BaseCompareNumberInspector


class Inspector(BaseCompareNumberInspector):
    def inspect(self, data):
        """
        :param data: row data
        """
        max_value = self._get_formula_result(self.setting['max'], data)
        min_value = self._get_formula_result(self.setting['min'], data)
        if min_value <= data[self.target_fieldname] <= max_value:
            return

        raise Exception('%s %s', self.target_fieldname, data)
