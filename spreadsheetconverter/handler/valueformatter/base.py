

class BaseValueFormatter(object):
    def __init__(self, settings):
        self.settings = settings

    def format(self, value):
        return value
