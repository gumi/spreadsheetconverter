from datetime import datetime
from .base import BaseValueConverter


class ValueConverter(BaseValueConverter):
    def _to_python(self, value):
        try:
            return datetime.strptime(value, '%Y/%m/%d').date()
        except ValueError:
            return datetime.strptime(value, '%Y/%m/%d %H:%M:%S').date()
