from spreadsheetconverter.utils import load_module


def get_handler(setting, config):
    """
    :type setting: dict
    :type config: Config
    """
    loader_module = load_module('spreadsheetconverter.handler.{}',
                                setting['type'])

    return loader_module.Handler(setting, config)
