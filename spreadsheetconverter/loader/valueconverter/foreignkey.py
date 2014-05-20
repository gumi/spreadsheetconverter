# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from .base import BaseValueConverter


class ValueConverter(BaseValueConverter):
    def __init__(self, settings):
        super(ValueConverter, self).__init__(settings)
        self._relation_data = {}

    def to_python(self, value):
        return self.relation[value]

    @property
    def relation(self):
        """
        変換表データ
        :rtype: dict
        """
        if self._relation_data:
            return self._relation_data

        from spreadsheetconverter import Converter
        converter = Converter(self.settings['relation']['from'])
        for entity in converter.convert(target_fields=[
            self.relation_field_to,
            self.relation_field_from,
        ]):
            from_value = entity[self.relation_field_from]
            to_value = entity[self.relation_field_to]
            self._relation_data[from_value] = to_value

        return self._relation_data

    @property
    def relation_field_to(self):
        return self.settings['relation']['column']

    @property
    def relation_field_from(self):
        return self.settings['relation']['key']
