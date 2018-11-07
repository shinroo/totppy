#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64

def encode(str_to_encode):
    """Encodes given str with base32.
    Args:
      str_to_encode (str):
        str to be encoded.
    Returns:
      Base32 encoded bytes.
    """

    return base64.b32encode(str.encode(str_to_encode))

def decode(bytes_to_decode):
    """Decodes given bytes with base32.
    Args:
      bytes_to_decode (bytes):
        bytes to be decoded.
    Returns:
      Base32 decoded str.
    """

    return base64.b32decode(bytes_to_decode).decode('utf-8')
