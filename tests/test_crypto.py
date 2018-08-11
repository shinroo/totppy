#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from pytotp import (
    crypto,
    Algorithm
)

class CryptoTest(unittest.TestCase):

    def test_hmac(self):
        hmac = crypto.HMAC(Algorithm.SHA1, 'E49756B4C8FAB4E4', b'test')
        self.assertIsNotNone(hmac)
        hmac = crypto.HMAC(Algorithm.SHA256, 'E49756B4C8FAB4E48222A3E7F3B97CC3', b'test')
        self.assertIsNotNone(hmac)
        hmac = crypto.HMAC(Algorithm.SHA512, 'E49756B4C8FAB4E48222A3E7F3B97CC3E49756B4C8FAB4E48222A3E7F3B97CC3', b'test')
        self.assertIsNotNone(hmac)
