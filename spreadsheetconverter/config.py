# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import codecs
from collections import defaultdict

import six
import yaml

from .loader import get_loader
from .handler import get_handler
from .exceptions import TargetFieldDoesNotExistError
from .utils import search_path


class Config(object):
    def __init__(self, rules):
        self.rules = rules
        self._fields = {
            field['name']: field for field in self.rules['fields']
        }
        self._fields_column = {
            field['column']: field for field in self.rules['fields']
        }
        self._loader = None
        self._handler = None

        self._formatter = {}
        self._converter = {}
        self._validator = defaultdict(dict)

        self._column_name_index_map = {}

        self.name = self.rules['target']

    @property
    def loader(self):
        if self._loader:
            return self._loader

        self._loader = get_loader(self.rules['target'])
        return self._loader

    @property
    def handler(self):
        if self._handler:
            return self._handler

        self._handler = get_handler(self.rules['handler'], self)
        return self._handler

    @property
    def header_row_index(self):
        """
        カラム名のはいっている行
        :rtype: int
        """
        return self.rules.get('row', 1) - 1

    @property
    def data_start_row_index(self):
        """
        データのはいっている開始行
        :rtype: int
        """
        return self.header_row_index + 1

    @property
    def limit(self):
        """
        変換の最大数
        :rtype: int
        """
        if 'limit' in self.rules:
            return self.rules['limit']

        return None

    def get_converter(self, item):
        if item not in self._fields:
            return None

        if item in self._converter:
            return self._converter[item]

        converter = self.loader.get_value_converter(self._fields[item])
        self._converter[item] = converter
        return converter

    def get_converter_by_column(self, item):
        return self.get_converter(self._fields_column[item]['name'])

    def get_formatter(self, item):
        if item in self._formatter:
            return self._formatter[item]

        formatter = self.handler.get_value_formatter(self._fields_column[item])
        self._formatter[item] = formatter
        return formatter

    def get_validators(self, item, target_fields=None):
        target_field_key = self._get_cache_key(target_fields)
        if item in self._validator[target_field_key]:
            return self._validator[target_field_key][item]

        validators = self.loader.get_validators(self._fields_column[item])
        self._validator[target_field_key][item] = validators
        return validators

    def get_sheet(self):
        return self.loader.sheet

    def save(self, data):
        for entity in data:
            for key, value in entity.items():
                formatter = self.get_formatter(key)
                if not formatter:
                    continue

                entity[key] = formatter.format(value)

        self.handler.save(data)

    def convert(self, sheet, target_fields=None):
        _data = []
        # 処理行数
        count = 0
        for i, row in enumerate(sheet.rows):
            if i == self.header_row_index:
                # タイトル行
                self.load_header_row(row)
                self.check_header_row()
                continue

            if i < self.data_start_row_index:
                continue

            _data.append(self.convert_column(row, target_fields=target_fields))

            # 処理行数
            count += 1
            if self.limit and count >= self.limit:
                break

        return _data

    def convert_column(self, row, target_fields=None):
        result = {}
        for i, value in enumerate(row):
            converter = self.get_converter(
                self._column_name_index_map[i])
            if not converter:
                continue

            if target_fields and converter.fieldname not in target_fields:
                # 変換対象指定がある場合で対象外
                continue

            # convert
            converted = converter.to_python(value)
            result[converter.fieldname] = converted

            # validate
            validators = self.get_validators(converter.fieldname,
                                             target_fields=target_fields)
            for validator in validators:
                validator.validate(converted)

        return result

    def load_header_row(self, row):
        for i, name in enumerate(row):
            self._column_name_index_map[i] = name

    def check_header_row(self):
        field_names = set(self._column_name_index_map.values())
        target_field_names = set(self._fields.keys())
        if not (target_field_names <= field_names):
            raise TargetFieldDoesNotExistError('{}: nothing fields: {}'.format(
                self.name,
                ', '.join(target_field_names - field_names),
            ))

    def _get_cache_key(self, target_fields):
        if target_fields is None:
            return 'None'
        return ':'.join(sorted(target_fields))

    def has_cache(self, target_fields=None):
        return False

    def get_cache(self, target_fields=None):
        raise NotImplementedError


YAML_CACHE = {}


class YamlConfig(Config):
    def __init__(self, yaml_path, load_context=None):
        if load_context is None:
            load_context = {}
        load_context[yaml_path] = self

        abs_yaml_path = search_path(
            yaml_path,
            path_env='SSC_YAML_SEARCH_PATH',
            recursive_env='SSC_YAML_SEARCH_RECURSIVE')
        f = codecs.open(abs_yaml_path, 'r', 'utf8').read()
        rules = yaml.load(f)

        # relation指定のfromを再読み込み
        for entity in rules['fields']:
            if 'relation' in entity:
                if isinstance(entity['relation']['from'], six.string_types):
                    related_path = entity['relation']['from']
                    if related_path not in load_context:
                        entity['relation']['from'] = YamlConfig.get_config(
                            related_path,
                            load_context=load_context)
                    else:
                        entity['relation']['from'] = load_context[related_path]

        super(YamlConfig, self).__init__(rules)

        self.name = yaml_path
        self._converted = {}

    @classmethod
    def get_config(cls, yaml_path, **kwargs):
        if yaml_path in YAML_CACHE:
            return YAML_CACHE[yaml_path]

        YAML_CACHE[yaml_path] = cls(yaml_path, **kwargs)
        return YAML_CACHE[yaml_path]

    def convert(self, sheet, target_fields=None):
        _result = super(YamlConfig, self).convert(
            sheet, target_fields=target_fields)
        self._set_cache(target_fields, _result)
        return _result

    def _get_cache_key(self, target_fields):
        if target_fields is None:
            return 'None'
        return ':'.join(sorted(target_fields))

    def has_cache(self, target_fields=None):
        return self._get_cache_key(target_fields) in self._converted

    def get_cache(self, target_fields=None):
        return self._converted[self._get_cache_key(target_fields)]

    def _set_cache(self, target_fields, data):
        self._converted[self._get_cache_key(target_fields)] = data
