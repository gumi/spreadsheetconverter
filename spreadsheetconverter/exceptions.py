# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals


class TargetFieldDoesNotExistError(Exception):
    pass


class ForeignkeyTargetDataDoesNotExistError(ValueError):
    pass
