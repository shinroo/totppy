#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import click
import datetime
import pytest-cov

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
    --generator, -g         Create one time password with generator, prompts for inputs.
    --token, -t             Create one time password with token, prompts for inputs.
  Examples
    $ python totppy --help
    $ python totppy --version
    $ python totppy --generator
    $ python totppy --token
'''

totppy_version = __version__

@click.command(add_help_option=False)
@click.option('-h', '--help',
              is_flag=True,
              default=False,
              help='Display help message.')
@click.option('-v', '--version',
              is_flag=True,
              default=False,
              help='Display installed version.')
@click.option('-g', '--generator',
              is_flag=True,
              default=False,
              help='Create one time password with generator, prompts for inputs.')
@click.option('-t', '--token',
              is_flag=True,
              default=False,
              help='Create one time password with token, prompts for inputs.')


@pytest.marker.no_cover
def main(help, version, generator, token):
    if (help):
        print(help_message)
        sys.exit(0)
    else:
        if (version):
            print('totppy' +  ' ' + totppy_version)
        elif (generator):
            digits = click.prompt('Digits', type=int)
            period = click.prompt('Period', type=int)
            secret = click.prompt('Secret', type=str)
            factor = Factor(digits=digits, period=period)
            generator = Generator(factor, Algorithm.SHA1, secret)
            password = generator.password(datetime.datetime.now())
            print('One time password : ' + str(password))
        elif (token):
            digits = click.prompt('Digits', type=int)
            period = click.prompt('Period', type=int)
            secret = click.prompt('Secret', type=str)
            name = click.prompt('Name', type=str)
            issuer = click.prompt('Issuer', type=str)
            factor = Factor(digits=digits, period=period)
            generator = Generator(factor, Algorithm.SHA1, secret)
            token = Token(generator, name, issuer)
            password = token.password()
            print('One time password : ' + str(password))

if __name__ == '__main__':
    main()
