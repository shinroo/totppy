#!/usr/bin/env python
# -*- coding: utf-8 -*-

import struct
import binascii
import datetime
import time

from pytotp import crypto
from .enums import (
    Error,
    Algorithm
)

"""A moving factor with which a generator produces different one-time passwords over time.
"""
class Factor(object):
    """The possible values are `digits` and `period`, with associated values for each."""

    def __init__(self, digits=6, period=30):
        """Returns a Factor instance.
        Args:
          digits (int):
            The number of digits in the password.
          period (int):
            Time period for password.
        """

        self._digits = digits
        self._period = period

"""A Generator contains all of the parameters needed to generate a one-time password.
"""
class Generator(object):

    def __init__(self, factor, algorithm, secret):
        """Returns a Generator instance.
        Args:
          factor (Factor):
            Contains digits and period.
          algorithm (Algorithm):
            Algorithm to be used to generate token.
          secret (bytes):
            The shared secret.
        """

        self._factor = factor
        self._algorithm = algorithm
        self._secret = secret
        assert self.__validate_factor(factor) == None, 'Invalid given factor'

    def __validate_factor(self, factor):
        if factor._period < 0:
            return Error.INVALID_PERIOD
        suitable_digits = [6, 7, 8]
        if factor._digits not in suitable_digits:
            return Error.INVALID_DIGITS
        return None

    """Returns a onetime use password.
    Args:
      date (datetime):
        The target time, represented as a `datetime`.
    Returns:
      The generated password.
    """
    def password(self, date):
        counter = int(time.mktime(date.timetuple()))
        # Ensure the counter value is big-endian
        big_counter_bytes = struct.pack(">I", counter)
        hash = crypto.HMAC(self._algorithm, self._secret, big_counter_bytes)
        offset = ord(hash[len(hash)-1]) & 0x0F
        truncated_hash = binascii.hexlify(hash[offset : offset+4].encode())
        password = int(truncated_hash, 32) % pow(10, self._factor._digits)
        return password
