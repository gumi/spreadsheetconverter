

class BaseValidator(object):
    def __init__(self, settings):
        self.settings = settings

    def validate(self, value):
        raise NotImplementedError

    @property
    def fieldname(self):
        return self.settings['column']
