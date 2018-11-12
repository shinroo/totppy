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

@click.command(add_help_option=False)
@click.option('-h', '--help', is_flag=True, default=False, help='Display help message.')
@click.option('-v', '--version', is_flag=True, default=False, help='Display installed version.')
@click.option('-g', '--generator', 
              is_flag=True,
              default=False,
              help='Create one time password with generator.',
              type=(int, int, str))
@click.option('-t', '--token',
              is_flag=True,
              default=False,
              help='Create one time password with token.',
              type=(int, int, str, str, str))
