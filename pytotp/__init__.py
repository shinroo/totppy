#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A Python library for generating TOTP and HOTP one-time passwords."""

from __future__ import absolute_import

__author__       = 'Abdullah Selek'
__email__        = 'abdullahselek@gmail.com'
__copyright__    = 'Copyright (c) 2018 Abdullah Selek'
__license__      = 'MIT License'
__version__      = '0.1'
__url__          = 'https://github.com/abdullahselek/pytotp'
__download_url__ = 'https://github.com/abdullahselek/pytotp'
__description__  = 'A Python library for generating TOTP and HOTP one-time passwords.'

from .generator import (
    Algorithm,
    Error,
    Factor
)
from pytotp import crypto
from pytotp import base32helper
