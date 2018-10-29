#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

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

    def password(self):
        """Calculates the current password based on the token's generator. The password generated will
        be consistent for a counter-based token, but for a timer-based token the password will
        depend on the current time when this property is accessed.
        Returns:
          The current password.
        """

        return self._generator.password(datetime.datetime.now())
