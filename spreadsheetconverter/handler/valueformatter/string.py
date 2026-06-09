from .base import BaseValueFormatter


class ValueFormatter(BaseValueFormatter):
    def format(self, value):
        return str(value)
