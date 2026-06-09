from .base import BaseValueConverter


class ValueConverter(BaseValueConverter):
    def to_python(self, value):
        if isinstance(value, str) \
                and self._has_default \
                and not value:
            return self.get_default()

        return str(value)
