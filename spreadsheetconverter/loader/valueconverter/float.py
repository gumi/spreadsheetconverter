from .base import BaseValueConverter


class ValueConverter(BaseValueConverter):
    def _to_python(self, value):
        return float(value)
