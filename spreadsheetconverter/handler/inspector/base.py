class BaseInspector(object):
    def __init__(self, setting):
        self.setting = setting

    def inspect(self, data):
        raise NotImplementedError

    @property
    def target_fieldname(self):
        return self.setting['column']


class BaseCompareNumberInspector(BaseInspector):
    def get_compare_value(self, data):
        return self._get_formula_result(self.setting['value'], data)

    def _get_formula_result(self, formula, data):
        if isinstance(formula, str):
            return eval(formula.format(**data))

        return formula
