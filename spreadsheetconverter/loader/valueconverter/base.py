# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals


class BaseValueConverter(object):
    def __init__(self, settings, config=None):
        """
        :type settings: dict
        :type config: Config
        """
        self.settings = settings
        self._config = config
        self._has_default = 'default' in settings
        self._default = settings.get('default')

    def to_python(self, value):
        try:
            return self._to_python(value)
        except ValueError:
            if not value:
                return self.get_default()
            raise

    def _to_python(self, value):
        return value

    def get_default(self):
        if self._has_default:
            return self._default

        raise ValueError('nothing default {}'.format(self.fieldname))

    @property
    def fieldname(self):
        return self.settings['column']
