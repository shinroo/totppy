#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64

def encode(str_to_encode):
    return base64.b32encode(str.encode(str_to_encode))

def decode(bytes_to_decode):
    return base64.b32decode(bytes_to_decode).decode('utf-8')
