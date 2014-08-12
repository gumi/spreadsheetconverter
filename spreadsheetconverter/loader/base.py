# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from .valueconverter import get_value_converter
from .validator import get_validators


class BaseLoader(object):
    def __init__(self, params):
        self._params = params

    @property
    def sheet(self):
        return self.get_book().get_sheet(self._params.fragment)

    def get_book(self):
        raise NotImplementedError

    def get_sheet(self, name):
        raise NotImplementedError

    def get_value_converter(self, setting, **kwargs):
        return get_value_converter(setting, **kwargs)

    def get_validators(self, setting):
        return get_validators(setting)


class BaseBook(object):
    @property
    def sheets(self):
        yield BaseSheet()

    def get_sheet(self, name):
        yield BaseSheet()


class BaseSheet(object):
    def __init__(self):
        pass

    @property
    def rows(self):
        raise NotImplementedError
