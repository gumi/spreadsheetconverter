# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import os

from dateutil.parser import parse
import pytz

from .base import BaseValueConverter


class ValueConverter(BaseValueConverter):
    def __init__(self, settings, **kwargs):
        super(ValueConverter, self).__init__(settings, **kwargs)

        self._timezone = None
        _default_timezone = os.environ.get('SSC_TIMEZONE')
        if _default_timezone:
            self._timezone = pytz.timezone(_default_timezone)
        _settings_timezone = settings.get('timezone')
        if _settings_timezone:
            self._timezone = pytz.timezone(_default_timezone)

    def _to_python(self, value):
        if not value:
            raise ValueError

        return self._localize(parse(value))

    def _localize(self, value):
        if self._timezone and not value.tzinfo:
            return self._timezone.localize(value)

        return value
