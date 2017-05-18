========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/carton-db.py/badge/?style=flat
    :target: https://readthedocs.org/projects/carton-dbpy
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/stevecj/carton-db.py.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/stevecj/carton-db.py

.. |requires| image:: https://requires.io/github/stevecj/carton-db.py/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/stevecj/carton-db.py/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/stevecj/carton-db.py/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/stevecj/carton-db.py

.. |version| image:: https://img.shields.io/pypi/v/cartondb.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/cartondb

.. |commits-since| image:: https://img.shields.io/github/commits-since/stevecj/carton-db.py/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/stevecj/carton-db.py/compare/v0.0.1...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/cartondb.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/cartondb

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/cartondb.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/cartondb

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/cartondb.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/cartondb


.. end-badges

A pure Python key/value data storage system where the values may consist of
simple data structures

* Free software: BSD license

This will be the Python implementation of Carton DB which currently has only
a Ruby implementation. For details, see https://github.com/stevecj/carton_db.rb.

Project Status: Initial Development
===================================

This is a brand new package project and does not yet actually do anything,
nor has it been released to PyPI so the installation instructions below do
not yet work.



Installation
============

::

    pip install cartondb

Documentation
=============

https://carton-dbpy.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
