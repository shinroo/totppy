#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hmac
import hashlib
import binascii

from .enums import Algorithm

def HMAC(algorithm, key, data):
      """Return a new hmac object.
      Args:
        algorithm (enum):
          Enum type from `Algorithm`.
        key (str):
          Key for the keyed hash object.
        data (bytes):
          Initial input for the hash, if provided.
      """

    byte_key = key.encode()
    if algorithm == Algorithm.SHA1:
        return hmac.new(byte_key, msg=data, digestmod=hashlib.sha1).hexdigest().upper()
    elif algorithm == Algorithm.SHA256:
        return hmac.new(byte_key, msg=data, digestmod=hashlib.sha256).hexdigest().upper()
    else:
        return hmac.new(byte_key, msg=data, digestmod=hashlib.sha512).hexdigest().upper()
