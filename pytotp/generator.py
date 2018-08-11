#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum

"""A cryptographic hash function used to calculate the HMAC from which a password is derived.
The supported algorithms are SHA-1, SHA-256, and SHA-512.
"""
class Algorithm(Enum):
    # The SHA-1 hash function.
    SHA1 = 1
    # The SHA-256 hash function.
    SHA256 = 2
    # The SHA-512 hash function.
    SHA512 = 3

"""An error type enum representing the various errors a `Generator` can throw when computing a
password.
"""
class Error(Enum):
    # The requested time is before the epoch date.
    INVALID_TIME = 1
    # The timer period is not a positive number of seconds.
    INVALID_PERIOD = 2
    # The number of digits is either too short to be secure, or too long to compute.
    INVALID_DIGITS = 3
