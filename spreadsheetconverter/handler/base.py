from .valueformatter import get_value_formatter


class BaseHandler(object):
    def __init__(self, handler_config, config):
        self.handler_config = handler_config
        self._config = config

    def get_value_formatter(self, setting):
        return get_value_formatter(setting)
