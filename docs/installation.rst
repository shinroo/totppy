Installation & Testing
----------------------

Installation
============

**From PyPI** ::

    $ pip install totppy

**From source**

Install dependencies using `pip`::

    $ pip install -r requirements.txt

Download the latest `totppy` library from: https://github.com/abdullahselek/totppy

Extract the source distribution and run::

    $ python setup.py build
    $ python setup.py install

Running Tests
=============

The test suite can be run against a single Python version which requires ``pip install pytest`` and optionally ``pip install pytest-cov`` (these are included if you have installed dependencies from ``requirements.testing.txt``)

To run the unit tests with a single Python version::

    $ py.test -v

to also run code coverage::

    $ py.test -v --cov-report html --cov=totppy

To run the unit tests against a set of Python versions::

    $ tox

Getting the code
================

The code is hosted at `Github <https://github.com/abdullahselek/totppy>`_.

Check out the latest development version anonymously with::

$ git clone https://github.com/abdullahselek/totppy.git
$ cd totppy
