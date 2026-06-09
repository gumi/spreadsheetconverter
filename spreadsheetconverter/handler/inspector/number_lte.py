
from .base import BaseCompareNumberInspector


class Inspector(BaseCompareNumberInspector):
    def inspect(self, data):
        """
        :param data: row data
        """
        if data[self.target_fieldname] <= self.get_compare_value(data):
            return

        raise Exception('%s %s', self.target_fieldname, data)
