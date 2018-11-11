#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import click

from totppy import (
    __version__,
    Factor,
    Generator,
    Algorithm,
    Token
)

help_message = '''
  A Python library for generating TOTP and HOTP one-time passwords.
  Usage
    $ python totppy [<options>]
  Options
    --help, -h              Display help message
    --version, -v           Display installed version
    --generator, -g         Create one time password with generator.
    --token, -t             Create one time password with token.
  Examples
    $ python spampy --help
    $ python spampy --version
    $ python spampy --generator
    $ python spampy --token
'''

spampy_version = __version__
