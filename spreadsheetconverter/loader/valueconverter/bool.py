from .base import BaseValueConverter


class ValueConverter(BaseValueConverter):
    def _to_python(self, value):
        if isinstance(value, str) and not value:
            return self.get_default()

        return bool(float(value))
