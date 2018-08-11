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
