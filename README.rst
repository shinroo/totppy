totppy
======

.. image:: https://codecov.io/gh/abdullahselek/totppy/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/abdullahselek/totppy

+-------------------------------------------------------------------------+----------------------------------------------------------------------------------+
|                                Linux                                    |                                       Windows                                    |
+=========================================================================+==================================================================================+
| .. image:: https://travis-ci.org/abdullahselek/totppy.svg?branch=master | .. image:: https://ci.appveyor.com/api/projects/status/3o0k8ppg8tn0htmx?svg=true |
|   :target: https://travis-ci.org/abdullahselek/totppy                   |    :target: https://ci.appveyor.com/project/abdullahselek/totppy                 |
+-------------------------------------------------------------------------+----------------------------------------------------------------------------------+

Introduction
============

A Python library for generating TOTP and HOTP one-time passwords. It works with Python versions from 2.7+ and Python 3.

Installing
==========

You can install totppy using::

    $ pip install totppy

Getting the code
================

The code is hosted at https://github.com/abdullahselek/totppy

Check out the latest development version anonymously with::

    $ git clone git://github.com/abdullahselek/totppy.git
    $ cd totppy

To install test dependencies, run either::

    $ pip install -Ur requirements.testing.txt

Running Tests
=============

The test suite can be run against a single Python version which requires ``pip install pytest`` and optionally ``pip install pytest-cov`` (these are included if you have installed dependencies from ``requirements.testing.txt``)

To run the unit tests with a single Python version::

    $ py.test -v

to also run code coverage::

    $ py.test --cov=totppy

To run the unit tests against a set of Python versions::

    $ tox

Sample Usage
============

Imports::

    from totppy import (
        Factor,
        Generator,
        Algorithm
    )

Creating time based one time password::

    factor = Factor(digits=6, period=15)
    generator = Generator(factor, Algorithm.SHA1, 'secret')
    password = generator.password(datetime.datetime(2018, 10, 31, 9, 20))

or::

    from totppy import (
        Factor,
        Generator,
        Algorithm,
        Token
    )

    factor = Factor(6, 10)
    generator = Generator(factor, Algorithm.SHA1, 'secret')
    token = Token(generator, 'name', 'issuer')
    password = token.password()

Relevant RFCs
-------------

| `RFC4226 <https://tools.ietf.org/html/rfc4226>`_
| `RFC6238 <https://tools.ietf.org/html/rfc6238>`_

License
-------

MIT License

Copyright (c) 2018 Abdullah Selek

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
