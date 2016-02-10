====================
SpreadsheetConverter
====================


.. image:: https://app.wercker.com/status/95671e377f8c3da730c70f0cddd119a2/m
   :alt: wercker status
   :target: https://app.wercker.com/project/bykey/95671e377f8c3da730c70f0cddd119a2


.. contents::
..

ExcelファイルやCVSなどの表を別の形式に変換するためのものです。
以下の特徴をもっています

- 変換ルールはyamlで定義可能
- 変換や出力のプラグインを書く事で独自フォーマットの出力が可能
- 別の変換ルールを用いて値の変換が可能


Requirements
------------

* Python:

  - CPython >= 2.7 or >= 3.3

Installation
------------

The last stable release is available on PyPI and can be installed with ``pip``::

    $ pip install SpreadsheetConverter


Example
-------

::

    $ cd sample
    $ ssconvert user/user.yaml --yaml_search_path yaml --xls_search_path xls --json_base_path json


Copyright
---------

- Copyright
  - Copyright (C) 2015 gumi Inc.
