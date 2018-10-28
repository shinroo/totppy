#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .generator import Generator

"""A `Token` contains a password generator and information identifying the corresponding account.
"""
class Token(object):

    def __init__(self, generator, name = '', issuer = ''):
        """Returns a Token instance.
        Args:
          generator (Generator):
            The password generator.
          name (str):
            The account name for the token (defaults to '').
          issuer (str):
            The entity which issued the token (defaults to '').
        """

        self._name = name
        self._issuer = issuer
        self._generator = generator
