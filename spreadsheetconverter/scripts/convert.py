# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import os
import argparse
import sys
import textwrap

from spreadsheetconverter import Converter, YamlConfig


def main(argv=sys.argv, quiet=False):
    command = ConvertCommand(argv, quiet)
    return command.run()


class ConvertCommand(object):
    description = """\
    指定yamlで変換を実行します
    """
    parser = argparse.ArgumentParser(
        description=textwrap.dedent(description)
    )
    parser.add_argument('config',  nargs='+', help='convert target yaml paths')

    parser.add_argument('--search_path', nargs='+',
                        help='file search paths')

    parser.add_argument('--yaml_search_path', nargs='+',
                        help='yaml file search paths')
    parser.add_argument('--yaml_search_recursive', type=bool,
                        help='yaml file search recursive')

    parser.add_argument('--xls_search_path', nargs='+',
                        help='xls file search paths')
    parser.add_argument('--xls_search_recursive', type=bool,
                        help='xls file search recursive')

    parser.add_argument('--json_base_path',
                        help='json file out path')

    parser.add_argument('--timezone',
                        help='default timezone')

    def __init__(self, argv, quiet=False):
        self.quiet = quiet
        self.args = self.parser.parse_args(argv[1:])

    def out(self, msg):  # pragma: no cover
        if not self.quiet:
            print(msg)

    def run(self, shell=None):
        if not self.args:
            self.out('Requires a config file argument')
            return 2
        print(self.args)

        if self.args.search_path:
            os.environ.setdefault('SSC_SEARCH_PATH',
                                  ':'.join(self.args.search_path))

        if self.args.yaml_search_path:
            os.environ.setdefault(
                'SSC_YAML_SEARCH_PATH',
                ':'.join(self.args.yaml_search_path))
        if self.args.yaml_search_recursive is not None:
            os.environ.setdefault(
                'SSC_YAML_SEARCH_RECURSIVE',
                '1' if self.args.yaml_search_recursive else '0')

        if self.args.xls_search_path:
            os.environ.setdefault(
                'SSC_XLS_SEARCH_PATH',
                ':'.join(self.args.xls_search_path))
        if self.args.xls_search_recursive is not None:
            os.environ.setdefault(
                'SSC_XLS_SEARCH_RECURSIVE',
                '1' if self.args.xls_search_recursive else '0')

        if self.args.json_base_path:
            os.environ.setdefault('SSC_JSON_BASE_PATH',
                                  self.args.json_base_path)

        if self.args.timezone:
            os.environ.setdefault('SSC_TIMEZONE',
                                  self.args.timezone)

        for config in self.args.config:
            converter = Converter(YamlConfig.get_config(config))
            converter.run()


if __name__ == '__main__':  # pragma: no cover
    sys.exit(main() or 0)
