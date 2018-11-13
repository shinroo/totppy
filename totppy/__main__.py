#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import click
import datetime

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
    $ python totppy --help
    $ python totppy --version
    $ python totppy --generator 6 15 'secret'
    $ python totppy --token 6 15 'secret' 'name' 'issuer'
'''

totppy_version = __version__

@click.command(add_help_option=False)
@click.option('-h', '--help', is_flag=True, default=False, help='Display help message.')
@click.option('-v', '--version', is_flag=True, default=False, help='Display installed version.')
@click.option('-g', '--generator',
              help='Create one time password with generator.',
              type=(int, int, str))
@click.option('-t', '--token',
              is_flag=True,
              default=False,
              help='Create one time password with token.',
              type=(int, int, str, str, str))

def main(help, version, generator, token):
    if (help):
        print(help_message)
        sys.exit(0)
    else:
        if (version):
            print('totppy' +  ' ' + totppy_version)
        elif (generator):
            (digits, period, secret) = generator
            factor = Factor(digits=digits, period=period)
            generator = Generator(factor, Algorithm.SHA1, secret)
            password = generator.password(datetime.datetime.now())
            print('One time password : ' + str(password))

if __name__ == '__main__':
    main()
