# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from .base import BaseValueConverter


class ValueConverter(BaseValueConverter):
    def __init__(self, settings):
        super(ValueConverter, self).__init__(settings)
        self._relation_data = {}
        self._converter = None
        self._value_converter = None

    def _to_python(self, value):
        converted = self.value_converter.to_python(value)
        if converted not in self.relation:
            raise ValueError

        return self.relation[converted]

    @property
    def value_converter(self):
        if self._value_converter:
            return self._value_converter

        self._value_converter = self.converter.config.get_converter_by_column(
            self.relation_field_from)
        return self._value_converter

    @property
    def converter(self):
        if self._converter:
            return self._converter

        from spreadsheetconverter import Converter
        self._converter = Converter(self.settings['relation']['from'])
        return self._converter

    @property
    def relation(self):
        """
        変換表データ
        :rtype: dict
        """
        if self._relation_data:
            return self._relation_data

        for entity in self.converter.convert(target_fields=[
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
