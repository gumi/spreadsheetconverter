from spreadsheetconverter.utils import load_module


def get_value_converter(setting, **kwargs):
    """
    :type setting: dict
    """
    loader_module = load_module('spreadsheetconverter.loader.valueconverter.{}',
                                setting['type'])

    return loader_module.ValueConverter(setting, **kwargs)
