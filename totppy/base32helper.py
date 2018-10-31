#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64

"""Encodes given str with base32.
Args:
  str_to_encode (str):
    str to be encoded.
Returns:
  Base32 encoded bytes.
"""
def encode(str_to_encode):
    return base64.b32encode(str.encode(str_to_encode))

"""Decodes given bytes with base32.
Args:
  bytes_to_decode (bytes):
    bytes to be decoded.
Returns:
  Base32 decoded str.
"""
def decode(bytes_to_decode):
    return base64.b32decode(bytes_to_decode).decode('utf-8')
